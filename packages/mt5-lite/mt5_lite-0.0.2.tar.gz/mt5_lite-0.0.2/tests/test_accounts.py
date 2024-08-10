import pytest
import random
from faker import Faker

from .context import Account

faker = Faker()


@pytest.fixture
def account_data() -> dict:
    return {
        "account_number": random.randint(10000000, 99999999),
        "password": faker.password(),
        "server": faker.name().title().replace(" ", "_"),
    }


@pytest.fixture
def account() -> Account:
    return Account("4234234232", 'testpassword', 'Deriv_Demo')


class TestAccount:
    def test_account_number(self, account: Account):
        account_number = account.account_number
        assert isinstance(account_number, int)
        assert account_number == 4234234232

    def test_password(self, account: Account):
        password = account.password
        assert isinstance(password, str)
        assert password == "testpassword"

    def test_server(self, account: Account):
        server = account.server
        assert isinstance(server, str)
        assert server == "Deriv_Demo"

    def test_to_data_method(self, account: Account):
        data = account.to_data()
        assert isinstance(data, dict)
        assert data['account_number'] == account.account_number
        assert data['password'] == account.password
        assert data['server'] == account.server

    def test_from_data_classmethod(self, account: Account):
        data = account.to_data()
        new_account = Account.from_data(data)
        assert isinstance(new_account, Account)
        assert new_account.account_number == account.account_number
        assert new_account.password == account.password
        assert new_account.server == account.server
        assert new_account == account

    def test_eq_method(self, account: Account, account_data: dict):
        new_account = Account(**account_data)
        assert new_account != account
