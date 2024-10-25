from decimal import Decimal

from src.models.balance import Balance


class BalanceRepository:
    def __init__(self, objs: list[Balance] | None = None):
        # Here, I would use something like a database connection or ORM to interact with the database.
        # In SQLAlchemy, it would be something like:
        #       self.session = session
        #       self.balances = session.query(Balance).all()
        # and then I would use the session to interact with the database.
        # For simplicity, I'm using a dictionary to simulate a NoSQL database.
        self.balances: dict[str, Balance] = {}
        if objs:
            for obj in objs:
                self.balances[str(obj.account_id)] = obj

    def clear(self):
        self.balances = {}

    def create_balance(self, account_id: int, balance: Decimal) -> Balance:
        _balance = Balance(account_id=account_id, balance=Decimal(balance))
        self.balances[str(account_id)] = _balance
        return _balance

    def get_all_balances(self) -> list[Balance] | None:
        return list(self.balances.values())

    def get_balance(self, user_id: str) -> Balance | None:
        return self.balances.get(user_id)
