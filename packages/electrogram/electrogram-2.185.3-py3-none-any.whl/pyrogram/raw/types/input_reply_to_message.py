from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputReplyToMessage(TLObject):  # type: ignore
    __slots__: List[str] = ["reply_to_msg_id", "top_msg_id", "reply_to_peer_id", "quote_text", "quote_entities", "quote_offset"]

    ID = 0x22c0f6d5
    QUALNAME = "types.InputReplyToMessage"

    def __init__(self, *, reply_to_msg_id: int, top_msg_id: Optional[int] = None, reply_to_peer_id: "raw.base.InputPeer" = None, quote_text: Optional[str] = None, quote_entities: Optional[List["raw.base.MessageEntity"]] = None, quote_offset: Optional[int] = None) -> None:
        self.reply_to_msg_id = reply_to_msg_id  # int
        self.top_msg_id = top_msg_id  # flags.0?int
        self.reply_to_peer_id = reply_to_peer_id  # flags.1?InputPeer
        self.quote_text = quote_text  # flags.2?string
        self.quote_entities = quote_entities  # flags.3?Vector<MessageEntity>
        self.quote_offset = quote_offset  # flags.4?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputReplyToMessage":
        
        flags = Int.read(b)
        
        reply_to_msg_id = Int.read(b)
        
        top_msg_id = Int.read(b) if flags & (1 << 0) else None
        reply_to_peer_id = TLObject.read(b) if flags & (1 << 1) else None
        
        quote_text = String.read(b) if flags & (1 << 2) else None
        quote_entities = TLObject.read(b) if flags & (1 << 3) else []
        
        quote_offset = Int.read(b) if flags & (1 << 4) else None
        return InputReplyToMessage(reply_to_msg_id=reply_to_msg_id, top_msg_id=top_msg_id, reply_to_peer_id=reply_to_peer_id, quote_text=quote_text, quote_entities=quote_entities, quote_offset=quote_offset)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.top_msg_id is not None else 0
        flags |= (1 << 1) if self.reply_to_peer_id is not None else 0
        flags |= (1 << 2) if self.quote_text is not None else 0
        flags |= (1 << 3) if self.quote_entities else 0
        flags |= (1 << 4) if self.quote_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.reply_to_msg_id))
        
        if self.top_msg_id is not None:
            b.write(Int(self.top_msg_id))
        
        if self.reply_to_peer_id is not None:
            b.write(self.reply_to_peer_id.write())
        
        if self.quote_text is not None:
            b.write(String(self.quote_text))
        
        if self.quote_entities is not None:
            b.write(Vector(self.quote_entities))
        
        if self.quote_offset is not None:
            b.write(Int(self.quote_offset))
        
        return b.getvalue()
