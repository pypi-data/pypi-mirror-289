from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateChannelViewForumAsMessages(TLObject):  # type: ignore
    __slots__: List[str] = ["channel_id", "enabled"]

    ID = 0x7b68920
    QUALNAME = "types.UpdateChannelViewForumAsMessages"

    def __init__(self, *, channel_id: int, enabled: bool) -> None:
        self.channel_id = channel_id  # long
        self.enabled = enabled  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateChannelViewForumAsMessages":
        # No flags
        
        channel_id = Long.read(b)
        
        enabled = Bool.read(b)
        
        return UpdateChannelViewForumAsMessages(channel_id=channel_id, enabled=enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.channel_id))
        
        b.write(Bool(self.enabled))
        
        return b.getvalue()
