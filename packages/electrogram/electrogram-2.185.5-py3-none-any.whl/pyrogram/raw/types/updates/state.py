from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class State(TLObject):  # type: ignore
    __slots__: List[str] = ["pts", "qts", "date", "seq", "unread_count"]

    ID = 0xa56c2a3e
    QUALNAME = "types.updates.State"

    def __init__(self, *, pts: int, qts: int, date: int, seq: int, unread_count: int) -> None:
        self.pts = pts  # int
        self.qts = qts  # int
        self.date = date  # int
        self.seq = seq  # int
        self.unread_count = unread_count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "State":
        # No flags
        
        pts = Int.read(b)
        
        qts = Int.read(b)
        
        date = Int.read(b)
        
        seq = Int.read(b)
        
        unread_count = Int.read(b)
        
        return State(pts=pts, qts=qts, date=date, seq=seq, unread_count=unread_count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.pts))
        
        b.write(Int(self.qts))
        
        b.write(Int(self.date))
        
        b.write(Int(self.seq))
        
        b.write(Int(self.unread_count))
        
        return b.getvalue()
