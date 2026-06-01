
class Cat:
    def __init__(self, name: str, age: int, breed: str) -> None:
        self.name = name
        self.age = age
        self.breed = breed

class BankAccount:
    def __init__(self, owner: str, balance: int = 0) -> None:
        self.owner = owner
        self.balance = balance

class Book:
    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = False


if __name__ == '__main__':
    b1 = Book("1984", "Orwell", 328)
    b2 = Book("Sapiens", "Harari", 443)

    print(b1.title)  # "1984"
    print(b1.is_read)  # False  ← по умолчанию
    print(b2.is_read)  # False

    # Можно изменить вручную после создания
    b1.is_read = True
    print(b1.is_read)  # True


    # acc1 = BankAccount("Igor", 1000)
    # acc2 = BankAccount("Anna")  # без баланса — должно быть 0
    #
    # print(acc1.owner)  # "Igor"
    # print(acc1.balance)  # 1000
    # print(acc2.owner)  # "Anna"
    # print(acc2.balance)  # 0


    # cat1 = Cat("Барсик", 3, "сибирская")
    # cat2 = Cat("Мурка", 5, "перс")
    #
    # print(cat1.name)  # "Барсик"
    # print(cat1.age)  # 3
    # print(cat1.breed)  # "сибирская"
    # print(cat2.breed)  # "перс"