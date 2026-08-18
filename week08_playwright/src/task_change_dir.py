import os

class ChangeDir:
    def __init__(self, target_path: str) -> None:
        self.target_path = target_path
        self.current_path = os.getcwd()

    def __enter__(self):
        self.saved_path = self.current_path
        self.current_path = os.chdir(self.target_path)


    def __exit__(self, exc_type, exc_val, exc_tb):
        self.current_path = os.chdir(self.saved_path)

if __name__ == '__main__':

    # Текущая директория, например: /Users/aleksei/qa-prep-2026
    print(f"Before: {os.getcwd()}")

    with ChangeDir("/tmp"):
        print(f"Inside: {os.getcwd()}")
        # /tmp

    print(f"After: {os.getcwd()}")
    # /Users/aleksei/qa-prep-2026 (вернулось)

    # Работа при исключении — восстанавливает всё равно
    try:
        with ChangeDir("/tmp"):
            print(f"Inside: {os.getcwd()}")
            raise ValueError("Boom")
    except ValueError:
        pass

    print(f"After error: {os.getcwd()}")
    # /Users/aleksei/qa-prep-2026 (вернулось даже после исключения!)