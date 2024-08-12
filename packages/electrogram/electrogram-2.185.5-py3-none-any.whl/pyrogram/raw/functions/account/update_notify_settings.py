from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateNotifySettings(TLObject):  # type: ignore
    __slots__: List[str] = ["peer", "settings"]

    ID = 0x84be5b93
    QUALNAME = "functions.account.UpdateNotifySettings"

    def __init__(self, *, peer: "raw.base.InputNotifyPeer", settings: "raw.base.InputPeerNotifySettings") -> None:
        self.peer = peer  # InputNotifyPeer
        self.settings = settings  # InputPeerNotifySettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateNotifySettings":
        # No flags
        
        peer = TLObject.read(b)
        
        settings = TLObject.read(b)
        
        return UpdateNotifySettings(peer=peer, settings=settings)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.settings.write())
        
        return b.getvalue()
