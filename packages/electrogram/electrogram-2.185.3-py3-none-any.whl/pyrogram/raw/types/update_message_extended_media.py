from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateMessageExtendedMedia(TLObject):  # type: ignore
    __slots__: List[str] = ["peer", "msg_id", "extended_media"]

    ID = 0xd5a41724
    QUALNAME = "types.UpdateMessageExtendedMedia"

    def __init__(self, *, peer: "raw.base.Peer", msg_id: int, extended_media: List["raw.base.MessageExtendedMedia"]) -> None:
        self.peer = peer  # Peer
        self.msg_id = msg_id  # int
        self.extended_media = extended_media  # Vector<MessageExtendedMedia>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateMessageExtendedMedia":
        # No flags
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        extended_media = TLObject.read(b)
        
        return UpdateMessageExtendedMedia(peer=peer, msg_id=msg_id, extended_media=extended_media)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Vector(self.extended_media))
        
        return b.getvalue()
