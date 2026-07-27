
class User:
    def __init__(self, name: str, email: str, is_active: bool = True) -> None:
        self.name = name
        self.email = email
        self.is_active = is_active

    def deactivate(self) -> None:
        self.is_active = False

    def send_email(self) -> None:
        print(f'Отправлено письмо на {self.email}')

    def __str__(self) -> str:
        return f'User: {self.name} (active={self.is_active})'

