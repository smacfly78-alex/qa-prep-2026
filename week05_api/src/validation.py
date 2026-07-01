
REQUIRED_FIELDS = ["id", "name", "email", "age"]

def validate_user_data(data: dict) -> list[str]:
    return [field for field in REQUIRED_FIELDS if field not in data]

if __name__ == '__main__':
    print(validate_user_data({"id": 1, "name": "Igor", "email": "i@x.com", "age": 30}))
    # []

    print(validate_user_data({"id": 1, "name": "Igor"}))
    # ['email', 'age']

    print(validate_user_data({}))
    # ['id', 'name', 'email', 'age']

    print(validate_user_data({"id": 1, "name": "Igor", "email": None, "age": 30}))
    # []  ← email присутствует (хоть и None), всё валидно