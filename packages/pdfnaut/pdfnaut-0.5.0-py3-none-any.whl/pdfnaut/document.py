from __future__ import annotations

from typing import Any, Generator, TypeVar, cast, overload

from .cos.parser import PdfParser, PermsAcquired
from .cos.objects import PdfReference, PdfObject, PdfStream, PdfXRefEntry
from .typings.document import Catalog, Info, Outlines, Page, PageTree, Trailer, XRefStream


class PdfDocument:
    """A high-level interface over :class:`~pdfnaut.cos.parser.PdfParser`"""
    
    @classmethod
    def from_filename(cls, path: str, *, strict: bool = False) -> PdfDocument:
        """Loads a PDF document from a file ``path``."""
        with open(path, "rb") as fp:
            return PdfDocument(fp.read(), strict=strict)

    def __init__(self, data: bytes, *, strict: bool = False) -> None:
        self._reader = PdfParser(data, strict=strict)
        self._reader.parse()

        self.access_level = PermsAcquired.OWNER
        """The current access level of the document, specified as a value from the
        :class:`.PermsAcquired` enum.
        
        - Owner: Full access to the document. If the document is not encrypted, \
        this is the default value.
        - User: Access to the document under restrictions.
        - None: Document is currently encrypted.
        """

        # some files use an empty string as a password
        if self.has_encryption:
            self.access_level = self.decrypt("")

    T = TypeVar("T")
    @overload
    def get_object(self, reference: PdfReference[T]) -> T:
        ...
    
    @overload
    def get_object(self, reference: tuple[int, int]) -> PdfObject | PdfStream:
        ...
    
    def get_object(self, reference: PdfReference | tuple[int, int]) -> PdfObject | PdfStream | Any:
        """Resolves a reference into the indirect object it points to.
        
        Arguments:
            reference (:class:`.PdfIndirectRef` | :class:`tuple[int, int]`): 
                A :class:`.PdfIndirectRef` object or a tuple of two integers representing, 
                in order, the object number and the generation number.
  
        Returns:
            The object the reference resolves to if valid, otherwise :class:`.PdfNull`.
        """
        return self._reader.get_object(reference)

    @property
    def has_encryption(self) -> bool:
        """Whether this document includes encryption."""
        return "Encrypt" in self._reader.trailer
    
    @property 
    def trailer(self) -> Trailer | XRefStream:
        """The PDF trailer which allows access to other core parts of the PDF structure. 
        
        For documents using an XRef stream, the stream extent is returned. See 
        ``§ 7.5.8.2 Cross-Reference Stream Dictionary`` and :class:`.XRefStream` 
        for more details.
                
        For details on the contents of the trailer, see ``§ 7.5.5 File Trailer`` in the 
        PDF spec."""
        return self._reader.trailer
    
    @property
    def xref(self) -> dict[tuple[int, int], PdfXRefEntry]:
        """A cross-reference mapping combining the entries of all XRef tables present 
        in the document.
        
        The key is a tuple of two integers: object number and generation number. 
        The value is any of the 3 types of XRef entries (free, in use, compressed)
        """
        return self._reader.xref

    @property
    def catalog(self) -> Catalog:
        """The root of the document's object hierarchy, including references to pages, 
        outlines, destinations, and other core attributes of a PDF document.
        
        For details on the contents of the catalog, see ``§ 7.7.2 Document Catalog``. 
        """
        return self.get_object(self._reader.trailer["Root"])
    
    @property
    def info(self) -> Info | None:
        """The ``Info`` entry in the catalog which includes document-level information.
        
        Some documents may specify a metadata stream rather than an Info entry. This can be
        accessed with :attr:`.PdfDocument.metadata`. PDF 2.0 deprecates all keys of this
        entry except for ``CreationDate`` and ``ModDate``.
        """
        if "Info" not in self.trailer:
            return
        return self._reader._ensure_object(self.trailer["Info"])

    @property
    def metadata(self) -> PdfStream | None:
        """The Metadata entry of the catalog which includes document-level metadata 
        stored as XMP."""
        if "Metadata" not in self.catalog:
            return    
        return self.get_object(self.catalog["Metadata"])

    @property
    def page_tree(self) -> PageTree:
        """The document's page tree. See ``§ 7.7.3 Page Tree``.

        For iterating over the pages of a PDF, prefer :attr:`.PdfDocument.flattened_pages`.
        """
        return self.get_object(self.catalog["Pages"])

    @property
    def outline_tree(self) -> Outlines | None:
        """The document's outlines commonly referred to as bookmarks. 
        
        See ``§ 12.3.3 Document Outline``."""
        if "Outlines" not in self.catalog:
            return
        return self.get_object(self.catalog["Outlines"])

    def decrypt(self, password: str) -> PermsAcquired:
        """Decrypts this document assuming it was encrypted with a ``password``.
        
        The Standard security handler may specify 2 passwords:
        - An owner password, allowing full access to the PDF
        - A user password, allowing restricted access to the PDF according to its permissions.

        Returns:
            A :class:`.PermsAcquired` specifying the permissions acquired by ``password``.
            
            - If the document is not encrypted, defaults to :attr:`.PermsAcquired.OWNER`
            - if the document was not decrypted, defaults to :attr:`.PermsAcquired.NONE`
        """
        self.access_level = self._reader.decrypt(password)
        return self.access_level
    
    def _flatten_pages(self, *, parent: PageTree | None = None) -> Generator[Page, None, None]:
        root = parent or self.page_tree

        for child in root["Kids"]:
            page = self.get_object(child)
            
            if page["Type"].value == b"Pages":
                yield from self._flatten_pages(parent=cast(PageTree, page))
            elif page["Type"].value == b"Page":
                yield cast(Page, page)

    @property
    def flattened_pages(self) -> Generator[Page, None, None]:
        """A generator suitable for iterating over the pages of a PDF."""
        return self._flatten_pages()
