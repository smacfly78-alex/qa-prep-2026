
class DBConnection:
    def __init__(self, db_name):
        self.db_name = db_name


    def execute(self, sql):
        print(f'Executing: {sql}')


    def __enter__(self) -> 'DBConnection':
        print(f'Connected to {self.db_name}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        print('Connection closed')


if __name__ == '__main__':
    with DBConnection("shop.db") as db:
        db.execute("SELECT * FROM users")
        db.execute("SELECT * FROM orders")

    # Connected to shop.db
    # Executing: SELECT * FROM users
    # Executing: SELECT * FROM orders
    # Connection closed

    # Работа при исключении
    try:
        with DBConnection("shop.db") as db:
            db.execute("SELECT * FROM users")
            raise ValueError("Query error!")
    except ValueError:
        pass

    # Connected to shop.db
    # Executing: SELECT * FROM users
    # Connection closed              ← connection закрыт ДО пробрасывания