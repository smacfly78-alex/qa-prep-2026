class Animal:
    species: str = "unknown"

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return '...'

    def info(self) -> str:
        return f'{self.name} is a {self.species}'


class Cat(Animal):
    species = "cat"

    def speak(self) -> str:
        return 'Meow'


class Dog(Animal):
    species = "dog"

    def speak(self) -> str:
        return 'Woof'

    def fetch(self) -> str:
        return f"{self.name} fetched the ball"


if __name__ == '__main__':
    cat = Cat("Barsik")
    print(cat.speak())  # Meow
    print(cat.info())  # Barsik is a cat

    dog = Dog("Rex")
    print(dog.speak())  # Woof
    print(dog.info())  # Rex is a dog
    print(dog.fetch())  # Rex fetched the ball

    # Проверяем, что у Cat нет fetch
    try:
        cat.fetch()
    except AttributeError as e:
        print(f"Cat cannot fetch: {e}")