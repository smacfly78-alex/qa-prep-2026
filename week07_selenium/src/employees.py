class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def get_bonus(self) -> float:
        """Base bonus is 5% of salary."""
        return self.salary * 0.05

    def describe(self) -> str:
        """Returns description with role and bonus."""
        return f"{self.name} ({self.get_role()}): salary ${self.salary:.2f}, bonus ${self.get_bonus():.2f}"

    def get_role(self) -> str:
        """Override in subclasses."""
        return "employee"


class Manager(Employee):
    def get_role(self) -> str:
        return 'manager'

    def get_bonus(self) -> float:
        return self.salary * 0.15


class Intern(Employee):
    def get_role(self) -> str:
        return 'intern'

    def get_bonus(self) -> float:
        return 0


if __name__ == '__main__':
    emp = Employee("Igor", 50000)
    mgr = Manager("Anna", 80000)
    intern = Intern("Petr", 20000)

    print(emp.describe())
    # Igor (employee): salary $50000.00, bonus $2500.00

    print(mgr.describe())
    # Anna (manager): salary $80000.00, bonus $12000.00

    print(intern.describe())
    # Petr (intern): salary $20000.00, bonus $0.00