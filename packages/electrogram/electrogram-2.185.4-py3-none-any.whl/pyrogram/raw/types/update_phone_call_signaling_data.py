from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdatePhoneCallSignalingData(TLObject):  # type: ignore
    __slots__: List[str] = ["phone_call_id", "data"]

    ID = 0x2661bf09
    QUALNAME = "types.UpdatePhoneCallSignalingData"

    def __init__(self, *, phone_call_id: int, data: bytes) -> None:
        self.phone_call_id = phone_call_id  # long
        self.data = data  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePhoneCallSignalingData":
        # No flags
        
        phone_call_id = Long.read(b)
        
        data = Bytes.read(b)
        
        return UpdatePhoneCallSignalingData(phone_call_id=phone_call_id, data=data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.phone_call_id))
        
        b.write(Bytes(self.data))
        
        return b.getvalue()
