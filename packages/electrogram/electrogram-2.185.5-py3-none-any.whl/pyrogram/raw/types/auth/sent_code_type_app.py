from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SentCodeTypeApp(TLObject):  # type: ignore
    __slots__: List[str] = ["length"]

    ID = 0x3dbb5986
    QUALNAME = "types.auth.SentCodeTypeApp"

    def __init__(self, *, length: int) -> None:
        self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SentCodeTypeApp":
        # No flags
        
        length = Int.read(b)
        
        return SentCodeTypeApp(length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.length))
        
        return b.getvalue()
