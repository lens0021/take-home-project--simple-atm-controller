from __future__ import annotations
from typing import List
from simple_atm_controller.account import Account


class ApiInterface:
    def __init__(self):
        self.authorized = False

    def authenticate(self, cardNumber: str, pin: int) -> bool:
        # TODO: Implement this method
        self.authorized = True
        return True

    def get_balance(self) -> int:
        # TODO: Implement this method
        return 0

    def list_accounts(self, card_number: str) -> List[Account]:
        # TODO: Implement this method
        return [Account(self), Account(self)]

    def deposit(self, account: Account, amount: int) -> bool:
        # TODO: Implement this method
        return True

    def withdraw(self, account: Account, amount: int) -> bool:
        # TODO: Implement this method
        return True
