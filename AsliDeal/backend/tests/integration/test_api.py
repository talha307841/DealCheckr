from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_verify_discount_valid():
    response = client.post("/api/v1/verify/", json={"product_id": "12345", "current_price": 1000})
    assert response.status_code == 200
    assert response.json() == {"valid": True, "message": "Discount is valid."}

def test_verify_discount_invalid():
    response = client.post("/api/v1/verify/", json={"product_id": "12345", "current_price": 2000})
    assert response.status_code == 200
    assert response.json() == {"valid": False, "message": "Discount is invalid."}

def test_verify_discount_not_found():
    response = client.post("/api/v1/verify/", json={"product_id": "nonexistent", "current_price": 1000})
    assert response.status_code == 404
    assert response.json() == {"detail": "Product not found."}