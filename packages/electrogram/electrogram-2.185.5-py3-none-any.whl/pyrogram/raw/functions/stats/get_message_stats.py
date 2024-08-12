from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class GetMessageStats(TLObject):  # type: ignore
    __slots__: List[str] = ["channel", "msg_id", "dark"]

    ID = 0xb6e0a3f5
    QUALNAME = "functions.stats.GetMessageStats"

    def __init__(self, *, channel: "raw.base.InputChannel", msg_id: int, dark: Optional[bool] = None) -> None:
        self.channel = channel  # InputChannel
        self.msg_id = msg_id  # int
        self.dark = dark  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetMessageStats":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        channel = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        return GetMessageStats(channel=channel, msg_id=msg_id, dark=dark)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        b.write(Int(flags))
        
        b.write(self.channel.write())
        
        b.write(Int(self.msg_id))
        
        return b.getvalue()
