import httpretty
import requests as requests

import shippo

BASE_URL = "http://localhost:9500"


class TestGlobalHeader:

    def request_callback(self, request, uri, response_headers):
        assert request.headers.get('header_param') == "value"
        return [200, {}, '{}']

    @httpretty.activate(allow_net_connect=False)
    def test_local_header(self):
        httpretty.register_uri(httpretty.GET, f"{BASE_URL}/example", body=self.request_callback)

        api = shippo.Shippo(server_url=BASE_URL)
        api.example(header_param="value")

    @httpretty.activate(allow_net_connect=False)
    def test_global_header(self):
        httpretty.register_uri(httpretty.GET, f"{BASE_URL}/example", body=self.request_callback)

        http_client = requests.Session()
        http_client.headers.update({'header_param': 'value'})
        api = shippo.Shippo(server_url=BASE_URL, client=http_client)

        api.example()
