from src.repositories import BalanceRepository

global_balance_repo = BalanceRepository()


def get_balance_repository():
    yield global_balance_repo
