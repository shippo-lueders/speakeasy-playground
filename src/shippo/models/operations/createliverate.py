"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import liveratecreaterequest as components_liveratecreaterequest
from ...models.components import liveratelist as components_liveratelist
from typing import Optional


@dataclasses.dataclass
class CreateLiveRateRequest:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    live_rate_create_request: Optional[components_liveratecreaterequest.LiveRateCreateRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Generate rates at checkout"""
    



@dataclasses.dataclass
class CreateLiveRateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    live_rate_list: Optional[components_liveratelist.LiveRateList] = dataclasses.field(default=None)
    

