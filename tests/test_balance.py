import http
from decimal import Decimal

import pytest

from src import main
from src.dependencies.repositories import get_balance_repository
from src.models import Balance
from src.repositories import BalanceRepository
from tests.conftest import HttpTests


@pytest.fixture
def balance_repo():
    yield BalanceRepository(
        [
            Balance(account_id=1, balance=Decimal("89.95")),
            Balance(account_id=2, balance=Decimal("201.28")),
        ]
    )


class TestBalance(HttpTests):
    @pytest.fixture(autouse=True)
    def setup_method(self, balance_repo: BalanceRepository):
        main.app.dependency_overrides[get_balance_repository] = lambda: balance_repo

    def test_query_balance(self):
        # Act
        response = self.client.get("/balance", params={"account_id": 1})

        # Assert
        assert response.status_code == http.HTTPStatus.OK.value
        assert response.text == "89.95"


    def test_query_balances(self):
        # Act
        response = self.client.get("/balance")

        # Assert
        assert response.status_code == http.HTTPStatus.OK.value
        assert response.json() == {"1": "89.95", "2": "201.28"}

    def test_unexisting_balance_should_return_404(self):
        # Act
        response = self.client.get("/balance", params={"account_id": 999})

        # Assert
        assert response.status_code == http.HTTPStatus.NOT_FOUND.value
        assert response.text == "0"
