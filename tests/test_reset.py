import http

from tests.conftest import HttpTests


class TestReset(HttpTests):
    def test_reset_api_data(self):
        # Act
        response = self.client.post("/reset/")

        # Assert
        assert response.status_code == http.HTTPStatus.OK
        assert response.text == "null"
        # TODO: Assert that the data has been reset