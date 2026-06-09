# === Задача 1 ===
from abc import ABC, abstractmethod


class Cart:
    total_carts: int = 0

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.items_count = 0
        Cart.total_carts += 1

    def add_item(self) -> None:
        self.items_count +=1

    @classmethod
    def get_total_carts(cls) -> int:
        return cls.total_carts

# === Задача 2 ===

class BaseReporter(ABC):
    @abstractmethod
    def report(self, test_name: str, status: str) -> str:
        pass


class ConsoleReporter(BaseReporter):
    def report(self, test_name: str, status: str) -> str:
        return f'[CONSOLE] {test_name}: {status}'

class SlackReporter(BaseReporter):
    def report(self, test_name: str, status: str) -> str:
        return f'💬 Slack notification → Test "{test_name}" finished with status: {status}'

class HtmlReporter(BaseReporter):
    def report(self, test_name: str, status: str) -> str:
        return f"<div class='test'>{test_name}: <span>{status}</span></div>"


def run_test_and_report(test_name: str, status: str, reporters: list[BaseReporter]) -> None:
    """Запускает тест и отправляет результат во все репортёры."""
    print(f"Running test: {test_name}")
    for reporter in reporters:
        result = reporter.report(test_name, status)
        print(result)


# === Задача 3 ===

class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    @property
    def salary(self) -> float:
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if value < 0:
            raise ValueError("Salary cannot be negative")
        if value > 1_000_000:
            raise ValueError("Salary unrealistic")
        self._salary = value

    def raise_salary(self, amount: float) -> None:
        self.salary = self.salary + amount

    def __repr__(self) -> str:
        return f"Employee(name='{self.name}', salary={self.salary})"


class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int) -> None:
        super().__init__(name, salary)
        self.team_size = team_size

    def apply_bonus(self) -> None:
        bonus = self.salary * 0.1 * self.team_size
        self.raise_salary(bonus)

    def __repr__(self) -> str:
        return f"{super().__repr__()}, team_size={self.team_size}"


# === Задача 4 ===

class Library:
    _total_libraries: int = 0

    def __init__(self, name: str, books: list[str] = None) -> None:
        if books is None:
            books =[]
        self.name = name
        self.books = list(books)
        Library._total_libraries += 1

    def add_book(self, title: str) -> None:
        self.books.append(title)

    @property
    def book_count(self) -> int:
        return len(self.books)

    @classmethod
    def get_total_libraries(cls) -> int:
        return cls._total_libraries

    def __repr__(self) -> str:
        return f'Library(name="{self.name}", books={self.book_count})'


# === Задача 5 ===

class Order(ABC):
    _next_id: int = 1
    _registry: dict[int, "Order"] = {}

    def __init__(self, customer:str, amount: float) -> None:
        self.order_id = Order._next_id
        Order._next_id += 1
        Order._registry[self.order_id] = self
        self.customer = customer
        self.amount = amount

    @property
    def amount(self) -> float:
        return self._amount

    @amount.setter
    def amount(self, value) -> None:
        if value < 0:
            raise ValueError('Amount cannot be negative')
        self._amount = value

    @abstractmethod
    def process(self) -> str:
        pass

    @classmethod
    def find_by_id(cls, order_id: int) -> "Order | None":
        return cls._registry.get(order_id)


    def __repr__(self) -> str:
        return f"Order(id={self.order_id}, customer='{self.customer}', amount={self.amount})"


class OnlineOrder(Order):
    def __init__(self, customer:str, amount: float, delivery_address: str) -> None:
        super().__init__(customer, amount)
        self.delivery_address = delivery_address

    def process(self) -> str:
        return f"Online order #{self.order_id} → shipping to {self.delivery_address}"

    @classmethod
    def from_dict(cls, data: dict) -> "OnlineOrder":
        return cls(data["customer"], data["amount"], data["delivery_address"])

    def __repr__(self) -> str:
        return f"{super().__repr__()}, address={self.delivery_address}"


class PickupOrder(Order):
    def __init__(self, customer:str, amount: float, pickup_location: str) -> None:
        super().__init__(customer, amount)
        self.pickup_location = pickup_location

    def process(self) -> str:
        return f"Pickup order #{self.order_id} → ready at {self.pickup_location}"

    @staticmethod
    def is_valid_location(location: str) -> bool:
        return location.strip() != "" and len(location.strip()) <= 200


def process_all_orders(orders: list[Order]) -> None:
    """Обрабатывает все заказы — работает с любым подтипом через общий метод process()."""
    print(f"Processing {len(orders)} orders:")
    for order in orders:
        result = order.process()
        print(f"  {result}")



