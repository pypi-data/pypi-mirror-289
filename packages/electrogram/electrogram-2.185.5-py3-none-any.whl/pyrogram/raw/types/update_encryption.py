from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateEncryption(TLObject):  # type: ignore
    __slots__: List[str] = ["chat", "date"]

    ID = 0xb4a2e88d
    QUALNAME = "types.UpdateEncryption"

    def __init__(self, *, chat: "raw.base.EncryptedChat", date: int) -> None:
        self.chat = chat  # EncryptedChat
        self.date = date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateEncryption":
        # No flags
        
        chat = TLObject.read(b)
        
        date = Int.read(b)
        
        return UpdateEncryption(chat=chat, date=date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.chat.write())
        
        b.write(Int(self.date))
        
        return b.getvalue()
