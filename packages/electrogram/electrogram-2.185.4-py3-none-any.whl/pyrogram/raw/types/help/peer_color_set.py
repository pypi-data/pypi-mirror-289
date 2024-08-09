from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class PeerColorSet(TLObject):  # type: ignore
    __slots__: List[str] = ["colors"]

    ID = 0x26219a58
    QUALNAME = "types.help.PeerColorSet"

    def __init__(self, *, colors: List[int]) -> None:
        self.colors = colors  # Vector<int>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PeerColorSet":
        # No flags
        
        colors = TLObject.read(b, Int)
        
        return PeerColorSet(colors=colors)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Vector(self.colors, Int))
        
        return b.getvalue()
