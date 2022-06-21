# Simple atm controller

[![.github/workflows/ci.yaml](https://github.com/lens0021/take-home-project--simple-atm-controller/actions/workflows/ci.yaml/badge.svg)](https://github.com/lens0021/take-home-project--simple-atm-controller/actions/workflows/ci.yaml) [![codecov](https://codecov.io/gh/lens0021/take-home-project--simple-atm-controller/branch/main/graph/badge.svg?token=GcRdoex9SN)](https://codecov.io/gh/lens0021/take-home-project--simple-atm-controller)

This is a library that provides functions/classes for future bare-bone workflows.

## Usage

```py
from simple_atm_controller import Card, Account
from your_custom_api import YourCustomApi

card = new Card('0000000000000000000', YourCustomApi()) # Card number
try:
  card.authenticate(0000) # Pin number
  accounts = card.list_accounts()
except Exception as err:
  print(f'Error occurred: {err}')
for account in accounts:
  try:
    print(account.get_balance())
  except Exception as err:
    print(f'Error occurred: {err}')

# NOTE: This is not a transfer. Transferring is not implemented.
if account[0]:
  status = account[0].deposit(10)
if account[1]:
  status = account[1].withdraw(10)
```

## Before using this

The API that is required for this library is not strictly defined. You should do the below steps:

- implement a subclass of ApiInterface
- Implement methods of it.
