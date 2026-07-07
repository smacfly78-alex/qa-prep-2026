import pytest
from jsonschema import validate, ValidationError
from src.schemas import PRODUCT_SCHEMA

def test_valid_product_passes_schema():
    data = {
        "id": 1,
        "name": "Laptop Pro",
        "price": 1299.99,
        "in_stock": True,
        "category": {
            "id": 5,
            "name": "Electronics",
            "path": ["Root", "Devices", "Computers"]
        },
        "tags": ["portable", "premium"]
    }

    validate(instance=data, schema=PRODUCT_SCHEMA)

@pytest.mark.parametrize('data', [{
        "id": 1,
        "name": "Laptop Pro",
        "price": -10,
        "in_stock": True,
        "category": {
            "id": 5,
            "name": "Electronics",
            "path": ["Root", "Devices", "Computers"]
        },
        "tags": ["portable", "premium"]
    }, {
        "id": 1,
        "name": "",
        "price": 1299.99,
        "in_stock": True,
        "category": {
            "id": 5,
            "name": "Electronics",
            "path": ["Root", "Devices", "Computers"]
        },
        "tags": ["portable", "premium"]
    }, {
        "id": 1,
        "name": "Laptop Pro",
        "price": 1299.99,
        "in_stock": True,
        "category": {
            "id": 5,
            "name": "Electronics",
            "path": []
        },
        "tags": ["portable", "premium"]
    }])
def test_invalid_product_fails_schema(data):
    with pytest.raises(ValidationError):
        validate(instance=data, schema=PRODUCT_SCHEMA)