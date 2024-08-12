from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputStorePaymentPremiumGiftCode(TLObject):  # type: ignore
    __slots__: List[str] = ["users", "currency", "amount", "boost_peer"]

    ID = 0xa3805f3f
    QUALNAME = "types.InputStorePaymentPremiumGiftCode"

    def __init__(self, *, users: List["raw.base.InputUser"], currency: str, amount: int, boost_peer: "raw.base.InputPeer" = None) -> None:
        self.users = users  # Vector<InputUser>
        self.currency = currency  # string
        self.amount = amount  # long
        self.boost_peer = boost_peer  # flags.0?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentPremiumGiftCode":
        
        flags = Int.read(b)
        
        users = TLObject.read(b)
        
        boost_peer = TLObject.read(b) if flags & (1 << 0) else None
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return InputStorePaymentPremiumGiftCode(users=users, currency=currency, amount=amount, boost_peer=boost_peer)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.boost_peer is not None else 0
        b.write(Int(flags))
        
        b.write(Vector(self.users))
        
        if self.boost_peer is not None:
            b.write(self.boost_peer.write())
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()
