from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChatForbidden(TLObject):  # type: ignore
    __slots__: List[str] = ["id", "title"]

    ID = 0x6592a1a7
    QUALNAME = "types.ChatForbidden"

    def __init__(self, *, id: int, title: str) -> None:
        self.id = id  # long
        self.title = title  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatForbidden":
        # No flags
        
        id = Long.read(b)
        
        title = String.read(b)
        
        return ChatForbidden(id=id, title=title)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(String(self.title))
        
        return b.getvalue()
