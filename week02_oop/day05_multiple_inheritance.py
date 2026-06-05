
class AuthMixin:
    def login_as_admin(self) -> str:
        return 'Logged in as admin'

    def login_as_user(self, name: str) -> str:
        return f'Logged in as user {name}'

class AssertionMixin:
    def assert_status_code(self, status: int, expected: int) -> bool:
        return status == expected

    def assert_not_empty(self, value: str) -> bool:
        return value != ""

class BaseTest:
    def setup(self) -> str:
        return 'BaseTest: setup done'

    def teardown(self) -> str:
        return 'BaseTest: teardown done'


class LoginApiTest(BaseTest, AuthMixin, AssertionMixin):
    def test_admin_login(self) -> bool:
        print(self.setup())
        print(self.login_as_admin())
        result = self.assert_status_code(200, 200)
        print(self.teardown())
        return result



if __name__ == "__main__":
    test = LoginApiTest()
    print(test.test_admin_login())
