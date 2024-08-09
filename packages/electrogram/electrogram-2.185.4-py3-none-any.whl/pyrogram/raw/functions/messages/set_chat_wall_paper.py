from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetChatWallPaper(TLObject):  # type: ignore
    __slots__: List[str] = ["peer", "for_both", "revert", "wallpaper", "settings", "id"]

    ID = 0x8ffacae1
    QUALNAME = "functions.messages.SetChatWallPaper"

    def __init__(self, *, peer: "raw.base.InputPeer", for_both: Optional[bool] = None, revert: Optional[bool] = None, wallpaper: "raw.base.InputWallPaper" = None, settings: "raw.base.WallPaperSettings" = None, id: Optional[int] = None) -> None:
        self.peer = peer  # InputPeer
        self.for_both = for_both  # flags.3?true
        self.revert = revert  # flags.4?true
        self.wallpaper = wallpaper  # flags.0?InputWallPaper
        self.settings = settings  # flags.2?WallPaperSettings
        self.id = id  # flags.1?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetChatWallPaper":
        
        flags = Int.read(b)
        
        for_both = True if flags & (1 << 3) else False
        revert = True if flags & (1 << 4) else False
        peer = TLObject.read(b)
        
        wallpaper = TLObject.read(b) if flags & (1 << 0) else None
        
        settings = TLObject.read(b) if flags & (1 << 2) else None
        
        id = Int.read(b) if flags & (1 << 1) else None
        return SetChatWallPaper(peer=peer, for_both=for_both, revert=revert, wallpaper=wallpaper, settings=settings, id=id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.for_both else 0
        flags |= (1 << 4) if self.revert else 0
        flags |= (1 << 0) if self.wallpaper is not None else 0
        flags |= (1 << 2) if self.settings is not None else 0
        flags |= (1 << 1) if self.id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        if self.wallpaper is not None:
            b.write(self.wallpaper.write())
        
        if self.settings is not None:
            b.write(self.settings.write())
        
        if self.id is not None:
            b.write(Int(self.id))
        
        return b.getvalue()
