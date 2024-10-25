from fastapi import APIRouter, FastAPI, status
from fastapi.responses import Response

from src.api import balances, events
from src.dependencies import global_balance_repo

base_router = APIRouter(
    tags=["base"],
)


@base_router.post("/reset")
async def reset_api_data():
    global_balance_repo.clear()
    return Response(
        status_code=status.HTTP_200_OK,
        media_type="text/plain",
        content="OK",
    )


def create_application() -> FastAPI:
    app = FastAPI()

    app.include_router(base_router)
    app.include_router(events.router)
    app.include_router(balances.router)

    return app


app = create_application()
