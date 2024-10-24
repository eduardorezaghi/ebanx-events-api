from decimal import Decimal
from typing import Annotated, Literal

from fastapi import Body
from pydantic import BaseModel, ConfigDict, Field, PositiveInt


class EventRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    event_type: Annotated[
        Literal["deposit", "withdraw", "transfer"], Field(..., alias="type")
    ]
    destination: Annotated[PositiveInt, Body(default=None)]
    origin: Annotated[PositiveInt, Body(default=None)]
    amount: Annotated[Decimal, Body(...)]
