from typing import Annotated

import fastapi
from fastapi import APIRouter, Depends
from fastapi.responses import Response
from pydantic import PositiveInt

from src.dependencies.repositories import get_balance_repository
from src.models import Balance
from src.repositories import BalanceRepository
from src.services.balance_service import BalanceService

router = APIRouter(
    prefix="/balance",
    tags=["balances"],
)


@router.get(
    "",
    status_code=fastapi.status.HTTP_200_OK,
    summary="Get one or all balances",
    response_model=None,
    responses={
        200: {
            "description": "The balance(s) were retrieved",
            "model": Balance,
        },
        404: {
            "description": "The balance was not found",
            "content": {"application/json": {"example": 0}},
        },
    },
)
async def get_balances(
    repository: Annotated[BalanceRepository, Depends(get_balance_repository)],
    account_id: Annotated[
        PositiveInt | None,
        fastapi.Query(description="The account ID to get the balance for"),
    ] = None,
) -> list[Balance] | str | Response:
    service = BalanceService(repository)
    balances: list[Balance] | str | None = None

    if account_id:
        balances = service.get_user_balance(account_id)
    else:
        balances = service.get_all_balances()

    if balances is None:
        return Response(
            content="0",
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            media_type="application/json",
        )

    return balances
