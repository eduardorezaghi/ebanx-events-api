from src.models.balance import Balance
from src.repositories import BalanceRepository


class BalanceService:
    def __init__(self, balance_repository: BalanceRepository):
        self.balance_repository = balance_repository

    def get_all_balances(self) -> list[Balance]:
        return self.balance_repository.get_all_balances()

    def get_user_balance(self, user_id: int) -> str | None:
        _balance = self.balance_repository.get_balance(str(user_id))
        return str(_balance.balance) if _balance else None
