from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputStickerSetDice(TLObject):  # type: ignore
    __slots__: List[str] = ["emoticon"]

    ID = 0xe67f520e
    QUALNAME = "types.InputStickerSetDice"

    def __init__(self, *, emoticon: str) -> None:
        self.emoticon = emoticon  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStickerSetDice":
        # No flags
        
        emoticon = String.read(b)
        
        return InputStickerSetDice(emoticon=emoticon)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.emoticon))
        
        return b.getvalue()
