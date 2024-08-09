from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelParticipantSelf(TLObject):  # type: ignore
    __slots__: List[str] = ["user_id", "inviter_id", "date", "via_request"]

    ID = 0x35a8bfa7
    QUALNAME = "types.ChannelParticipantSelf"

    def __init__(self, *, user_id: int, inviter_id: int, date: int, via_request: Optional[bool] = None) -> None:
        self.user_id = user_id  # long
        self.inviter_id = inviter_id  # long
        self.date = date  # int
        self.via_request = via_request  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantSelf":
        
        flags = Int.read(b)
        
        via_request = True if flags & (1 << 0) else False
        user_id = Long.read(b)
        
        inviter_id = Long.read(b)
        
        date = Int.read(b)
        
        return ChannelParticipantSelf(user_id=user_id, inviter_id=inviter_id, date=date, via_request=via_request)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.via_request else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(Long(self.inviter_id))
        
        b.write(Int(self.date))
        
        return b.getvalue()
