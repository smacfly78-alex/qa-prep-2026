
class Product:
    _total_count: int = 0
    def __init__(self, name: str, price: float, category: str) -> None:
        self.name = name
        self.price = price
        self.category = category
        Product._total_count += 1

    def __repr__(self) -> str:
        return f'Product(name="{self.name}", price={self.price}, category="{self.category}")'

    @classmethod
    def from_csv_row(cls, row: str) -> "Product":
        name, price, category = row.split(',')
        return cls(name, float(price), category)

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(data['name'], data['price'], data['category'])

    @classmethod
    def free_sample(cls, name: str, category: str) -> "Product":
        return cls(name=name, price=0.0, category=category)

    @classmethod
    def total_created(cls) -> int:
        return cls._total_count

    @staticmethod
    def is_valid_price(price: float) -> bool:
        return 0 <= price <= 10000

class Task:
    _next_id: int = 1
    _registry: dict[int, "Task"] = {}

    def __init__(self, title: str) -> None:
        self.task_id = Task._next_id
        Task._next_id += 1
        self.title = title
        self.is_done = False
        Task._registry[self.task_id] =  self

    def __repr__(self) -> str:
        return f'Task(id={self.task_id}, title="{self.title}", done={self.is_done})'

    def mark_done(self) -> None:
        self.is_done = True

    @classmethod
    def find_by_id(cls, task_id: int) -> "Task | None":
        return cls._registry.get(task_id)

    @classmethod
    def get_all_done(cls) -> list["Task"]:
        list_done =[]
        for task in cls._registry.values():
            if task.is_done:
                list_done.append(task)
        return list_done

    @classmethod
    def count_total(cls) -> int:
        return len(cls._registry)

    @staticmethod
    def is_valid_title(title: str) -> bool:
        return title.strip() != "" and len(title.strip()) <= 100




if __name__ == '__main__':
    t1 = Task("Buy bread")
    t2 = Task("Walk the dog")
    t3 = Task("Read book")

    print(t1)  # Task(id=1, title='Buy bread', done=False)
    print(t2)  # Task(id=2, title='Walk the dog', done=False)
    print(t3)  # Task(id=3, title='Read book', done=False)

    # Помечаем некоторые как выполненные
    t1.mark_done()
    t3.mark_done()

    # Поиск по ID
    found = Task.find_by_id(2)
    print(found)  # Task(id=2, title='Walk the dog', done=False)

    not_found = Task.find_by_id(999)
    print(not_found)  # None

    # Получаем выполненные
    done_tasks = Task.get_all_done()
    print(done_tasks)  # [Task(id=1, ...), Task(id=3, ...)]
    print(len(done_tasks))  # 2

    # Общее число
    print(Task.count_total())  # 3

    # Валидация title
    print(Task.is_valid_title("Normal title"))  # True
    print(Task.is_valid_title(""))  # False
    print(Task.is_valid_title("   "))  # False (пустая после strip)
    print(Task.is_valid_title("x" * 150))  # False (слишком длинная)


    p1 = Product("Apple", 99.99, "fruits")
    p2 = Product.from_csv_row("Banana,49.99,fruits")
    p3 = Product.from_dict({"name": "Bread", "price": 35.00, "category": "bakery"})
    p4 = Product.free_sample("Cheese sample", "dairy")

    print(p1)  # Product(name='Apple', price=99.99, category='fruits')
    print(p2)  # Product(name='Banana', price=49.99, category='fruits')
    print(p3)  # Product(name='Bread', price=35.0, category='bakery')
    print(p4)  # Product(name='Cheese sample', price=0.0, category='dairy')

    print(Product.total_created())  # 4

    print(Product.is_valid_price(50))  # True
    print(Product.is_valid_price(-10))  # False
    print(Product.is_valid_price(20000))  # False