from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
from app.services.verifier import verify_discount
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
from app.services import verifier

router = APIRouter()


class VerifyRequest(BaseModel):
    product_id: str
    current_price: float


@router.post("/")
async def verify_discount_offer(request: VerifyRequest):
    # Lookup historical price (stubbed for tests)
    historical_price = await verifier.get_historical_price(request.product_id)

    if historical_price is None:
        raise HTTPException(status_code=404, detail="Product not found.")

    try:
        is_valid = verifier.verify_discount(request.current_price, historical_price)
    except HTTPException:
        # re-raise to surface proper status
        raise

    return {
        "valid": bool(is_valid),
        "message": "Discount is valid." if is_valid else "Discount is invalid.",
    }
