from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .base import PdfName, PdfNull
from ...filters import SUPPORTED_FILTERS
from ...exceptions import PdfFilterError


@dataclass
class PdfStream:
    """A sequence of bytes that may be of unlimited length. Objects with a large 
    amount of data like images or fonts are usually represented by streams 
    (``§ 7.3.8 Stream objects``)."""
    # no type here yet because details can be an extent plus a lot of other things
    details: dict[str, Any]
    raw: bytes = field(repr=False)
    _sec_handler: dict[str, Any] = field(default_factory=dict, repr=False)

    def decode(self) -> bytes:
        """Returns the decoded contents of the stream. If no filter is defined, 
        it returns the original contents.
        
        Raises :class:`.pdfnaut.exceptions.PdfFilterError` if a filter is unsupported."""

        filters = self.details.get("Filter")
        params = self.details.get("DecodeParms")
            
        if filters is None:
            return self.raw
        
        if isinstance(filters, PdfName):
            filters = [filters]

        if not isinstance(params, list):
            params = [params]

        output = self.raw

        for filt, params in zip(filters, params):
            if filt.value not in SUPPORTED_FILTERS:
                raise PdfFilterError(f"{filt.value.decode()}: Filter is unsupported.")
            
            if isinstance(params, PdfNull) or params is None:
                params = {}
            
            if filt.value == b"Crypt" and self._sec_handler.get("_Handler"):
                params.update(self._sec_handler)
            
            output = SUPPORTED_FILTERS[filt.value]().decode(self.raw, params=params)

        return output
