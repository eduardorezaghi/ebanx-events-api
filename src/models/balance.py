from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, PositiveInt, field_validator


class Balance(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    account_id: PositiveInt
    balance: Decimal = Field(..., decimal_places=2, max_digits=20)

    @field_validator("balance")
    def validate_balance(cls, value: Decimal) -> Decimal:
        if value < 0:
            raise ValueError("Balance cannot be negative")
        return value

    def deposit(self, amount: Decimal) -> Decimal:
        if amount < 0:
            raise ValueError("Deposit amount must be greater than 0")

        self.balance += amount

        return self.balance

    def withdraw(self, amount: Decimal) -> Decimal:
        if amount < 0:
            raise ValueError("Withdraw amount must be greater than 0")

        if self.balance < amount:
            raise ValueError("Insufficient funds")

        self.balance -= amount

        return self.balance


class BalanceInfo(BaseModel):
    id: PositiveInt
    balance: Decimal


class BalanceWithdrawn(BaseModel):
    origin: BalanceInfo

    # 1. I would use Pydantic's JSON serialization for this, but I kept like that due to the requirements
    # of ipkiss test suite, which matches strings instead of JSON objects.
    def to_plain_text(self) -> str:
        return f'{{"origin": {{"id": "{self.origin.id}", "balance": {self.origin.balance}}}}}'


class BalanceDeposited(BaseModel):
    destination: BalanceInfo

    # 2. I would use Pydantic's JSON serialization for this, but I kept like that due to the requirements
    # of ipkiss test suite, which matches strings instead of JSON objects.
    def to_plain_text(self) -> str:
        return f'{{"destination": {{"id": "{self.destination.id}", "balance": {self.destination.balance}}}}}'


class BalanceTransfered(BaseModel):
    origin: BalanceInfo
    destination: BalanceInfo

    # 3. I would use Pydantic's JSON serialization for this, but I kept like that due to the requirements
    # of ipkiss test suite, which matches strings instead of JSON objects.
    def to_plain_text(self) -> str:
        return f'{{"origin": {{"id":"{self.origin.id}", "balance":{self.origin.balance}}}, "destination": {{"id":"{self.destination.id}", "balance":{self.destination.balance}}}}}'
