from decimal import Decimal

from src.models.balance import Balance
from src.repositories import BalanceRepository


def get_balance_repository():
    yield BalanceRepository(
        [
            Balance(account_id=1, balance=Decimal("99.95")),
            Balance(account_id=2, balance=Decimal("201.28")),
        ]
    )
