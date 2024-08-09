from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class UpdateDialogFilter(TLObject):  # type: ignore
    __slots__: List[str] = ["id", "filter"]

    ID = 0x26ffde7d
    QUALNAME = "types.UpdateDialogFilter"

    def __init__(self, *, id: int, filter: "raw.base.DialogFilter" = None) -> None:
        self.id = id  # int
        self.filter = filter  # flags.0?DialogFilter

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateDialogFilter":
        
        flags = Int.read(b)
        
        id = Int.read(b)
        
        filter = TLObject.read(b) if flags & (1 << 0) else None
        
        return UpdateDialogFilter(id=id, filter=filter)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.filter is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.id))
        
        if self.filter is not None:
            b.write(self.filter.write())
        
        return b.getvalue()
