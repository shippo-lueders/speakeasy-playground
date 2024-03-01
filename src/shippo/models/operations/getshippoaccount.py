"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import shippoaccount as components_shippoaccount
from typing import Optional


@dataclasses.dataclass
class GetShippoAccountRequest:
    shippo_account_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'ShippoAccountId', 'style': 'simple', 'explode': False }})
    r"""Object ID of the ShippoAccount"""
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class GetShippoAccountResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    shippo_account: Optional[components_shippoaccount.ShippoAccount] = dataclasses.field(default=None)
    

