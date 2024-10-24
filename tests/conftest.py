import pytest
from starlette.testclient import TestClient



@pytest.fixture(scope="module")
def test_client():
    with TestClient(main.app) as test_client:
        yield test_client

