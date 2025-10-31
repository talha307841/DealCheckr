from fastapi import APIRouter, HTTPException
from typing import List
from ..schemas.offer import OfferCreate, OfferResponse
from ..models.offer import Offer
from ..db.session import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/", response_model=OfferResponse)
def create_offer(offer: OfferCreate, db: Session = next(get_db())):
    db_offer = Offer(**offer.dict())
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer

@router.get("/", response_model=List[OfferResponse])
def read_offers(skip: int = 0, limit: int = 10, db: Session = next(get_db())):
    offers = db.query(Offer).offset(skip).limit(limit).all()
    return offers

@router.get("/{offer_id}", response_model=OfferResponse)
def read_offer(offer_id: int, db: Session = next(get_db())):
    offer = db.query(Offer).filter(Offer.id == offer_id).first()
    if offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer

@router.put("/{offer_id}", response_model=OfferResponse)
def update_offer(offer_id: int, offer: OfferCreate, db: Session = next(get_db())):
    db_offer = db.query(Offer).filter(Offer.id == offer_id).first()
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    for key, value in offer.dict().items():
        setattr(db_offer, key, value)
    db.commit()
    db.refresh(db_offer)
    return db_offer

@router.delete("/{offer_id}", response_model=OfferResponse)
def delete_offer(offer_id: int, db: Session = next(get_db())):
    db_offer = db.query(Offer).filter(Offer.id == offer_id).first()
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Offer not found")
    db.delete(db_offer)
    db.commit()
    return db_offer