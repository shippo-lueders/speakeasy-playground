"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import address as components_address
from typing import Optional


@dataclasses.dataclass
class GetAddressRequest:
    address_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'AddressId', 'style': 'simple', 'explode': False }})
    r"""Object ID of the address"""
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class GetAddressResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    address: Optional[components_address.Address] = dataclasses.field(default=None)
    

