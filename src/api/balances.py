
from fastapi import APIRouter
import fastapi

router = APIRouter(
    prefix="/balance",
    tags=["balances"],
)


@router.get("/", status_code=fastapi.status.HTTP_200_OK)
async def get_balance():
    return None
