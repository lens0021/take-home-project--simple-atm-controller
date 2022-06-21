from .api_interface import ApiInterface
from typing import List
from .account import Account


class Card:
    """
    A card with a cardNumber
    """

    def __init__(self, cardNumber: str, api: ApiInterface):
        self.cardNumber = cardNumber
        self.api = api or ApiInterface()

    def authenticate(self, pin: int) -> bool:
        """
        Authenticates the card with the given pin
        """
        return self.api.authenticate(self.cardNumber, pin)

    def list_accounts(self) -> List[Account]:
        """
        Lists all accounts on the card
        """
        if not self.api.authorized:
            raise Exception("Not authenticated")
        return self.api.list_accounts(self.cardNumber)
