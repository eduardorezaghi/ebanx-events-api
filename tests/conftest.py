import pytest
from starlette.testclient import TestClient

from src import main


@pytest.fixture(scope="module")
def test_client():
    with TestClient(main.app) as test_client:
        yield test_client
