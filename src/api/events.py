from typing import Annotated

import fastapi
from fastapi import APIRouter, Depends, Response

from src.dependencies.repositories import get_balance_repository
from src.models import EventRequest
from src.repositories import BalanceRepository
from src.services.balance_service import BalanceService

router = APIRouter(
    prefix="/event",
    tags=["events"],
)


@router.post(
    "",
)
async def process_event(
    _request: EventRequest,
    balance_repository: Annotated[BalanceRepository, Depends(get_balance_repository)],
):
    service = BalanceService(balance_repository)

    try:
        plaintext_resp = await service.process_event(_request)

        return Response(
            status_code=fastapi.status.HTTP_201_CREATED,
            media_type="text/plain",
            content=plaintext_resp,
        )

    except ValueError:
        return Response(
            status_code=fastapi.status.HTTP_400_BAD_REQUEST,
            media_type="text/plain",
            content=b"0",
        )
    except Exception:
        return Response(
            status_code=fastapi.status.HTTP_404_NOT_FOUND,
            media_type="text/plain",
            content=b"0",
        )
