from __future__ import annotations

from typing import cast, Any, TypeVar

from dataclasses import dataclass

from _future.good import ObjectGetter, PdfDictionary
from pdfnaut.document import PdfDocument
from pdfnaut.typings.document import Trailer
from ..cos.objects import PdfHexString, PdfReference


def omit_false_entries(dictionary: PdfDictionary[str, Any], 
                       except_: list[str] | None = None) -> PdfDictionary[str, Any]:
    if except_ is None:
        except_ = []

    result = PdfDictionary({ 
        key: val for key, val in dictionary.items() 
        if val or key in except_ 
    })
    
    if hasattr(dictionary, "_resolver"):
        result._resolver = dictionary._resolver
    
    return result


T = TypeVar("T")
MaybeRef = PdfReference[T] | T


class TrailerDict:
    Size


@dataclass
class TrailerNew:
    _resolver: ObjectGetter

    size: int
    """The total number of entries in the combined cross-reference table."""

    root_ref: PdfReference[str]
    """A reference to the document's catalog."""
    
    prev: int | None = None
    """The offset of the previous trailer if present."""
    
    encrypt_ref_or_val: MaybeRef[str] | None = None
    """A possible reference to the document's encryption dictionary."""

    info_ref: PdfReference[str] | None = None
    """A reference to the document-level information dictionary."""
    
    identifiers: list[PdfHexString | bytes] | None = None
    """A list of two bytestrings constituting a file identifier. The first bytestring is 
    produced when the document is first created and shall not change while the second 
    bytestring shall change when the document is modified."""
    
    
    @classmethod
    def from_dict(cls, mapping: PdfDictionary[str, Any]):
        return cls(
            _resolver=mapping._resolver,
            size=mapping["Size"],
            prev=mapping.get("Prev"),
            root_ref=mapping.raw_at("Root"),
            encrypt_ref_or_val=mapping.get_raw("Encrypt"),
            info_ref=mapping.get_raw("Info"),
            identifiers=mapping.get("ID")
        )
    
    def to_dict(self) -> PdfDictionary[str, Any]:
        dictionary = omit_false_entries(
            PdfDictionary({
                "Size": self.size,
                "Prev": self.prev,
                "Root": self.root_ref,
                "Encrypt": self.encrypt_ref_or_val,
                "Info": self.info_ref,
                "ID": self.identifiers
            }), ["Size", "Root"]
        )
        return dictionary.with_resolver(self._resolver)


if __name__ == "__main__":
    document = PdfDocument.from_filename(r"C:\Users\Micro\Code\Python\pdfnaut\examples\pdfs\Andrew S. Tanenbaum - Modern Operating Systems.pdf")
    
    trailer = cast(Trailer | PdfDictionary, PdfDictionary(cast(dict[str, Any], document.trailer)))
    print(trailer.at("Size"))
    # trailer = PdfDictionary(cast(dict[str, Any], document.trailer)).with_resolver(document.get_object))
    
    # print(trailer.to_dict()["Root"])