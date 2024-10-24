from fastapi import APIRouter
import fastapi

from strategies import BalanceProcessStrategy

router = APIRouter(
    prefix="/event",
    tags=["events"],
)


@router.post("/", status_code=fastapi.status.HTTP_201_CREATED)
async def process_event():
    return None
