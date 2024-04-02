import httpretty
import pytest
import shippo

BASE_URL = "http://localhost:9500"

class TestExample:

    @pytest.fixture
    def api(self):
        return shippo.Shippo(server_url=BASE_URL)

    @httpretty.activate
    def test_example_one(self, api: shippo.Shippo):
        httpretty.register_uri(
            httpretty.POST, f"{BASE_URL}/example", status=201, content_type="application/json",
            body='{"field": "value"}'
        )
        
        response = api.example()
        print(response)

    @httpretty.activate
    def test_example_two(self, api: shippo.Shippo):
        httpretty.register_uri(
            httpretty.POST, f"{BASE_URL}/example", status=201, content_type="application/json",
            body='{"field": {"example": "value"}}'
        )

        response = api.example()
        print(response)
