import http

from tests.conftest import HttpTests


class TestBalance(HttpTests):
    def test_query_balance(self):
        # Act
        response = self.client.get("/balance/", params={"account_id": 1})

        # Assert
        assert response.status_code == 200
        assert response.json() is None

    def test_unexisting_balance_should_return_404(self):
        # Act
        response = self.client.get("/balance/", params={"account_id": 999})

        # Assert
        assert response.status_code == http.HTTPStatus.NOT_FOUND.value
