from typing import List, Optional

from pydantic import BaseModel


class ChargeBase(BaseModel):
    pass


class ChargeCreate(ChargeBase):
    pass


class Charge(ChargeBase):
    charge_card_id: str
    charge_id: str
    amount: int

    class Config:
        orm_mode = True

class CardBase(BaseModel):
    pass


class CardCreate(CardBase):
    pass


class Card(CardBase):
    card_id: str
    limit: int
    available_balance: int

    class Config:
        orm_mode = True