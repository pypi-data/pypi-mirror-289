from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateBusinessAwayMessage(TLObject):  # type: ignore
    __slots__: List[str] = ["message"]

    ID = 0xa26a7fa5
    QUALNAME = "functions.account.UpdateBusinessAwayMessage"

    def __init__(self, *, message: "raw.base.InputBusinessAwayMessage" = None) -> None:
        self.message = message  # flags.0?InputBusinessAwayMessage

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateBusinessAwayMessage":
        
        flags = Int.read(b)
        
        message = TLObject.read(b) if flags & (1 << 0) else None
        
        return UpdateBusinessAwayMessage(message=message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.message is not None else 0
        b.write(Int(flags))
        
        if self.message is not None:
            b.write(self.message.write())
        
        return b.getvalue()
