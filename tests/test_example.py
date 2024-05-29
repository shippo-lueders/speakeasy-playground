import httpretty
import pytest
import shippo

from src.shippo.models.components import ExampleObject

BASE_URL = "http://localhost:9500"


class TestExample:

    @pytest.fixture
    def api(self):
        return shippo.Shippo(server_url=BASE_URL)

    @httpretty.activate
    def test_field_simple(self, api: shippo.Shippo):
        httpretty.register_uri(
            httpretty.GET, f"{BASE_URL}/example", status=200, content_type="application/json",
            body='{"field": "value"}'
        )

        response = api.example()
        assert isinstance(response.field, str)

    @httpretty.activate
    def test_field_complex(self, api: shippo.Shippo):
        httpretty.register_uri(
            httpretty.GET, f"{BASE_URL}/example", status=200, content_type="application/json",
            body='{"field": {"other_field": "value"}}'
        )

        response = api.example()
        assert type(response.field).__name__ == ExampleObject.__name__
