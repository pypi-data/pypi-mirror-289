from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class MessageEditData(TLObject):  # type: ignore
    __slots__: List[str] = ["caption"]

    ID = 0x26b5dde6
    QUALNAME = "types.messages.MessageEditData"

    def __init__(self, *, caption: Optional[bool] = None) -> None:
        self.caption = caption  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageEditData":
        
        flags = Int.read(b)
        
        caption = True if flags & (1 << 0) else False
        return MessageEditData(caption=caption)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.caption else 0
        b.write(Int(flags))
        
        return b.getvalue()
