from abc import ABC, abstractmethod
from typing import Literal

from src.models import BalanceDeposited, BalanceInfo, BalanceWithdrawn, EventRequest
from src.repositories import BalanceRepository


class EventStrategy(ABC):
    @abstractmethod
    async def process(self, *args, **kwargs):
        pass


class DepositStrategy(EventStrategy):
    async def process(
        self, balance_repo: BalanceRepository, event_request: EventRequest
    ):
        _balance = balance_repo.get_balance(str(event_request.destination))
        if _balance is None:
            balance = balance_repo.create_balance(
                account_id=event_request.destination,
                balance=event_request.amount,
            )
        else:
            try:
                _balance.deposit(event_request.amount)
            except ValueError:
                raise

            balance = _balance

        return BalanceDeposited(
            destination=BalanceInfo(
                id=balance.account_id,
                balance=balance.balance,
            )
        )


class WithdrawStrategy(EventStrategy):
    async def process(
        self, balance_repo: BalanceRepository, event_request: EventRequest
    ):
        _balance = balance_repo.get_balance(str(event_request.origin))
        if _balance is None:
            raise Exception("Account not found")

        try:
            _balance.withdraw(event_request.amount)
        except ValueError:
            raise

        return BalanceWithdrawn(
            origin=BalanceInfo(
                id=_balance.account_id,
                balance=_balance.balance,
            )
        )


# Context class
class EventProcessStrategy:
    """
    Context processor class for Strategy pattern.

    This class is responsible for selecting the appropriate strategy based on the event type.
    """

    def __init__(self) -> None:
        self.strategies: dict[str, EventStrategy] = {
            "deposit": DepositStrategy(),
            "withdraw": WithdrawStrategy(),
        }

    def get_strategy(self, event_type: Literal["deposit", "withdraw"]) -> EventStrategy:
        strategy = self.strategies.get(event_type)
        if strategy is None:
            raise ValueError(f"No strategy found for event type: {event_type}")

        return strategy
