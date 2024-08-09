from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UploadMedia(TLObject):  # type: ignore
    __slots__: List[str] = ["peer", "media", "business_connection_id"]

    ID = 0x14967978
    QUALNAME = "functions.messages.UploadMedia"

    def __init__(self, *, peer: "raw.base.InputPeer", media: "raw.base.InputMedia", business_connection_id: Optional[str] = None) -> None:
        self.peer = peer  # InputPeer
        self.media = media  # InputMedia
        self.business_connection_id = business_connection_id  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UploadMedia":
        
        flags = Int.read(b)
        
        business_connection_id = String.read(b) if flags & (1 << 0) else None
        peer = TLObject.read(b)
        
        media = TLObject.read(b)
        
        return UploadMedia(peer=peer, media=media, business_connection_id=business_connection_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.business_connection_id is not None else 0
        b.write(Int(flags))
        
        if self.business_connection_id is not None:
            b.write(String(self.business_connection_id))
        
        b.write(self.peer.write())
        
        b.write(self.media.write())
        
        return b.getvalue()
