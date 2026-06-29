
def safe_divide(a: int, b: int) -> float | None:
    try:
        result = a / b
    except ZeroDivisionError:
        print('Cannot divide by zero')
    else:
        print(f'Division successful: {result}')
        return result
    finally:
        print('Done')

class InsufficientFundsError(Exception):
    pass

def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFundsError(f'Not enough funds: balance={balance}, requested={amount}')
    elif amount <= 0:
        raise ValueError("Amount must be positive")
    else:
        return balance-amount

class UserDataError(Exception):
    pass

def parse_user_age(text: str) -> int:
    try:
        result = int(text)
    except ValueError as v:
        raise UserDataError("Invalid age input") from v
    else:
        if result < 0 or result > 150:
            raise UserDataError("Age out of range")
        return result


if __name__ == '__main__':
    print(parse_user_age("25"))
    # 25

    try:
        parse_user_age("not a number")
    except UserDataError as e:
        print(f"Error: {e}")
        print(f"Original cause: {e.__cause__}")
    # Error: Invalid age input
    # Original cause: invalid literal for int() with base 10: 'not a number'

    try:
        parse_user_age("200")
    except UserDataError as e:
        print(f"Error: {e}")
        print(f"Original cause: {e.__cause__}")
    # Error: Age out of range
    # Original cause: None


    new_balance = withdraw(100.0, 30.0)
    print(new_balance)
    # 70.0

    try:
        withdraw(100.0, 200.0)
    except InsufficientFundsError as e:
        print(f"Error: {e}")
    # Error: Not enough funds: balance=100.0, requested=200.0

    try:
        withdraw(100.0, -10.0)
    except ValueError as e:
        print(f"Error: {e}")
    # Error: Amount must be positive


    print(safe_divide(10, 2))
    # Division successful: 5.0
    # Done
    # 5.0

    print(safe_divide(10, 0))
    # Cannot divide by zero
    # Done
    # 0.0