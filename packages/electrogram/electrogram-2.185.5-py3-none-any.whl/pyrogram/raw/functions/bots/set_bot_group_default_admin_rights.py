from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class SetBotGroupDefaultAdminRights(TLObject):  # type: ignore
    __slots__: List[str] = ["admin_rights"]

    ID = 0x925ec9ea
    QUALNAME = "functions.bots.SetBotGroupDefaultAdminRights"

    def __init__(self, *, admin_rights: "raw.base.ChatAdminRights") -> None:
        self.admin_rights = admin_rights  # ChatAdminRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetBotGroupDefaultAdminRights":
        # No flags
        
        admin_rights = TLObject.read(b)
        
        return SetBotGroupDefaultAdminRights(admin_rights=admin_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.admin_rights.write())
        
        return b.getvalue()
