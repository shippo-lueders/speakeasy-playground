import httpretty
import pytest
import shippo

BASE_URL = "http://localhost:9500"


class TestExample:

    @pytest.fixture
    def api(self):
        return shippo.Shippo(server_url=BASE_URL)

    @httpretty.activate
    def test_example(self, api: shippo.Shippo):
        httpretty.register_uri(
            httpretty.GET, f"{BASE_URL}/example", status=200, content_type="application/json",
            body='{"field": "value"}'
        )

        response = api.example()
        print(response)
