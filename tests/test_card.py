from simple_atm_controller.card import Card
from simple_atm_controller.api_interface import ApiInterface
import pytest


def test_constructor():
    card = Card("12345678", ApiInterface())
    assert card.cardNumber == "12345678"


def test_authenticate():
    card = Card("12345678", ApiInterface())
    assert card.authenticate(1234)


def test_list_accounts():
    card = Card("12345678", ApiInterface())

    with pytest.raises(Exception):
        card.list_accounts()

    card.authenticate(1234)
    assert isinstance(card.list_accounts(), list)
