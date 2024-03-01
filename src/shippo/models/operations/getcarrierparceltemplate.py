"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.components import carrierparceltemplatestruct as components_carrierparceltemplatestruct
from typing import Optional


@dataclasses.dataclass
class GetCarrierParcelTemplateRequest:
    carrier_parcel_template_token: str = dataclasses.field(metadata={'path_param': { 'field_name': 'CarrierParcelTemplateToken', 'style': 'simple', 'explode': False }})
    r"""The unique string representation of the carrier parcel template"""
    shippo_api_version: Optional[str] = dataclasses.field(default=None, metadata={'header': { 'field_name': 'SHIPPO-API-VERSION', 'style': 'simple', 'explode': False }})
    r"""String used to pick a non-default API version to use"""
    



@dataclasses.dataclass
class GetCarrierParcelTemplateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    carrier_parcel_template_struct: Optional[components_carrierparceltemplatestruct.CarrierParcelTemplateStruct] = dataclasses.field(default=None)
    

