from pydantic import BaseModel
from typing import List, Optional

class OfferBase(BaseModel):
    title: str
    description: str
    original_price: float
    discounted_price: float
    url: str

class OfferCreate(OfferBase):
    pass

class Offer(OfferBase):
    id: int

    class Config:
        orm_mode = True

class OfferResponse(BaseModel):
    offers: List[Offer]
    total: int

class OfferVerificationResponse(BaseModel):
    is_valid: bool
    message: str
    offer: Optional[Offer]