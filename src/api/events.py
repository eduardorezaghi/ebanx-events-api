from typing import Annotated

import fastapi
from fastapi import APIRouter, Depends, HTTPException, Response

from src.dependencies.repositories import get_balance_repository
from src.models import EventRequest
from src.repositories import BalanceRepository
from src.strategies import EventProcessStrategy

router = APIRouter(
    prefix="/event",
    tags=["events"],
)


@router.post(
    "/",
    status_code=fastapi.status.HTTP_201_CREATED,
)
async def process_event(
    _request: EventRequest,
    balance_repository: Annotated[BalanceRepository, Depends(get_balance_repository)],
):
    strategy = EventProcessStrategy().get_strategy(_request.event_type)

    try:
        return await strategy.process(
            balance_repo=balance_repository, event_request=_request
        )
    except ValueError:
        return Response(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            content="0",
        )
    except Exception:
        return Response(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            content="0",
        )
