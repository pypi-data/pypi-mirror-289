from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ClearAllDrafts(TLObject):  # type: ignore
    __slots__: List[str] = []

    ID = 0x7e58ee9c
    QUALNAME = "functions.messages.ClearAllDrafts"

    def __init__(self) -> None:
        pass

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ClearAllDrafts":
        # No flags
        
        return ClearAllDrafts()

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        return b.getvalue()
