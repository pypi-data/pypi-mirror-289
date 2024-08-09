from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateNewQuickReply(TLObject):  # type: ignore
    __slots__: List[str] = ["quick_reply"]

    ID = 0xf53da717
    QUALNAME = "types.UpdateNewQuickReply"

    def __init__(self, *, quick_reply: "raw.base.QuickReply") -> None:
        self.quick_reply = quick_reply  # QuickReply

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNewQuickReply":
        # No flags
        
        quick_reply = TLObject.read(b)
        
        return UpdateNewQuickReply(quick_reply=quick_reply)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.quick_reply.write())
        
        return b.getvalue()
