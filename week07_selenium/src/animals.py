
class Animal:
    def __init__(self, species: str) -> None:
        self.species = species

    def speak(self) -> str:
        return 'some sound'

    def info(self) -> str:
        return f'This is a {self.species}'

class Cat(Animal):
    def __init__(self) -> None:
        super().__init__('cat')

    def speak(self) -> str:
        return 'Meow'


class Dog(Animal):
    def __init__(self) -> None:
        super().__init__('dog')

    def speak(self) -> str:
        return 'Woof'

    def fetch(self) -> None:
        print('Dog fetches the ball')
