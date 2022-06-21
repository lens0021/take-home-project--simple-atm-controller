from simple_atm_controller.account import Account
from simple_atm_controller.api_interface import ApiInterface


def test_get_balance():
    api = ApiInterface()
    account = Account(api)
    assert isinstance(account.get_balance(), int)


def test_deposit():
    api = ApiInterface()
    account = Account(api)
    assert account.deposit(100)


def test_withdraw():
    api = ApiInterface()
    account = Account(api)
    assert account.withdraw(100)
