from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputStorePaymentPremiumSubscription(TLObject):  # type: ignore
    __slots__: List[str] = ["restore", "upgrade"]

    ID = 0xa6751e66
    QUALNAME = "types.InputStorePaymentPremiumSubscription"

    def __init__(self, *, restore: Optional[bool] = None, upgrade: Optional[bool] = None) -> None:
        self.restore = restore  # flags.0?true
        self.upgrade = upgrade  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentPremiumSubscription":
        
        flags = Int.read(b)
        
        restore = True if flags & (1 << 0) else False
        upgrade = True if flags & (1 << 1) else False
        return InputStorePaymentPremiumSubscription(restore=restore, upgrade=upgrade)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.restore else 0
        flags |= (1 << 1) if self.upgrade else 0
        b.write(Int(flags))
        
        return b.getvalue()
