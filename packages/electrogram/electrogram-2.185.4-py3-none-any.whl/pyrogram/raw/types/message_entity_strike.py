from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageEntityStrike(TLObject):  # type: ignore
    __slots__: List[str] = ["offset", "length"]

    ID = 0xbf0693d4
    QUALNAME = "types.MessageEntityStrike"

    def __init__(self, *, offset: int, length: int) -> None:
        self.offset = offset  # int
        self.length = length  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEntityStrike":
        # No flags
        
        offset = Int.read(b)
        
        length = Int.read(b)
        
        return MessageEntityStrike(offset=offset, length=length)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.offset))
        
        b.write(Int(self.length))
        
        return b.getvalue()
