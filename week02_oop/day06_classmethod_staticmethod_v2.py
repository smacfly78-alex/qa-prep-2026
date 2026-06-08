
class Account:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if value >= 0:
            self._balance = value
        else:
            raise ValueError('Error')

    def deposit(self, amount: float) -> None:
        self.balance = self.balance + amount

    def __repr__(self) -> str:
        return f'Account(owner="{self.owner}", balance={self.balance})'

    @classmethod
    def from_dict(cls, data: dict) -> "Account":
        owner = data["owner"]
        balance = data.get("balance", 0.0)
        return cls(owner, balance)

class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float, interest_rate: float) -> None:
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        interest = self.balance * self.interest_rate
        self.deposit(interest)

    def __repr__(self) -> str:
        return f'{super().__repr__()}, rate={self.interest_rate}'


if __name__ == '__main__':
    acc = Account("Igor", 1000.0)
    print(acc)  # Account(owner='Igor', balance=1000.0)

    acc.deposit(500)
    print(acc.balance)  # 1500.0

    # Альтернативный конструктор
    acc2 = Account.from_dict({"owner": "Anna", "balance": 2000.0})
    print(acc2)  # Account(owner='Anna', balance=2000.0)

    acc3 = Account.from_dict({"owner": "Empty"})  # без balance
    print(acc3.balance)  # 0.0

    # Валидация баланса
    try:
        acc.balance = -100
    except ValueError as e:
        print(f"Error: {e}")  # Error: Balance cannot be negative

    # Сберегательный
    sav = SavingsAccount("Dmitry", 10000.0, 0.05)
    print(sav)  # Account(owner='Dmitry', balance=10000.0), rate=0.05
    sav.apply_interest()
    print(sav.balance)  # 10500.0