from typing import Union

from fastapi import APIRouter, Depends, FastAPI

from src.api import balances, events


base_router = APIRouter(
    tags=["base"],
)

@base_router.post("/reset", status_code=200)
async def reset_api_data():
    return None

def create_application() -> FastAPI:
    app = FastAPI()

    app.include_router(base_router)
    app.include_router(events.router)
    app.include_router(balances.router)

    return app


app = create_application()
