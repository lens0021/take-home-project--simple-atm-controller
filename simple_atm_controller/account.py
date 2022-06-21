from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .api_interface import ApiInterface


class Account:
    def __init__(self, api: ApiInterface):
        self.api = api

    def get_balance(self):
        return self.api.get_balance()

    def deposit(self, amount: int):
        return self.api.deposit(self, amount)

    def withdraw(self, amount: int):
        return self.api.withdraw(self, amount)
