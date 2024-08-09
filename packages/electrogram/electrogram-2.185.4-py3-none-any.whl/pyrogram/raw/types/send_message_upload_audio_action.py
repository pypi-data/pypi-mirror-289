from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SendMessageUploadAudioAction(TLObject):  # type: ignore
    __slots__: List[str] = ["progress"]

    ID = 0xf351d7ab
    QUALNAME = "types.SendMessageUploadAudioAction"

    def __init__(self, *, progress: int) -> None:
        self.progress = progress  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendMessageUploadAudioAction":
        # No flags
        
        progress = Int.read(b)
        
        return SendMessageUploadAudioAction(progress=progress)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.progress))
        
        return b.getvalue()
