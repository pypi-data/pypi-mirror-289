from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdatePinnedForumTopic(TLObject):  # type: ignore
    __slots__: List[str] = ["channel", "topic_id", "pinned"]

    ID = 0x6c2d9026
    QUALNAME = "functions.channels.UpdatePinnedForumTopic"

    def __init__(self, *, channel: "raw.base.InputChannel", topic_id: int, pinned: bool) -> None:
        self.channel = channel  # InputChannel
        self.topic_id = topic_id  # int
        self.pinned = pinned  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePinnedForumTopic":
        # No flags
        
        channel = TLObject.read(b)
        
        topic_id = Int.read(b)
        
        pinned = Bool.read(b)
        
        return UpdatePinnedForumTopic(channel=channel, topic_id=topic_id, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(Int(self.topic_id))
        
        b.write(Bool(self.pinned))
        
        return b.getvalue()
