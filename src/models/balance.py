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


class BalanceDeposited(BaseModel):
    destination: BalanceInfo
