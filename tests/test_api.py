from simple_atm_controller.api_interface import ApiInterface


def test_authenticate():
    api = ApiInterface()
    assert api.authenticate('0000', 1234)


def test_list_accounts():
    api = ApiInterface()
    # assert is a list of Account objects
    assert isinstance(api.list_accounts("0000"), list)
