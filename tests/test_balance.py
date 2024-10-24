import pytest


class TestBalance:
    @pytest.fixture(autouse=True)
    def setup(self, test_client):
        self.client = test_client

    def test_query_balance(self):
        # Act
        response = self.client.get("/balance/")

        # Assert
        assert response.status_code == 200
        assert response.json() is None
