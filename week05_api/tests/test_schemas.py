from week05_api.src.schemas import ORDER_SCHEMA
from jsonschema import validate


def test_valid_order_passes_schema():
    """Valid order data should pass ORDER_SCHEMA validation."""
    order = {
        "id": 1,
        "status": "active",
        "customer": {
            "id": 42,
            "name": "Igor",
            "email": "i@x.com"
        },
        "items": [
            {"product_id": 100, "quantity": 2},
            {"product_id": 200, "quantity": 1}
        ],
        "total": 150.50
    }

    validate(instance=order, schema=ORDER_SCHEMA)

import pytest
from jsonschema import ValidationError


@pytest.mark.parametrize("bad_order,error_hint", [
    # Кейс 1 — статус вне enum
    (
        {"id": 1, "status": "unknown", "customer": {"id": 42,"name": "Igor","email": "i@x.com"}, "items": [{"product_id": 100, "quantity": 2},
            {"product_id": 200, "quantity": 1}], "total": 100.0},
        "status"
    ),
    # Кейс 2 — customer без email
    (
        {"id": 1, "status": "active", "customer": {"id": 42, "name": "Igor"}, "items": [{"product_id": 100, "quantity": 2},
            {"product_id": 200, "quantity": 1}], "total": 100.0},
        "email"
    ),
    # Кейс 3 — item без quantity
    (
        {"id": 1, "status": "active", "customer": {"id": 42,"name": "Igor","email": "i@x.com"}, "items": [{"product_id": 100}], "total": 100.0},
        "quantity"
    ),
])
def test_invalid_order_fails_schema(bad_order, error_hint):
    with pytest.raises(ValidationError):
        validate(instance=bad_order, schema=ORDER_SCHEMA)