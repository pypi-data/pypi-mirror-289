from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChannelAvailableMessages(TLObject):  # type: ignore
    __slots__: List[str] = ["channel_id", "available_min_id"]

    ID = 0xb23fc698
    QUALNAME = "types.UpdateChannelAvailableMessages"

    def __init__(self, *, channel_id: int, available_min_id: int) -> None:
        self.channel_id = channel_id  # long
        self.available_min_id = available_min_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelAvailableMessages":
        # No flags
        
        channel_id = Long.read(b)
        
        available_min_id = Int.read(b)
        
        return UpdateChannelAvailableMessages(channel_id=channel_id, available_min_id=available_min_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(Int(self.available_min_id))
        
        return b.getvalue()
