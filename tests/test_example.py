import httpretty
import pytest
import shippo

from shippo.models.components import EnumSet

BASE_URL = "http://localhost:9500"


class TestExample:

    @pytest.fixture
    def api(self):
        return shippo.Shippo(server_url=BASE_URL)

    @httpretty.activate
    def test_example(self, api: shippo.Shippo):
        httpretty.register_uri(
            httpretty.GET, f"{BASE_URL}/example/1", status=200, content_type="application/json",
            body='{"field": "one"}'
        )

        response = api.get("1")
        print(response)
