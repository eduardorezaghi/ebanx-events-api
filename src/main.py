from typing import Union

from fastapi import APIRouter, Depends, FastAPI

from src.api import balances, events


def create_application() -> FastAPI:
    app = FastAPI()

    app.include_router(events.router)
    app.include_router(balances.router)

    return app


app = create_application()
