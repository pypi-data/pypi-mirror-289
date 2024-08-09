from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ChannelAdminLogEventActionChangeProfilePeerColor(TLObject):  # type: ignore
    __slots__: List[str] = ["prev_value", "new_value"]

    ID = 0x5e477b25
    QUALNAME = "types.ChannelAdminLogEventActionChangeProfilePeerColor"

    def __init__(self, *, prev_value: "raw.base.PeerColor", new_value: "raw.base.PeerColor") -> None:
        self.prev_value = prev_value  # PeerColor
        self.new_value = new_value  # PeerColor

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelAdminLogEventActionChangeProfilePeerColor":
        # No flags
        
        prev_value = TLObject.read(b)
        
        new_value = TLObject.read(b)
        
        return ChannelAdminLogEventActionChangeProfilePeerColor(prev_value=prev_value, new_value=new_value)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.prev_value.write())
        
        b.write(self.new_value.write())
        
        return b.getvalue()
