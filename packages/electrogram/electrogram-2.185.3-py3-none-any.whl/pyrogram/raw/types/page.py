from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class Page(TLObject):  # type: ignore
    __slots__: List[str] = ["url", "blocks", "photos", "documents", "part", "rtl", "v2", "views"]

    ID = 0x98657f0d
    QUALNAME = "types.Page"

    def __init__(self, *, url: str, blocks: List["raw.base.PageBlock"], photos: List["raw.base.Photo"], documents: List["raw.base.Document"], part: Optional[bool] = None, rtl: Optional[bool] = None, v2: Optional[bool] = None, views: Optional[int] = None) -> None:
        self.url = url  # string
        self.blocks = blocks  # Vector<PageBlock>
        self.photos = photos  # Vector<Photo>
        self.documents = documents  # Vector<Document>
        self.part = part  # flags.0?true
        self.rtl = rtl  # flags.1?true
        self.v2 = v2  # flags.2?true
        self.views = views  # flags.3?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Page":
        
        flags = Int.read(b)
        
        part = True if flags & (1 << 0) else False
        rtl = True if flags & (1 << 1) else False
        v2 = True if flags & (1 << 2) else False
        url = String.read(b)
        
        blocks = TLObject.read(b)
        
        photos = TLObject.read(b)
        
        documents = TLObject.read(b)
        
        views = Int.read(b) if flags & (1 << 3) else None
        return Page(url=url, blocks=blocks, photos=photos, documents=documents, part=part, rtl=rtl, v2=v2, views=views)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.part else 0
        flags |= (1 << 1) if self.rtl else 0
        flags |= (1 << 2) if self.v2 else 0
        flags |= (1 << 3) if self.views is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.url))
        
        b.write(Vector(self.blocks))
        
        b.write(Vector(self.photos))
        
        b.write(Vector(self.documents))
        
        if self.views is not None:
            b.write(Int(self.views))
        
        return b.getvalue()
