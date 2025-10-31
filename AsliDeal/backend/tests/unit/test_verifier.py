from fastapi import HTTPException
from app.services.verifier import verify_discount

def test_verify_discount_valid():
    # Test with a valid discount
    current_price = 100
    historical_price = 150
    result = verify_discount(current_price, historical_price)
    assert result is True

def test_verify_discount_invalid():
    # Test with an invalid discount
    current_price = 100
    historical_price = 120
    result = verify_discount(current_price, historical_price)
    assert result is False

def test_verify_discount_edge_case():
    # Test with edge case where prices are equal
    current_price = 100
    historical_price = 100
    result = verify_discount(current_price, historical_price)
    assert result is False

def test_verify_discount_negative_prices():
    # Test with negative prices
    current_price = -100
    historical_price = -150
    try:
        result = verify_discount(current_price, historical_price)
    except HTTPException as e:
        assert e.status_code == 400  # Expecting a bad request for negative prices

def test_verify_discount_zero_prices():
    # Test with zero prices
    current_price = 0
    historical_price = 0
    result = verify_discount(current_price, historical_price)
    assert result is False