if __name__ == "__main__":
    # Создание через конструкторы
    o1 = OnlineOrder("Igor", 100.0, "Moscow, Lenin st. 5")
    o2 = PickupOrder("Anna", 250.0, "Store #42")
    o3 = OnlineOrder.from_dict({
        "customer": "Dmitry",
        "amount": 500.0,
        "delivery_address": "Tashkent, Mirzo Ulug'bek st. 100"
    })

    print(o1)
    print(o2)
    print(o3)

    # Полиморфизм — функция работает с разными типами
    process_all_orders([o1, o2, o3])

    # Поиск в реестре — через базовый класс
    found = Order.find_by_id(2)
    print(found)

    # Валидация при создании
    try:
        bad = OnlineOrder("Bad", -100, "addr")
    except ValueError as e:
        print(f"Error: {e}")

    # Попытка создать абстрактный класс
    try:
        abstract = Order("Test", 100)
    except TypeError as e:
        print(f"Error: {e}")

    # Статическая утилита
    print(PickupOrder.is_valid_location("Store #1"))  # True
    print(PickupOrder.is_valid_location(""))  # False
    print(PickupOrder.is_valid_location("   "))  # False



    # Подготовка исходного списка
    initial_books = ["1984", "Animal Farm"]

    # Создаём две библиотеки с одним и тем же списком
    lib1 = Library("Central", initial_books)
    lib2 = Library("Branch", initial_books)

    # Добавляем книгу в lib1
    lib1.add_book("Brave New World")

    # Что выведут?
    print(lib1.book_count)  # ?
    print(lib2.book_count)  # ?
    print(len(initial_books))  # ?

    # Создаём третью библиотеку без передачи списка
    lib3 = Library("Empty")
    lib3.add_book("New Book")

    print(lib3.book_count)  # ?
    print(Library.get_total_libraries())  # ?


    # Создание с валидным значением
    emp = Employee("Igor", 50000.0)
    print(emp)  # Employee(name='Igor', salary=50000.0)

    # Повышение через метод
    emp.raise_salary(10000)
    print(emp.salary)  # 60000.0

    # Валидация при создании
    try:
        bad = Employee("Bad", -100)
    except ValueError as e:
        print(f"Error: {e}")  # Error: Salary cannot be negative

    try:
        unrealistic = Employee("Rich", 5_000_000)
    except ValueError as e:
        print(f"Error: {e}")  # Error: Salary unrealistic

    # Менеджер
    mgr = Manager("Anna", 80000.0, 5)
    print(mgr)  # Employee(name='Anna', salary=80000.0), team_size=5

    # Бонус применяется через родительский raise_salary → автоматически валидируется
    mgr.apply_bonus()  # 80000 + 80000 * 0.5 = 120000
    print(mgr.salary)  # 120000.0

    # Создание менеджера с невалидной зарплатой — должна сработать ТА ЖЕ валидация из Employee
    try:
        bad_mgr = Manager("Bad Boss", -500, 3)
    except ValueError as e:
        print(f"Error: {e}")  # Error: Salary cannot be negative



    #Создаём три разных репортёра
    console = ConsoleReporter()
    slack = SlackReporter()
    html = HtmlReporter()

    # Запускаем тест с отправкой во все три
    run_test_and_report(
        test_name="test_login",
        status="PASSED",
        reporters=[console, slack, html]
    )


    # Должно вывести:
    # Running test: test_login
    # [CONSOLE] test_login: PASSED
    # 💬 Slack notification → Test 'test_login' finished with status: PASSED
    # <div class='test'>test_login: <span>PASSED</span></div>

    # Бонус — добавляем новый репортёр без изменения функции
    class FileReporter(BaseReporter):
        def report(self, test_name: str, status: str) -> str:
            return f"FILE LOG: [{test_name}] => {status}"


    file_reporter = FileReporter()

    # run_test_and_report работает с новым типом БЕЗ ИЗМЕНЕНИЙ
    run_test_and_report(
        test_name="test_logout",
        status="FAILED",
        reporters=[console, file_reporter]
    )

    c1 = Cart("Igor")
    c1.add_item()
    c1.add_item()
    c1.add_item()

    c2 = Cart("Anna")
    c2.add_item()

    c3 = Cart("Dmitry")

    print(c1.items_count)  # 3
    print(c2.items_count)  # 1
    print(c3.items_count)  # 0
    print(Cart.get_total_carts())  # 3

    print(Cart.total_carts)  # ? Подумайте перед запуском