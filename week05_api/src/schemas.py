
POST_SCHEMA = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

ORDER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "status": {"type": "string", "enum": ["active", "cancelled", "completed"]},
        "customer": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "email": {"type": "string"}
            },
            "required": ["id", "name", "email"]
        },
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "product_id": {"type": "integer"},
                    "quantity": {"type": "integer"}
                },
                "required": ["product_id", "quantity"]
            },
        },
        "total": {"type": "number"}
    },
    "required": ["id", "status", "customer", "items", "total"]
}

PRODUCT_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 1, "maxLength": 100},
        "price": {"type": "number", "minimum": 0},
        "in_stock": {"type": "boolean"},
        "category": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "path": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 1
                },
            },
            "required": ["id", "name", "path"]
        },
        "tags": {
            "type": "array",
            "items": {"type": "string"}
        },
    },
    "required": ["id", "name", "price", "in_stock", "category", "tags"]
}