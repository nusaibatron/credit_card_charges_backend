from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

db_cards = []
db_charges = []

class Card(BaseModel):
    card_id: str
    limit: int
    available_balance: int

class Charge(BaseModel):
    charge_card_id: str
    charge_id: str
    amount: int

@app.get("/")
def index():
    return {"key": "val"}

@app.get("/cards")
def get_cards():
    return db_cards

@app.post("/cards")
def create_card(card: Card):
    db_cards.append(card.dict())
    return db_cards[-1]

@app.get("/charges")
def get_charges():
    return db_charges

@app.post("/charges")
def create_charge(charge: Charge):
    db_charges.append(charge.dict())
    return db_charges[-1]




