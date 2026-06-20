class User:
    def __init__(self, name: str, email: str, age: int) -> None:
        self.name = name
        self.email = email
        self.age = age

    def is_adult(self) -> bool:
        return self.age >= 18

    def is_valid_email(self) -> bool:
        return "@" in self.email and "." in self.email