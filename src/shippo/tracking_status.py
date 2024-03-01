"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .sdkconfiguration import SDKConfiguration
from shippo import utils
from shippo._hooks import HookContext
from shippo.models import components, errors, operations
from typing import Optional

class TrackingStatus:
    r"""<p style=\\"text-align: center; background-color: #F2F3F4;\\"></br>
    If you purchased your shipping label through Shippo, you can also get all the tracking details of your Shipment 
    from the <a href=\"#tag/Transactions\">Transaction</a> object.
    </br></br></p>
    A tracking status of a package is an indication of current location of a package in the supply chain. For example,  sorting, warehousing, or out for delivery. Use the tracking status object to track the location of your shipments.

    When using your <a href=\"https://docs.goshippo.com/docs/guides_general/authentication/\">Test</a> token for tracking, you need to use Shippo's 
    predefined tokens for testing different tracking statuses. You can find more information in our 
    <a href=\"https://docs.goshippo.com/docs/tracking/tracking/\">Tracking tutorial</a> on how to do this, and what the 
    payloads look like.      
    <SchemaDefinition schemaRef=\"#/components/schemas/Track\"/>
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def create_track(self, shippo_api_version: Optional[str] = None, tracks_request: Optional[components.TracksRequest] = None) -> operations.CreateTrackResponse:
        r"""Register a tracking webhook
        Registers a webhook that will send HTTP notifications to you when the status of your tracked package changes. For more details on creating a webhook, see our guides on <a href=\"https://docs.goshippo.com/docs/tracking/webhooks/\">Webhooks</a> and <a href=\"https://docs.goshippo.com/docs/tracking/tracking/\">Tracking</a>.
        """
        hook_ctx = HookContext(operation_id='CreateTrack', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.CreateTrackRequest(
            shippo_api_version=shippo_api_version,
            tracks_request=tracks_request,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/tracks'
        headers = utils.get_headers(request)
        req_content_type, data, form = utils.serialize_request_body(request, operations.CreateTrackRequest, "tracks_request", False, True, 'json')
        if req_content_type is not None and req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('POST', url, data=data, files=form, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.CreateTrackResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[components.Track])
                res.track = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.Tracks400Response)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    
    
    def get_track(self, tracking_number: str, carrier: str, shippo_api_version: Optional[str] = None) -> operations.GetTrackResponse:
        r"""Get a tracking status
        Returns the tracking status of a shipment using a carrier name and a tracking number.
        """
        hook_ctx = HookContext(operation_id='GetTrack', oauth2_scopes=[], security_source=self.sdk_configuration.security)
        request = operations.GetTrackRequest(
            tracking_number=tracking_number,
            carrier=carrier,
            shippo_api_version=shippo_api_version,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetTrackRequest, base_url, '/tracks/{Carrier}/{TrackingNumber}', request)
        headers = utils.get_headers(request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        
        try:
            req = self.sdk_configuration.get_hooks().before_request(
                hook_ctx, 
                requests_http.Request('GET', url, headers=headers).prepare(),
            )
            http_res = client.send(req)
        except Exception as e:
            _, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, None, e)
            raise e

        if utils.match_status_codes(['400','4XX','5XX'], http_res.status_code):
            http_res, e = self.sdk_configuration.get_hooks().after_error(hook_ctx, http_res, None)
            if e:
                raise e
        else:
            result = self.sdk_configuration.get_hooks().after_success(hook_ctx, http_res)
            if isinstance(result, Exception):
                raise result
            http_res = result
        
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.GetTrackResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[components.Track])
                res.track = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code == 400:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, errors.Tracks400Response)
                out.raw_response = http_res
                raise out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    