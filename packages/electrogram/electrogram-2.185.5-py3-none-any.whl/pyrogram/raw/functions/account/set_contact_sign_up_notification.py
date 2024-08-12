from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetContactSignUpNotification(TLObject):  # type: ignore
    __slots__: List[str] = ["silent"]

    ID = 0xcff43f61
    QUALNAME = "functions.account.SetContactSignUpNotification"

    def __init__(self, *, silent: bool) -> None:
        self.silent = silent  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetContactSignUpNotification":
        # No flags
        
        silent = Bool.read(b)
        
        return SetContactSignUpNotification(silent=silent)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bool(self.silent))
        
        return b.getvalue()
