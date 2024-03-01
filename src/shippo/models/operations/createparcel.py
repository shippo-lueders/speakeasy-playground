"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import parcel as components_parcel
from ...models.components import parcelrequest as components_parcelrequest
from typing import Optional


@dataclasses.dataclass
class CreateParcelRequest:
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    parcel_request: Optional[components_parcelrequest.ParcelRequest] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    r"""Parcel details."""
    



@dataclasses.dataclass
class CreateParcelResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    parcel: Optional[components_parcel.Parcel] = dataclasses.field(default=None)
    

