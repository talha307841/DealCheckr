from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from ..db.session import get_db
from ..models.offer import Offer
from ..schemas.offer import OfferCreate, OfferUpdate

def get_offer(offer_id: int, db: Session = Depends(get_db)) -> Offer:
    offer = db.query(Offer).filter(Offer.id == offer_id).first()
    if not offer:
        raise HTTPException(status_code=404, detail="Offer not found")
    return offer

def create_offer(offer: OfferCreate, db: Session = Depends(get_db)) -> Offer:
    new_offer = Offer(**offer.dict())
    db.add(new_offer)
    db.commit()
    db.refresh(new_offer)
    return new_offer

def update_offer(offer_id: int, offer: OfferUpdate, db: Session = Depends(get_db)) -> Offer:
    existing_offer = get_offer(offer_id, db)
    for key, value in offer.dict(exclude_unset=True).items():
        setattr(existing_offer, key, value)
    db.commit()
    return existing_offer

def delete_offer(offer_id: int, db: Session = Depends(get_db)) -> None:
    existing_offer = get_offer(offer_id, db)
    db.delete(existing_offer)
    db.commit()