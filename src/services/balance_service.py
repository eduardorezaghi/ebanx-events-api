from decimal import Decimal

from src.models.balance import Balance
from src.repositories import BalanceRepository


class BalanceService:
    def __init__(self, balance_repository: BalanceRepository):
        self.balance_repository = balance_repository

    def create_balance(self, account_id: int, balance: Decimal) -> Balance:
        return self.balance_repository.create_balance(account_id, balance)

    def get_all_balances(self) -> list[Balance]:
        return self.balance_repository.get_all_balances() or []

    def get_user_balance(self, user_id: int) -> str | None:
        _balance = self.balance_repository.get_balance(str(user_id))
        return str(_balance.balance) if _balance else None
