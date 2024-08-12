from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class ToggleConnectedBotPaused(TLObject):  # type: ignore
    __slots__: List[str] = ["peer", "paused"]

    ID = 0x646e1097
    QUALNAME = "functions.account.ToggleConnectedBotPaused"

    def __init__(self, *, peer: "raw.base.InputPeer", paused: bool) -> None:
        self.peer = peer  # InputPeer
        self.paused = paused  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleConnectedBotPaused":
        # No flags
        
        peer = TLObject.read(b)
        
        paused = Bool.read(b)
        
        return ToggleConnectedBotPaused(peer=peer, paused=paused)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Bool(self.paused))
        
        return b.getvalue()
