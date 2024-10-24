from typing import Literal
from abc import ABC, abstractmethod


class EventProcessStrategy(ABC):
    @abstractmethod
    def process(self):
        pass


class BalanceProcessStrategy(EventProcessStrategy):
    def __init__(self, event_type: Literal["deposit", "withdraw"]):
        self.event = event_type

    def process(self): ...
