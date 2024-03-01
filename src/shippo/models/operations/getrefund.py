"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import refund as components_refund
from typing import Optional


@dataclasses.dataclass
class GetRefundRequest:
    refund_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'RefundId', 'style': 'simple', 'explode': False }})
    r"""Object ID of the refund to update"""
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class GetRefundResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    refund: Optional[components_refund.Refund] = dataclasses.field(default=None)
    

