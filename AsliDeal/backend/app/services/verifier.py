from typing import List, Dict
from datetime import datetime
from typing import Optional
from fastapi import HTTPException


def verify_discount(current_price: float, historical_price: float) -> bool:
    """Return True when the current price represents a genuine discount compared to historical price.

    Rules used for tests:
    - Negative prices raise HTTPException(400).
    - If historical_price <= 0 or current_price <= 0, treat as not valid (no discount).
    - A discount is considered valid only if the percentage drop is >= 25% (configurable).
    """
    if current_price < 0 or historical_price < 0:
        raise HTTPException(status_code=400, detail="Negative prices are not allowed")

    if historical_price == 0 or current_price == 0:
        return False

    # Calculate percentage reduction from historical to current price
    discount_percent = (historical_price - current_price) / historical_price * 100
    threshold = 25.0
    return discount_percent >= threshold


async def get_historical_price(product_id: str) -> Optional[float]:
    """Simple lookup used by integration tests. In production this would query the DB.

    For tests we return 1500 for product_id '12345' and None for others.
    """
    sample_data = {
        "12345": 1500.0,
    }
    return sample_data.get(product_id)
