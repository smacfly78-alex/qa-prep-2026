class BaseTest:
    def setup(self) -> str:
        return 'BaseTest: setup'

class DatabaseMixin:
    def prepare(self) -> str:
        return 'Database prepared'

    def cleanup_db(self) -> str:
        return 'Database cleaned'

class ApiMixin:
    def prepare(self) -> str:
        return 'API client prepared'

    def send_request(self, url: str) -> str:
        return f'GET {url}'

class IntegrationTest(BaseTest, DatabaseMixin, ApiMixin):
    def run(self) -> None:
        print(self.setup())
        print(self.prepare())
        print(ApiMixin.prepare(self))
        print(self.send_request("/users"))
        print(self.cleanup_db())

if __name__ == '__main__':
    test = IntegrationTest()
    test.run()

    # Должно вывести:
    # BaseTest: setup
    # Database prepared          ← prepare из DatabaseMixin (он раньше в стопке)
    # API client prepared        ← явный вызов ApiMixin.prepare
    # GET /users
    # Database cleaned