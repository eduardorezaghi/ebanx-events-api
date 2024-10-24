from decimal import Decimal

from src.models import Balance
from src.repositories import BalanceRepository

global_balance_repo = BalanceRepository(
    [
        Balance(account_id=100, balance=Decimal("99.95")),
        Balance(account_id=200, balance=Decimal("201.28")),
    ]
)


def get_balance_repository():
    yield global_balance_repo
