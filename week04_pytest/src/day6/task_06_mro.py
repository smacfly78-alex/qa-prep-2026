class Living:
    def describe(self) -> str:
        return "I am living"


class Walker:
    def describe(self) -> str:
        return "I walk"


class Talker:
    def describe(self) -> str:
        return "I talk"


# Создайте класс Worker, наследующий Living, Walker, Talker
# Без переопределения describe()
class Worker(Walker, Living, Talker):
    def __init__(self):
        pass


w = Worker()
print(w.describe())