from typing import Generator

import pytest
from starlette.testclient import TestClient

from src import main


@pytest.fixture(scope="module")
def test_client() -> Generator[TestClient, None, None]:
    with TestClient(main.app) as test_client:
        yield test_client


class HttpTests:
    @pytest.fixture(autouse=True)
    def setup(self, test_client: TestClient) -> None:
        self.client = test_client
