from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class DeletePhoneCallHistory(TLObject):  # type: ignore
    __slots__: List[str] = ["revoke"]

    ID = 0xf9cbe409
    QUALNAME = "functions.messages.DeletePhoneCallHistory"

    def __init__(self, *, revoke: Optional[bool] = None) -> None:
        self.revoke = revoke  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DeletePhoneCallHistory":
        
        flags = Int.read(b)
        
        revoke = True if flags & (1 << 0) else False
        return DeletePhoneCallHistory(revoke=revoke)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.revoke else 0
        b.write(Int(flags))
        
        return b.getvalue()
