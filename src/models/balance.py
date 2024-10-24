from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field, PositiveInt


class Balance(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    account_id: PositiveInt
    balance: Decimal = Field(..., decimal_places=2, max_digits=20)
