from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Literal

from src.models import (
    BalanceDeposited,
    BalanceInfo,
    BalanceTransfered,
    BalanceWithdrawn,
    EventRequest,
)


class EventStrategy(ABC):
    @abstractmethod
    async def process(self, *args, **kwargs):
        pass


class DepositStrategy(EventStrategy):
    async def process(self, service, event_request: EventRequest):
        _balance = service.get_user_balance(str(event_request.destination))
        if _balance is None:
            balance = service.create_balance(
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
        ).to_plain_text()


class WithdrawStrategy(EventStrategy):
    async def process(self, service, event_request: EventRequest):
        _balance = service.get_user_balance(event_request.origin)
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
        ).to_plain_text()


class TransferStrategy(EventStrategy):
    async def process(self, service, event_request: EventRequest):
        _origin = service.get_user_balance(str(event_request.origin))
        _destination = service.get_user_balance(str(event_request.destination))

        if _origin is None:
            raise Exception("Origin account not found")

        if _destination is None:
            _destination = service.create_balance(
                account_id=event_request.destination,
                balance=Decimal(0),
            )

        try:
            _origin.withdraw(event_request.amount)
            _destination.deposit(event_request.amount)
        except ValueError:
            raise

        return BalanceTransfered(
            origin=BalanceInfo(
                id=_origin.account_id,
                balance=_origin.balance,
            ),
            destination=BalanceInfo(
                id=_destination.account_id,
                balance=_destination.balance,
            ),
        ).to_plain_text()


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
            "transfer": TransferStrategy(),
        }

    def get_strategy(
        self, event_type: Literal["deposit", "withdraw", "transfer"]
    ) -> EventStrategy:
        strategy = self.strategies.get(event_type)
        if strategy is None:
            raise ValueError(f"No strategy found for event type: {event_type}")

        return strategy
