from decimal import Decimal

from src.models import Balance, EventRequest
from src.repositories import BalanceRepository
from src.strategies import EventProcessStrategy


class BalanceService:
    def __init__(self, balance_repository: BalanceRepository):
        self.balance_repository = balance_repository

    def create_balance(self, account_id: int, balance: Decimal) -> Balance:
        return self.balance_repository.create_balance(account_id, balance)

    def get_all_balances(self) -> list[Balance]:
        return self.balance_repository.get_all_balances() or []

    def get_user_balance(self, user_id: int) -> Balance | None:
        return self.balance_repository.get_balance(str(user_id))

    async def process_event(
        self,
        event_request: EventRequest,
    ):
        service = BalanceService(self.balance_repository)
        strategy = EventProcessStrategy().get_strategy(event_request.event_type)

        return await strategy.process(service, event_request)
