
class User:
    def __init__(self, name: str, email: str, is_active: bool = True) -> None:
        self.name = name
        self.email = email
        self.is_active = is_active

    def deactivate(self) -> None:
        self.is_active = False

    def send_email(self, subject: str) -> str:
        if self.is_active:
            return f'Sent to {self.email}: {subject}'
        return 'User inactive, email not sent'


    def __str__(self) -> str:
        return f'User: {self.name} (active={self.is_active})'


if __name__ == '__main__':
    user = User("Igor", "i@x.com")
    print(user)  # User: Igor (active=True)
    print(user.send_email("Hello"))  # Sent to i@x.com: Hello

    user.deactivate()
    print(user)  # User: Igor (active=False)
    print(user.send_email("Hi"))  # User inactive, email not sent