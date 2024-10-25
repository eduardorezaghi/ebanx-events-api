# EBANX Events API

## Summary
This is a simple API that have four endpoints:
- POST `/reset`: Clear all balances.
- POST `/event`: Perform `
    - `adeposit` adds a given amount to the account balance.
    - `withdraw` subtracts a given amount from the account balance.
    - `transfer` subtracts a given amount from the source account and adds it to the destination account.
    If the destination account does not exist, it is created.
- GET `/account?account_id={account_id}`: Get the balance for a given account.
- (extra) ` GET /account`: Get the balance for all accounts.


To run the application, you need to have Python and it's venv module installed, or Poetry.

## Running with Python
To create a virtual environment and install the dependencies, run the following commands:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running with Poetry
To install the dependencies with Poetry, run the following commands:
```bash
poetry install
```
It will create a virtual environment for you. To activate it, run:
```bash
poetry shell
```

## Running the application
To run the application, you can use either of the following commands:
```bash
fastapi dev src/main.py # If you used venv
poetry run fastapi dev src/main.py # If you used Poetry
uvicorn src.main:app --reload # Directly call uvicorn, must be in <projectRoot>
```

You can navigate to `http://localhost:8000/docs` to see the API documentation using Swagger.

## Running the tests
To run the tests, you can use either of the following commands:
```bash
pytest # If you used venv
poetry run pytest # If you used Poetry
```

## Curl examples
```bash
# Create an acount with id 100 and balance 150
curl -X 'POST' \
  'http://localhost:8000/event' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "type": "deposit",
  "destination": 100,
  "amount": 150
}'
# {"destination": {"id":"100", "balance": 150}}
```

```bash
# Get the balance of account 100
curl -X 'GET' \
  'http://localhost:8000/account?account_id=100' \
  -H 'accept: application/json'
# {"id":"100", "balance": 150}
```

```bash
# Withdraw amount 40 from account 100
curl -X 'POST' \
  'http://localhost:8000/event' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "type": "withdraw",
    "origin": 100,
    "amount": 40
}'
# {"origin": {"id":"100", "balance": 110}}
```

```bash
# Transfer amount 10 from account 100 to account 200
curl -X 'POST' \
  'http://localhost:8000/event' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "type": "transfer",
  "origin": 100,
  "destination": 300,
  "amount": 10
}'
# {"origin": {"id":"100", "balance": 140}, "destination": {"id":"300", "balance": 10}}
```