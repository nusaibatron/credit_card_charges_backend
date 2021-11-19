from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Card1(Base):
    __tablename__ = "cards"

    card_id = Column(String, primary_key=True, index=True)
    limit = Column(Integer, unique=False, index=True)
    available_balance = Column(Integer, unique=False, index=True)

    charges = relationship("Charge1", back_populates="card")


class Charge1(Base):
    __tablename__ = "charges"

    charge_id = Column(String, primary_key=True, index=True)
    charge_amount = Column(Integer, unique=False, index=True)
    charge_card_id = Column(Integer, ForeignKey("cards.card_id"))

    card = relationship("Card1", back_populates="charges")