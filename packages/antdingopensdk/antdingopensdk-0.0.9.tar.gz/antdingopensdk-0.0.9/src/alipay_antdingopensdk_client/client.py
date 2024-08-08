# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alipay_antdingopensdk_client import models as antdingopensdk_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    _access_key_id: str = None
    _access_key_secret: str = None
    _webgw_secret: str = None
    _webgw_version: str = None
    _webgw_app_id: str = None
    _sdk_version: str = None

    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        if UtilClient.is_unset(self._region_id):
            self._region_id = 'prod'
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'dev': 'webgw.stable.alipay.net',
            'prod': 'webgw.alipay.comm',
            'pre': 'webgw-pre.alipay.com'
        }
        self._webgw_secret = 'JRvZiQzZ828kM42X'
        self._webgw_version = '2.0'
        self._webgw_app_id = 'antdingopensdk'
        self._access_key_id = config.access_key_id
        self._access_key_secret = config.access_key_secret
        self._sdk_version = '1.0.0'
        self.check_config(config)
        self._endpoint = self.get_endpoint('antdingopen', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_scenegroup_member(
        self,
        request: antdingopensdk_models.AddScenegroupMemberRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.AddScenegroupMemberResponse:
        """
        新增群成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='addScenegroupMember',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/addScenegroupMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.AddScenegroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_scenegroup_member_async(
        self,
        request: antdingopensdk_models.AddScenegroupMemberRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.AddScenegroupMemberResponse:
        """
        新增群成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='addScenegroupMember',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/addScenegroupMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.AddScenegroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_query_group_member(
        self,
        request: antdingopensdk_models.BatchQueryGroupMemberRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.BatchQueryGroupMemberResponse:
        """
        查询群成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='batchQueryGroupMember',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/batchQueryGroupMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.BatchQueryGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_query_group_member_async(
        self,
        request: antdingopensdk_models.BatchQueryGroupMemberRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.BatchQueryGroupMemberResponse:
        """
        查询群成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='batchQueryGroupMember',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/batchQueryGroupMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.BatchQueryGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_user_is_group_member(
        self,
        request: antdingopensdk_models.CheckUserIsGroupMemberRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CheckUserIsGroupMemberResponse:
        """
        查询用户是否为企业内部群成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='checkUserIsGroupMember',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/checkUserIsGroupMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CheckUserIsGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_user_is_group_member_async(
        self,
        request: antdingopensdk_models.CheckUserIsGroupMemberRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CheckUserIsGroupMemberResponse:
        """
        查询用户是否为企业内部群成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='checkUserIsGroupMember',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/checkUserIsGroupMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CheckUserIsGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_topbox(
        self,
        request: antdingopensdk_models.CloseTopboxRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CloseTopboxResponse:
        """
        关闭互动卡片吊顶
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='closeTopbox',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/closeTopbox',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CloseTopboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_topbox_async(
        self,
        request: antdingopensdk_models.CloseTopboxRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CloseTopboxResponse:
        """
        关闭互动卡片吊顶
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='closeTopbox',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/closeTopbox',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CloseTopboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scenegroup(
        self,
        request: antdingopensdk_models.CreateScenegroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateScenegroupResponse:
        """
        创建场景群
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createScenegroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/createScenegroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateScenegroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scenegroup_async(
        self,
        request: antdingopensdk_models.CreateScenegroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateScenegroupResponse:
        """
        创建场景群
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createScenegroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/createScenegroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateScenegroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_topbox(
        self,
        request: antdingopensdk_models.CreateTopboxRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateTopboxResponse:
        """
        创建并开启互动卡片吊顶
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createTopbox',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/createTopbox',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateTopboxResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_topbox_async(
        self,
        request: antdingopensdk_models.CreateTopboxRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateTopboxResponse:
        """
        创建并开启互动卡片吊顶
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createTopbox',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/createTopbox',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateTopboxResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scenegroup_member(
        self,
        request: antdingopensdk_models.DeleteScenegroupMemberRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteScenegroupMemberResponse:
        """
        删除群成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteScenegroupMember',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/deleteScenegroupMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteScenegroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scenegroup_member_async(
        self,
        request: antdingopensdk_models.DeleteScenegroupMemberRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteScenegroupMemberResponse:
        """
        删除群成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteScenegroupMember',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/deleteScenegroupMember',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteScenegroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inner_group_members(
        self,
        request: antdingopensdk_models.GetInnerGroupMembersRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetInnerGroupMembersResponse:
        """
        查询企业内部群成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getInnerGroupMembers',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/getInnerGroupMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetInnerGroupMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inner_group_members_async(
        self,
        request: antdingopensdk_models.GetInnerGroupMembersRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetInnerGroupMembersResponse:
        """
        查询企业内部群成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getInnerGroupMembers',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/getInnerGroupMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetInnerGroupMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_newest_inner_groups(
        self,
        request: antdingopensdk_models.GetNewestInnerGroupsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetNewestInnerGroupsResponse:
        """
        查询最近活跃的企业内部群列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getNewestInnerGroups',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/getNewestInnerGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetNewestInnerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_newest_inner_groups_async(
        self,
        request: antdingopensdk_models.GetNewestInnerGroupsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetNewestInnerGroupsResponse:
        """
        查询最近活跃的企业内部群列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getNewestInnerGroups',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/getNewestInnerGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetNewestInnerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scene_group_info(
        self,
        request: antdingopensdk_models.GetSceneGroupInfoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetSceneGroupInfoResponse:
        """
        查询群简要信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getSceneGroupInfo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/getSceneGroupInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetSceneGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scene_group_info_async(
        self,
        request: antdingopensdk_models.GetSceneGroupInfoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetSceneGroupInfoResponse:
        """
        查询群简要信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getSceneGroupInfo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/getSceneGroupInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetSceneGroupInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scenegroup(
        self,
        request: antdingopensdk_models.GetScenegroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetScenegroupResponse:
        """
        查询群信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getScenegroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/getScenegroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetScenegroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scenegroup_async(
        self,
        request: antdingopensdk_models.GetScenegroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetScenegroupResponse:
        """
        查询群信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getScenegroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/getScenegroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetScenegroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_group_mute_status(
        self,
        request: antdingopensdk_models.QueryGroupMuteStatusRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryGroupMuteStatusResponse:
        """
        查询群成员禁言状态
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryGroupMuteStatus',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/queryGroupMuteStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryGroupMuteStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_group_mute_status_async(
        self,
        request: antdingopensdk_models.QueryGroupMuteStatusRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryGroupMuteStatusResponse:
        """
        查询群成员禁言状态
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryGroupMuteStatus',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/queryGroupMuteStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryGroupMuteStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_scene_group_template_robot(
        self,
        request: antdingopensdk_models.QuerySceneGroupTemplateRobotRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QuerySceneGroupTemplateRobotResponse:
        """
        查询群内群模版机器人
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='querySceneGroupTemplateRobot',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/querySceneGroupTemplateRobot',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QuerySceneGroupTemplateRobotResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_scene_group_template_robot_async(
        self,
        request: antdingopensdk_models.QuerySceneGroupTemplateRobotRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QuerySceneGroupTemplateRobotResponse:
        """
        查询群内群模版机器人
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='querySceneGroupTemplateRobot',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/querySceneGroupTemplateRobot',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QuerySceneGroupTemplateRobotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_inner_groups(
        self,
        request: antdingopensdk_models.SearchInnerGroupsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SearchInnerGroupsResponse:
        """
        根据关键词搜索企业内部群
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='searchInnerGroups',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/searchInnerGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SearchInnerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_inner_groups_async(
        self,
        request: antdingopensdk_models.SearchInnerGroupsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SearchInnerGroupsResponse:
        """
        根据关键词搜索企业内部群
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='searchInnerGroups',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/searchInnerGroups',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SearchInnerGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_scencegroup_message(
        self,
        request: antdingopensdk_models.SendScencegroupMessageRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SendScencegroupMessageResponse:
        """
        发送群助手消息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='sendScencegroupMessage',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/sendScencegroupMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SendScencegroupMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_scencegroup_message_async(
        self,
        request: antdingopensdk_models.SendScencegroupMessageRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SendScencegroupMessageResponse:
        """
        发送群助手消息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='sendScencegroupMessage',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/sendScencegroupMessage',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SendScencegroupMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_or_stop_scenegroup_template(
        self,
        request: antdingopensdk_models.StartOrStopScenegroupTemplateRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.StartOrStopScenegroupTemplateResponse:
        """
        启停群模版
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='startOrStopScenegroupTemplate',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/startOrStopScenegroupTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.StartOrStopScenegroupTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_or_stop_scenegroup_template_async(
        self,
        request: antdingopensdk_models.StartOrStopScenegroupTemplateRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.StartOrStopScenegroupTemplateResponse:
        """
        启停群模版
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='startOrStopScenegroupTemplate',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/startOrStopScenegroupTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.StartOrStopScenegroupTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group_sub_admin(
        self,
        request: antdingopensdk_models.UpdateGroupSubAdminRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateGroupSubAdminResponse:
        """
        更新群管理员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateGroupSubAdmin',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/updateGroupSubAdmin',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateGroupSubAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_sub_admin_async(
        self,
        request: antdingopensdk_models.UpdateGroupSubAdminRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateGroupSubAdminResponse:
        """
        更新群管理员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateGroupSubAdmin',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/updateGroupSubAdmin',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateGroupSubAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_member_ban_words(
        self,
        request: antdingopensdk_models.UpdateMemberBanWordsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateMemberBanWordsResponse:
        """
        设置群成员禁言状态
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateMemberBanWords',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/updateMemberBanWords',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateMemberBanWordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_member_ban_words_async(
        self,
        request: antdingopensdk_models.UpdateMemberBanWordsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateMemberBanWordsResponse:
        """
        设置群成员禁言状态
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateMemberBanWords',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/updateMemberBanWords',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateMemberBanWordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_member_group_nick(
        self,
        request: antdingopensdk_models.UpdateMemberGroupNickRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateMemberGroupNickResponse:
        """
        更新群成员的群昵称
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateMemberGroupNick',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/updateMemberGroupNick',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateMemberGroupNickResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_member_group_nick_async(
        self,
        request: antdingopensdk_models.UpdateMemberGroupNickRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateMemberGroupNickResponse:
        """
        更新群成员的群昵称
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateMemberGroupNick',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/updateMemberGroupNick',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateMemberGroupNickResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scenegroup(
        self,
        request: antdingopensdk_models.UpdateScenegroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateScenegroupResponse:
        """
        更新场景群
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateScenegroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/updateScenegroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateScenegroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scenegroup_async(
        self,
        request: antdingopensdk_models.UpdateScenegroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateScenegroupResponse:
        """
        更新场景群
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateScenegroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.ChatService/updateScenegroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateScenegroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_schedule_conference(
        self,
        request: antdingopensdk_models.CancelScheduleConferenceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CancelScheduleConferenceResponse:
        """
        取消预约会议
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='cancelScheduleConference',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/cancelScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CancelScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_schedule_conference_async(
        self,
        request: antdingopensdk_models.CancelScheduleConferenceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CancelScheduleConferenceResponse:
        """
        取消预约会议
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='cancelScheduleConference',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/cancelScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CancelScheduleConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_meeting_room(
        self,
        request: antdingopensdk_models.CreateMeetingRoomRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateMeetingRoomResponse:
        """
        创建会议室
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createMeetingRoom',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/createMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_meeting_room_async(
        self,
        request: antdingopensdk_models.CreateMeetingRoomRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateMeetingRoomResponse:
        """
        创建会议室
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createMeetingRoom',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/createMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateMeetingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_meeting_room_group(
        self,
        request: antdingopensdk_models.CreateMeetingRoomGroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateMeetingRoomGroupResponse:
        """
        创建会议室分组
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createMeetingRoomGroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/createMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_meeting_room_group_async(
        self,
        request: antdingopensdk_models.CreateMeetingRoomGroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateMeetingRoomGroupResponse:
        """
        创建会议室分组
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createMeetingRoomGroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/createMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateMeetingRoomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_schedule_conference(
        self,
        request: antdingopensdk_models.CreateScheduleConferenceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateScheduleConferenceResponse:
        """
        创建预约会议
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createScheduleConference',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/createScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_schedule_conference_async(
        self,
        request: antdingopensdk_models.CreateScheduleConferenceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateScheduleConferenceResponse:
        """
        创建预约会议
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createScheduleConference',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/createScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateScheduleConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_video_conference(
        self,
        request: antdingopensdk_models.CreateVideoConferenceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateVideoConferenceResponse:
        """
        创建视频会议
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createVideoConference',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/createVideoConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateVideoConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_video_conference_async(
        self,
        request: antdingopensdk_models.CreateVideoConferenceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateVideoConferenceResponse:
        """
        创建视频会议
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createVideoConference',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/createVideoConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateVideoConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_meeting_room(
        self,
        request: antdingopensdk_models.DeleteMeetingRoomRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteMeetingRoomResponse:
        """
        删除会议室
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteMeetingRoom',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/deleteMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_meeting_room_async(
        self,
        request: antdingopensdk_models.DeleteMeetingRoomRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteMeetingRoomResponse:
        """
        删除会议室
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteMeetingRoom',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/deleteMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteMeetingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_meeting_room_group(
        self,
        request: antdingopensdk_models.DeleteMeetingRoomGroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteMeetingRoomGroupResponse:
        """
        删除会议室分组
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteMeetingRoomGroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/deleteMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_meeting_room_group_async(
        self,
        request: antdingopensdk_models.DeleteMeetingRoomGroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteMeetingRoomGroupResponse:
        """
        删除会议室分组
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteMeetingRoomGroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/deleteMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteMeetingRoomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invite_users(
        self,
        request: antdingopensdk_models.InviteUsersRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.InviteUsersResponse:
        """
        邀请用户入会
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='inviteUsers',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/inviteUsers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.InviteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def invite_users_async(
        self,
        request: antdingopensdk_models.InviteUsersRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.InviteUsersResponse:
        """
        邀请用户入会
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='inviteUsers',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/inviteUsers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.InviteUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cloud_record_text(
        self,
        request: antdingopensdk_models.QueryCloudRecordTextRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryCloudRecordTextResponse:
        """
        查询会议录制中的文本信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryCloudRecordText',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryCloudRecordText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryCloudRecordTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cloud_record_text_async(
        self,
        request: antdingopensdk_models.QueryCloudRecordTextRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryCloudRecordTextResponse:
        """
        查询会议录制中的文本信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryCloudRecordText',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryCloudRecordText',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryCloudRecordTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cloud_record_video(
        self,
        request: antdingopensdk_models.QueryCloudRecordVideoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryCloudRecordVideoResponse:
        """
        查询会议录制的详情信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryCloudRecordVideo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryCloudRecordVideo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryCloudRecordVideoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cloud_record_video_async(
        self,
        request: antdingopensdk_models.QueryCloudRecordVideoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryCloudRecordVideoResponse:
        """
        查询会议录制的详情信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryCloudRecordVideo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryCloudRecordVideo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryCloudRecordVideoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cloud_record_video_play_info(
        self,
        request: antdingopensdk_models.QueryCloudRecordVideoPlayInfoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryCloudRecordVideoPlayInfoResponse:
        """
        查询会议录制中的视频信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryCloudRecordVideoPlayInfo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryCloudRecordVideoPlayInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryCloudRecordVideoPlayInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cloud_record_video_play_info_async(
        self,
        request: antdingopensdk_models.QueryCloudRecordVideoPlayInfoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryCloudRecordVideoPlayInfoResponse:
        """
        查询会议录制中的视频信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryCloudRecordVideoPlayInfo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryCloudRecordVideoPlayInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryCloudRecordVideoPlayInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_conference_info(
        self,
        request: antdingopensdk_models.QueryConferenceInfoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryConferenceInfoResponse:
        """
        查询视频会议信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryConferenceInfo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryConferenceInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryConferenceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_conference_info_async(
        self,
        request: antdingopensdk_models.QueryConferenceInfoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryConferenceInfoResponse:
        """
        查询视频会议信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryConferenceInfo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryConferenceInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryConferenceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_conference_members(
        self,
        request: antdingopensdk_models.QueryConferenceMembersRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryConferenceMembersResponse:
        """
        查询视频会议成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryConferenceMembers',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryConferenceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryConferenceMembersResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_conference_members_async(
        self,
        request: antdingopensdk_models.QueryConferenceMembersRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryConferenceMembersResponse:
        """
        查询视频会议成员
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryConferenceMembers',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryConferenceMembers',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryConferenceMembersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_meeting_room(
        self,
        request: antdingopensdk_models.QueryMeetingRoomRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryMeetingRoomResponse:
        """
        查询会议室详情
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryMeetingRoom',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_meeting_room_async(
        self,
        request: antdingopensdk_models.QueryMeetingRoomRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryMeetingRoomResponse:
        """
        查询会议室详情
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryMeetingRoom',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryMeetingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_meeting_room_group(
        self,
        request: antdingopensdk_models.QueryMeetingRoomGroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryMeetingRoomGroupResponse:
        """
        查询会议室分组信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryMeetingRoomGroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_meeting_room_group_async(
        self,
        request: antdingopensdk_models.QueryMeetingRoomGroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryMeetingRoomGroupResponse:
        """
        查询会议室分组信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryMeetingRoomGroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryMeetingRoomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_meeting_room_group_list(
        self,
        request: antdingopensdk_models.QueryMeetingRoomGroupListRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryMeetingRoomGroupListResponse:
        """
        查询会议室分组列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryMeetingRoomGroupList',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryMeetingRoomGroupList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryMeetingRoomGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_meeting_room_group_list_async(
        self,
        request: antdingopensdk_models.QueryMeetingRoomGroupListRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryMeetingRoomGroupListResponse:
        """
        查询会议室分组列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryMeetingRoomGroupList',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryMeetingRoomGroupList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryMeetingRoomGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_meeting_room_list(
        self,
        request: antdingopensdk_models.QueryMeetingRoomListRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryMeetingRoomListResponse:
        """
        查询会议室列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryMeetingRoomList',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryMeetingRoomList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryMeetingRoomListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_meeting_room_list_async(
        self,
        request: antdingopensdk_models.QueryMeetingRoomListRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryMeetingRoomListResponse:
        """
        查询会议室列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryMeetingRoomList',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryMeetingRoomList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryMeetingRoomListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_schedule_conference(
        self,
        request: antdingopensdk_models.QueryScheduleConferenceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryScheduleConferenceResponse:
        """
        查询预约会议
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryScheduleConference',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_schedule_conference_async(
        self,
        request: antdingopensdk_models.QueryScheduleConferenceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryScheduleConferenceResponse:
        """
        查询预约会议
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryScheduleConference',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/queryScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryScheduleConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_cloud_record(
        self,
        request: antdingopensdk_models.StartCloudRecordRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.StartCloudRecordResponse:
        """
        开启视频会议云录制
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='startCloudRecord',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/startCloudRecord',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.StartCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_cloud_record_async(
        self,
        request: antdingopensdk_models.StartCloudRecordRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.StartCloudRecordResponse:
        """
        开启视频会议云录制
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='startCloudRecord',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/startCloudRecord',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.StartCloudRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_cloud_record(
        self,
        request: antdingopensdk_models.StopCloudRecordRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.StopCloudRecordResponse:
        """
        停止视频会议云录制
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='stopCloudRecord',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/stopCloudRecord',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.StopCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_cloud_record_async(
        self,
        request: antdingopensdk_models.StopCloudRecordRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.StopCloudRecordResponse:
        """
        停止视频会议云录制
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='stopCloudRecord',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/stopCloudRecord',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.StopCloudRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_meeting_room(
        self,
        request: antdingopensdk_models.UpdateMeetingRoomRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateMeetingRoomResponse:
        """
        更新会议室信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateMeetingRoom',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/updateMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateMeetingRoomResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_meeting_room_async(
        self,
        request: antdingopensdk_models.UpdateMeetingRoomRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateMeetingRoomResponse:
        """
        更新会议室信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateMeetingRoom',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/updateMeetingRoom',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateMeetingRoomResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_meeting_room_group(
        self,
        request: antdingopensdk_models.UpdateMeetingRoomGroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateMeetingRoomGroupResponse:
        """
        更新会议室分组信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateMeetingRoomGroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/updateMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateMeetingRoomGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_meeting_room_group_async(
        self,
        request: antdingopensdk_models.UpdateMeetingRoomGroupRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateMeetingRoomGroupResponse:
        """
        更新会议室分组信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateMeetingRoomGroup',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/updateMeetingRoomGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateMeetingRoomGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schedule_conf_settings(
        self,
        request: antdingopensdk_models.UpdateScheduleConfSettingsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateScheduleConfSettingsResponse:
        """
        更新预约会议设置
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateScheduleConfSettings',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/updateScheduleConfSettings',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateScheduleConfSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schedule_conf_settings_async(
        self,
        request: antdingopensdk_models.UpdateScheduleConfSettingsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateScheduleConfSettingsResponse:
        """
        更新预约会议设置
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateScheduleConfSettings',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/updateScheduleConfSettings',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateScheduleConfSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_schedule_conference(
        self,
        request: antdingopensdk_models.UpdateScheduleConferenceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateScheduleConferenceResponse:
        """
        更新预约会议
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateScheduleConference',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/updateScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateScheduleConferenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_schedule_conference_async(
        self,
        request: antdingopensdk_models.UpdateScheduleConferenceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateScheduleConferenceResponse:
        """
        更新预约会议
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateScheduleConference',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.ConferenceService/updateScheduleConference',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateScheduleConferenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_conversaion_space(
        self,
        request: antdingopensdk_models.GetConversaionSpaceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetConversaionSpaceResponse:
        """
        获取群存储空间信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getConversaionSpace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.ConvFileService/getConversaionSpace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetConversaionSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_conversaion_space_async(
        self,
        request: antdingopensdk_models.GetConversaionSpaceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetConversaionSpaceResponse:
        """
        获取群存储空间信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getConversaionSpace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.ConvFileService/getConversaionSpace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetConversaionSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send(
        self,
        request: antdingopensdk_models.SendRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SendResponse:
        """
        发送文件到指定会话
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='send',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.ConvFileService/send',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SendResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_async(
        self,
        request: antdingopensdk_models.SendRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SendResponse:
        """
        发送文件到指定会话
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='send',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.ConvFileService/send',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_by_app(
        self,
        request: antdingopensdk_models.SendByAppRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SendByAppResponse:
        """
        以应用身份发送文件给指定用户
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='sendByApp',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.ConvFileService/sendByApp',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SendByAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_by_app_async(
        self,
        request: antdingopensdk_models.SendByAppRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SendByAppResponse:
        """
        以应用身份发送文件给指定用户
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='sendByApp',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.ConvFileService/sendByApp',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SendByAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_link(
        self,
        request: antdingopensdk_models.SendLinkRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SendLinkResponse:
        """
        发送文件链接到指定会话
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='sendLink',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.ConvFileService/sendLink',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SendLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_link_async(
        self,
        request: antdingopensdk_models.SendLinkRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SendLinkResponse:
        """
        发送文件链接到指定会话
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='sendLink',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.ConvFileService/sendLink',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SendLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_drive_space(
        self,
        request: antdingopensdk_models.AddDriveSpaceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.AddDriveSpaceResponse:
        """
        新建钉盘空间
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='addDriveSpace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.DriveService/addDriveSpace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.AddDriveSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_drive_space_async(
        self,
        request: antdingopensdk_models.AddDriveSpaceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.AddDriveSpaceResponse:
        """
        新建钉盘空间
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='addDriveSpace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.DriveService/addDriveSpace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.AddDriveSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_drive_space(
        self,
        request: antdingopensdk_models.DeleteDriveSpaceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteDriveSpaceResponse:
        """
        删除钉盘空间
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteDriveSpace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.DriveService/deleteDriveSpace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteDriveSpaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_drive_space_async(
        self,
        request: antdingopensdk_models.DeleteDriveSpaceRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteDriveSpaceResponse:
        """
        删除钉盘空间
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteDriveSpace',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.DriveService/deleteDriveSpace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteDriveSpaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_drive_spaces(
        self,
        request: antdingopensdk_models.ListDriveSpacesRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListDriveSpacesResponse:
        """
        列出空间列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listDriveSpaces',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.DriveService/listDriveSpaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListDriveSpacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_drive_spaces_async(
        self,
        request: antdingopensdk_models.ListDriveSpacesRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListDriveSpacesResponse:
        """
        列出空间列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listDriveSpaces',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.DriveService/listDriveSpaces',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListDriveSpacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_attendee(
        self,
        request: antdingopensdk_models.AddAttendeeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.AddAttendeeResponse:
        """
        添加日程参与者
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='addAttendee',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/addAttendee',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.AddAttendeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_attendee_async(
        self,
        request: antdingopensdk_models.AddAttendeeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.AddAttendeeResponse:
        """
        添加日程参与者
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='addAttendee',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/addAttendee',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.AddAttendeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_meeting_rooms(
        self,
        request: antdingopensdk_models.AddMeetingRoomsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.AddMeetingRoomsResponse:
        """
        预定会议室
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='addMeetingRooms',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/addMeetingRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.AddMeetingRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_meeting_rooms_async(
        self,
        request: antdingopensdk_models.AddMeetingRoomsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.AddMeetingRoomsResponse:
        """
        预定会议室
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='addMeetingRooms',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/addMeetingRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.AddMeetingRoomsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_event(
        self,
        request: antdingopensdk_models.CreateEventRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateEventResponse:
        """
        创建日程
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createEvent',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/createEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_event_async(
        self,
        request: antdingopensdk_models.CreateEventRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateEventResponse:
        """
        创建日程
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createEvent',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/createEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_subscribed_calendar(
        self,
        request: antdingopensdk_models.CreateSubscribedCalendarRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateSubscribedCalendarResponse:
        """
        创建订阅日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createSubscribedCalendar',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/createSubscribedCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateSubscribedCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_subscribed_calendar_async(
        self,
        request: antdingopensdk_models.CreateSubscribedCalendarRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateSubscribedCalendarResponse:
        """
        创建订阅日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createSubscribedCalendar',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/createSubscribedCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateSubscribedCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event(
        self,
        request: antdingopensdk_models.DeleteEventRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteEventResponse:
        """
        删除日程
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteEvent',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/deleteEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_async(
        self,
        request: antdingopensdk_models.DeleteEventRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteEventResponse:
        """
        删除日程
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteEvent',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/deleteEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_subscribed_calendar(
        self,
        request: antdingopensdk_models.DeleteSubscribedCalendarRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteSubscribedCalendarResponse:
        """
        删除订阅日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteSubscribedCalendar',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/deleteSubscribedCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteSubscribedCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_subscribed_calendar_async(
        self,
        request: antdingopensdk_models.DeleteSubscribedCalendarRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteSubscribedCalendarResponse:
        """
        删除订阅日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteSubscribedCalendar',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/deleteSubscribedCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteSubscribedCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event(
        self,
        request: antdingopensdk_models.GetEventRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetEventResponse:
        """
        查询单个日程详情
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getEvent',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/getEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_async(
        self,
        request: antdingopensdk_models.GetEventRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetEventResponse:
        """
        查询单个日程详情
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getEvent',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/getEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_meeting_rooms_schedule(
        self,
        request: antdingopensdk_models.GetMeetingRoomsScheduleRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetMeetingRoomsScheduleResponse:
        """
        获取会议室忙闲信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getMeetingRoomsSchedule',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/getMeetingRoomsSchedule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetMeetingRoomsScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_meeting_rooms_schedule_async(
        self,
        request: antdingopensdk_models.GetMeetingRoomsScheduleRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetMeetingRoomsScheduleResponse:
        """
        获取会议室忙闲信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getMeetingRoomsSchedule',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/getMeetingRoomsSchedule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetMeetingRoomsScheduleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscribed_calendar(
        self,
        request: antdingopensdk_models.GetSubscribedCalendarRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetSubscribedCalendarResponse:
        """
        查询单个订阅日历详情
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getSubscribedCalendar',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/getSubscribedCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetSubscribedCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscribed_calendar_async(
        self,
        request: antdingopensdk_models.GetSubscribedCalendarRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetSubscribedCalendarResponse:
        """
        查询单个订阅日历详情
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getSubscribedCalendar',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/getSubscribedCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetSubscribedCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_calendars(
        self,
        request: antdingopensdk_models.ListCalendarsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListCalendarsResponse:
        """
        查询日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listCalendars',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/listCalendars',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListCalendarsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_calendars_async(
        self,
        request: antdingopensdk_models.ListCalendarsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListCalendarsResponse:
        """
        查询日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listCalendars',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/listCalendars',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListCalendarsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_events(
        self,
        request: antdingopensdk_models.ListEventsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListEventsResponse:
        """
        查询日程列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listEvents',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/listEvents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_events_async(
        self,
        request: antdingopensdk_models.ListEventsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListEventsResponse:
        """
        查询日程列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listEvents',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/listEvents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_events_view(
        self,
        request: antdingopensdk_models.ListEventsViewRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListEventsViewResponse:
        """
        查询日程视图
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listEventsView',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/listEventsView',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListEventsViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_events_view_async(
        self,
        request: antdingopensdk_models.ListEventsViewRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListEventsViewResponse:
        """
        查询日程视图
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listEventsView',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/listEventsView',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListEventsViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def patch_event(
        self,
        request: antdingopensdk_models.PatchEventRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.PatchEventResponse:
        """
        修改日程
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='patchEvent',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/patchEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.PatchEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def patch_event_async(
        self,
        request: antdingopensdk_models.PatchEventRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.PatchEventResponse:
        """
        修改日程
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='patchEvent',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/patchEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.PatchEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_attendee(
        self,
        request: antdingopensdk_models.RemoveAttendeeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.RemoveAttendeeResponse:
        """
        删除日程参与者
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='removeAttendee',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/removeAttendee',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.RemoveAttendeeResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_attendee_async(
        self,
        request: antdingopensdk_models.RemoveAttendeeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.RemoveAttendeeResponse:
        """
        删除日程参与者
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='removeAttendee',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/removeAttendee',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.RemoveAttendeeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_meeting_rooms(
        self,
        request: antdingopensdk_models.RemoveMeetingRoomsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.RemoveMeetingRoomsResponse:
        """
        取消预定会议室
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='removeMeetingRooms',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/removeMeetingRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.RemoveMeetingRoomsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_meeting_rooms_async(
        self,
        request: antdingopensdk_models.RemoveMeetingRoomsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.RemoveMeetingRoomsResponse:
        """
        取消预定会议室
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='removeMeetingRooms',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/removeMeetingRooms',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.RemoveMeetingRoomsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def subscribe_calendar(
        self,
        request: antdingopensdk_models.SubscribeCalendarRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SubscribeCalendarResponse:
        """
        订阅公共日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='subscribeCalendar',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/subscribeCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SubscribeCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def subscribe_calendar_async(
        self,
        request: antdingopensdk_models.SubscribeCalendarRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SubscribeCalendarResponse:
        """
        订阅公共日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='subscribeCalendar',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/subscribeCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SubscribeCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unsubscribe_calendar(
        self,
        request: antdingopensdk_models.UnsubscribeCalendarRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UnsubscribeCalendarResponse:
        """
        取消订阅公共日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='unsubscribeCalendar',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/unsubscribeCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UnsubscribeCalendarResponse(),
            self.call_api(params, req, runtime)
        )

    async def unsubscribe_calendar_async(
        self,
        request: antdingopensdk_models.UnsubscribeCalendarRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UnsubscribeCalendarResponse:
        """
        取消订阅公共日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='unsubscribeCalendar',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/unsubscribeCalendar',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UnsubscribeCalendarResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subscribed_calendars(
        self,
        request: antdingopensdk_models.UpdateSubscribedCalendarsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateSubscribedCalendarsResponse:
        """
        更新订阅日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateSubscribedCalendars',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/updateSubscribedCalendars',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateSubscribedCalendarsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subscribed_calendars_async(
        self,
        request: antdingopensdk_models.UpdateSubscribedCalendarsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateSubscribedCalendarsResponse:
        """
        更新订阅日历
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateSubscribedCalendars',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.calendar.EventService/updateSubscribedCalendars',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateSubscribedCalendarsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def expand_group_capacity(
        self,
        request: antdingopensdk_models.ExpandGroupCapacityRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ExpandGroupCapacityResponse:
        """
        群扩容下单
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='expandGroupCapacity',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.im.GroupService/expandGroupCapacity',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ExpandGroupCapacityResponse(),
            self.call_api(params, req, runtime)
        )

    async def expand_group_capacity_async(
        self,
        request: antdingopensdk_models.ExpandGroupCapacityRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ExpandGroupCapacityResponse:
        """
        群扩容下单
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='expandGroupCapacity',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.im.GroupService/expandGroupCapacity',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ExpandGroupCapacityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_org_honor_template(
        self,
        request: antdingopensdk_models.CreateOrgHonorTemplateRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateOrgHonorTemplateResponse:
        """
        创建荣誉勋章模板
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createOrgHonorTemplate',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/createOrgHonorTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateOrgHonorTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_org_honor_template_async(
        self,
        request: antdingopensdk_models.CreateOrgHonorTemplateRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateOrgHonorTemplateResponse:
        """
        创建荣誉勋章模板
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createOrgHonorTemplate',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/createOrgHonorTemplate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateOrgHonorTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_honor(
        self,
        request: antdingopensdk_models.GrantHonorRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GrantHonorResponse:
        """
        授予勋章
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='grantHonor',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/grantHonor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GrantHonorResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_honor_async(
        self,
        request: antdingopensdk_models.GrantHonorRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GrantHonorResponse:
        """
        授予勋章
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='grantHonor',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/grantHonor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GrantHonorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_org_honors(
        self,
        request: antdingopensdk_models.QueryOrgHonorsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryOrgHonorsResponse:
        """
        查询企业荣誉
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryOrgHonors',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/queryOrgHonors',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryOrgHonorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_org_honors_async(
        self,
        request: antdingopensdk_models.QueryOrgHonorsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryOrgHonorsResponse:
        """
        查询企业荣誉
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryOrgHonors',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/queryOrgHonors',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryOrgHonorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_user_honors(
        self,
        request: antdingopensdk_models.QueryUserHonorsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryUserHonorsResponse:
        """
        查询员工勋章列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryUserHonors',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/queryUserHonors',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryUserHonorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_user_honors_async(
        self,
        request: antdingopensdk_models.QueryUserHonorsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryUserHonorsResponse:
        """
        查询员工勋章列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryUserHonors',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/queryUserHonors',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryUserHonorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recall_honor(
        self,
        request: antdingopensdk_models.RecallHonorRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.RecallHonorResponse:
        """
        收回勋章
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='recallHonor',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/recallHonor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.RecallHonorResponse(),
            self.call_api(params, req, runtime)
        )

    async def recall_honor_async(
        self,
        request: antdingopensdk_models.RecallHonorRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.RecallHonorResponse:
        """
        收回勋章
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='recallHonor',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/recallHonor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.RecallHonorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def wear_org_honor(
        self,
        request: antdingopensdk_models.WearOrgHonorRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.WearOrgHonorResponse:
        """
        穿戴勋章
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='wearOrgHonor',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/wearOrgHonor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.WearOrgHonorResponse(),
            self.call_api(params, req, runtime)
        )

    async def wear_org_honor_async(
        self,
        request: antdingopensdk_models.WearOrgHonorRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.WearOrgHonorResponse:
        """
        穿戴勋章
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='wearOrgHonor',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.honor.HonorService/wearOrgHonor',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.WearOrgHonorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_live(
        self,
        request: antdingopensdk_models.CreateLiveRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateLiveResponse:
        """
        创建直播ID 接口调用流程 步骤一：调用本接口，获取直播ID。 步骤二：使用直播ID，拼接以下链接：
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createLive',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/createLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_live_async(
        self,
        request: antdingopensdk_models.CreateLiveRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateLiveResponse:
        """
        创建直播ID 接口调用流程 步骤一：调用本接口，获取直播ID。 步骤二：使用直播ID，拼接以下链接：
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createLive',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/createLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_live(
        self,
        request: antdingopensdk_models.DeleteLiveRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteLiveResponse:
        """
        删除直播ID 调用本接口，根据直播ID删除直播。 调用本接口，删除直播。 如果直播未发起，调用本接口删除后，直播不能正常发起。
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteLive',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/deleteLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_live_async(
        self,
        request: antdingopensdk_models.DeleteLiveRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteLiveResponse:
        """
        删除直播ID 调用本接口，根据直播ID删除直播。 调用本接口，删除直播。 如果直播未发起，调用本接口删除后，直播不能正常发起。
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteLive',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/deleteLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_live_replay_url(
        self,
        request: antdingopensdk_models.GetLiveReplayUrlRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetLiveReplayUrlResponse:
        """
        获取直播的可下载回放地址
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getLiveReplayUrl',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/getLiveReplayUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetLiveReplayUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_live_replay_url_async(
        self,
        request: antdingopensdk_models.GetLiveReplayUrlRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetLiveReplayUrlResponse:
        """
        获取直播的可下载回放地址
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getLiveReplayUrl',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/getLiveReplayUrl',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetLiveReplayUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_live_info(
        self,
        request: antdingopensdk_models.QueryLiveInfoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryLiveInfoResponse:
        """
        查询直播信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryLiveInfo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/queryLiveInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryLiveInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_live_info_async(
        self,
        request: antdingopensdk_models.QueryLiveInfoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryLiveInfoResponse:
        """
        查询直播信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryLiveInfo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/queryLiveInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryLiveInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_live_watch_detail(
        self,
        request: antdingopensdk_models.QueryLiveWatchDetailRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryLiveWatchDetailResponse:
        """
        查询直播的观看数据
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryLiveWatchDetail',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/queryLiveWatchDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryLiveWatchDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_live_watch_detail_async(
        self,
        request: antdingopensdk_models.QueryLiveWatchDetailRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryLiveWatchDetailResponse:
        """
        查询直播的观看数据
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryLiveWatchDetail',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/queryLiveWatchDetail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryLiveWatchDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_live_watch_user_list(
        self,
        request: antdingopensdk_models.QueryLiveWatchUserListRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryLiveWatchUserListResponse:
        """
        查询直播观看人员信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryLiveWatchUserList',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/queryLiveWatchUserList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryLiveWatchUserListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_live_watch_user_list_async(
        self,
        request: antdingopensdk_models.QueryLiveWatchUserListRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryLiveWatchUserListResponse:
        """
        查询直播观看人员信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryLiveWatchUserList',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/queryLiveWatchUserList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryLiveWatchUserListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_live(
        self,
        request: antdingopensdk_models.UpdateLiveRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateLiveResponse:
        """
        修改直播属性信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateLive',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/updateLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateLiveResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_live_async(
        self,
        request: antdingopensdk_models.UpdateLiveRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateLiveResponse:
        """
        修改直播属性信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateLive',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.ysp.LiveService/updateLive',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateLiveResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_media(
        self,
        request: antdingopensdk_models.UploadMediaRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UploadMediaResponse:
        """
        上传媒体<br>
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='uploadMedia',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.document.MediaService/uploadMedia',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UploadMediaResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_media_async(
        self,
        request: antdingopensdk_models.UploadMediaRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UploadMediaResponse:
        """
        上传媒体<br>
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='uploadMedia',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.document.MediaService/uploadMedia',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UploadMediaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_batch_dept_ids(
        self,
        request: antdingopensdk_models.GetBatchDeptIdsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetBatchDeptIdsResponse:
        """
        根据deptNo转为deptList，根据deptNo转换为DeptId,用于成员管理、权限管理、发布版本的部门迁移。 21001 和 688688
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getBatchDeptIds',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.rpc.MigrateDingAppService/getBatchDeptIds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetBatchDeptIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_batch_dept_ids_async(
        self,
        request: antdingopensdk_models.GetBatchDeptIdsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetBatchDeptIdsResponse:
        """
        根据deptNo转为deptList，根据deptNo转换为DeptId,用于成员管理、权限管理、发布版本的部门迁移。 21001 和 688688
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getBatchDeptIds',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.rpc.MigrateDingAppService/getBatchDeptIds',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetBatchDeptIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def on_call(
        self,
        request: antdingopensdk_models.OnCallRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.OnCallResponse:
        """
        回调方法
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='onCall',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.fc.process.common.service.facade.callback.ProcessCallback/onCall',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.OnCallResponse(),
            self.call_api(params, req, runtime)
        )

    async def on_call_async(
        self,
        request: antdingopensdk_models.OnCallRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.OnCallResponse:
        """
        回调方法
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='onCall',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.fc.process.common.service.facade.callback.ProcessCallback/onCall',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.OnCallResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def comment_list_report(
        self,
        request: antdingopensdk_models.CommentListReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CommentListReportResponse:
        """
        获取日志评论列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='commentListReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/commentListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CommentListReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def comment_list_report_async(
        self,
        request: antdingopensdk_models.CommentListReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CommentListReportResponse:
        """
        获取日志评论列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='commentListReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/commentListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CommentListReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_report(
        self,
        request: antdingopensdk_models.CreateReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateReportResponse:
        """
        创建日志 说明 调用本接口创建日志，对应日志模板中的每个组件只允许是文本类型，其他类型组件暂不支持接口调用
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/createReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_report_async(
        self,
        request: antdingopensdk_models.CreateReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateReportResponse:
        """
        创建日志 说明 调用本接口创建日志，对应日志模板中的每个组件只允许是文本类型，其他类型组件暂不支持接口调用
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/createReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_report_template_by_name(
        self,
        request: antdingopensdk_models.GetReportTemplateByNameRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetReportTemplateByNameResponse:
        """
        获取模板详情
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getReportTemplateByName',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/getReportTemplateByName',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetReportTemplateByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_report_template_by_name_async(
        self,
        request: antdingopensdk_models.GetReportTemplateByNameRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetReportTemplateByNameResponse:
        """
        获取模板详情
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getReportTemplateByName',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/getReportTemplateByName',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetReportTemplateByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_report_un_read_count(
        self,
        request: antdingopensdk_models.GetReportUnReadCountRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetReportUnReadCountResponse:
        """
        获取员工有多少数量的日志（一个月内）是未读状态
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getReportUnReadCount',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/getReportUnReadCount',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetReportUnReadCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_report_un_read_count_async(
        self,
        request: antdingopensdk_models.GetReportUnReadCountRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetReportUnReadCountResponse:
        """
        获取员工有多少数量的日志（一个月内）是未读状态
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getReportUnReadCount',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/getReportUnReadCount',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetReportUnReadCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_list_by_user_id(
        self,
        request: antdingopensdk_models.GetTemplateListByUserIdRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetTemplateListByUserIdResponse:
        """
        获取用户可见的日志模板
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getTemplateListByUserId',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/getTemplateListByUserId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetTemplateListByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_list_by_user_id_async(
        self,
        request: antdingopensdk_models.GetTemplateListByUserIdRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetTemplateListByUserIdResponse:
        """
        获取用户可见的日志模板
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getTemplateListByUserId',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/getTemplateListByUserId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetTemplateListByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_report(
        self,
        request: antdingopensdk_models.ListReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListReportResponse:
        """
        获取用户发出的日志列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/listReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_report_async(
        self,
        request: antdingopensdk_models.ListReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListReportResponse:
        """
        获取用户发出的日志列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/listReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def receiver_list_report(
        self,
        request: antdingopensdk_models.ReceiverListReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ReceiverListReportResponse:
        """
        获取日志接收人员列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='receiverListReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/receiverListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ReceiverListReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def receiver_list_report_async(
        self,
        request: antdingopensdk_models.ReceiverListReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ReceiverListReportResponse:
        """
        获取日志接收人员列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='receiverListReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/receiverListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ReceiverListReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_content(
        self,
        request: antdingopensdk_models.SaveContentRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SaveContentResponse:
        """
        保存日志内容
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='saveContent',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/saveContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SaveContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_content_async(
        self,
        request: antdingopensdk_models.SaveContentRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SaveContentResponse:
        """
        保存日志内容
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='saveContent',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/saveContent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SaveContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def simple_list_report(
        self,
        request: antdingopensdk_models.SimpleListReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SimpleListReportResponse:
        """
        获取用户发送日志的概要信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='simpleListReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/simpleListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SimpleListReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def simple_list_report_async(
        self,
        request: antdingopensdk_models.SimpleListReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SimpleListReportResponse:
        """
        获取用户发送日志的概要信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='simpleListReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/simpleListReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SimpleListReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def statistics_list_by_type_report(
        self,
        request: antdingopensdk_models.StatisticsListByTypeReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.StatisticsListByTypeReportResponse:
        """
        获取日志相关人员列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='statisticsListByTypeReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/statisticsListByTypeReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.StatisticsListByTypeReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def statistics_list_by_type_report_async(
        self,
        request: antdingopensdk_models.StatisticsListByTypeReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.StatisticsListByTypeReportResponse:
        """
        获取日志相关人员列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='statisticsListByTypeReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/statisticsListByTypeReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.StatisticsListByTypeReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def statistics_report(
        self,
        request: antdingopensdk_models.StatisticsReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.StatisticsReportResponse:
        """
        获取日志统计数据
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='statisticsReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/statisticsReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.StatisticsReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def statistics_report_async(
        self,
        request: antdingopensdk_models.StatisticsReportRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.StatisticsReportResponse:
        """
        获取日志统计数据
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='statisticsReport',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.log.ReportService/statisticsReport',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.StatisticsReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_send_oto(
        self,
        request: antdingopensdk_models.BatchSendOTORequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.BatchSendOTOResponse:
        """
        批量发送人与机器人会话中机器人消息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='batchSendOTO',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.RobotService/batchSendOTO',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.BatchSendOTOResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_send_oto_async(
        self,
        request: antdingopensdk_models.BatchSendOTORequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.BatchSendOTOResponse:
        """
        批量发送人与机器人会话中机器人消息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='batchSendOTO',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.RobotService/batchSendOTO',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.BatchSendOTOResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_url_to_media_id(
        self,
        request: antdingopensdk_models.TransferUrlToMediaIdRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.TransferUrlToMediaIdResponse:
        """
        转化 url 为 mediaId
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='transferUrlToMediaId',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.RobotService/transferUrlToMediaId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.TransferUrlToMediaIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_url_to_media_id_async(
        self,
        request: antdingopensdk_models.TransferUrlToMediaIdRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.TransferUrlToMediaIdResponse:
        """
        转化 url 为 mediaId
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='transferUrlToMediaId',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.im.RobotService/transferUrlToMediaId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.TransferUrlToMediaIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_push_scene(
        self,
        request: antdingopensdk_models.QueryRobotPushSceneRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryRobotPushSceneResponse:
        """
        查询机器人推送场景
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryRobotPushScene',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.robot.RobotSubscribeService/queryRobotPushScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryRobotPushSceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_push_scene_async(
        self,
        request: antdingopensdk_models.QueryRobotPushSceneRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryRobotPushSceneResponse:
        """
        查询机器人推送场景
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryRobotPushScene',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.robot.RobotSubscribeService/queryRobotPushScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryRobotPushSceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_unsubscription(
        self,
        request: antdingopensdk_models.QueryRobotUnsubscriptionRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryRobotUnsubscriptionResponse:
        """
        分页查询钉钉机器人退订工号
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryRobotUnsubscription',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.robot.RobotSubscribeService/queryRobotUnsubscription',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryRobotUnsubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_unsubscription_async(
        self,
        request: antdingopensdk_models.QueryRobotUnsubscriptionRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryRobotUnsubscriptionResponse:
        """
        分页查询钉钉机器人退订工号
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryRobotUnsubscription',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.aliding.v1.robot.RobotSubscribeService/queryRobotUnsubscription',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryRobotUnsubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_one_key_un_subscribe_staff_id(
        self,
        request: antdingopensdk_models.QueryOneKeyUnSubscribeStaffIdRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryOneKeyUnSubscribeStaffIdResponse:
        """
        查询钉钉机器人退订信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryOneKeyUnSubscribeStaffId',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.management.service.robot.RobotSubscriptionService/queryOneKeyUnSubscribeStaffId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryOneKeyUnSubscribeStaffIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_one_key_un_subscribe_staff_id_async(
        self,
        request: antdingopensdk_models.QueryOneKeyUnSubscribeStaffIdRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryOneKeyUnSubscribeStaffIdResponse:
        """
        查询钉钉机器人退订信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryOneKeyUnSubscribeStaffId',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.management.service.robot.RobotSubscriptionService/queryOneKeyUnSubscribeStaffId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryOneKeyUnSubscribeStaffIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_robot_owner(
        self,
        request: antdingopensdk_models.QueryRobotOwnerRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryRobotOwnerResponse:
        """
        查询机器人Owner
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryRobotOwner',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.management.service.robot.RobotSubscriptionService/queryRobotOwner',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryRobotOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_robot_owner_async(
        self,
        request: antdingopensdk_models.QueryRobotOwnerRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryRobotOwnerResponse:
        """
        查询机器人Owner
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryRobotOwner',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.management.service.robot.RobotSubscriptionService/queryRobotOwner',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryRobotOwnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_subscribe_by_user(
        self,
        request: antdingopensdk_models.QuerySubscribeByUserRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QuerySubscribeByUserResponse:
        """
        根据用户查询未订阅场景列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='querySubscribeByUser',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.management.service.robot.RobotSubscriptionService/querySubscribeByUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QuerySubscribeByUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_subscribe_by_user_async(
        self,
        request: antdingopensdk_models.QuerySubscribeByUserRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QuerySubscribeByUserResponse:
        """
        根据用户查询未订阅场景列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='querySubscribeByUser',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.management.service.robot.RobotSubscriptionService/querySubscribeByUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QuerySubscribeByUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_un_subscribe_staff_id_by_scene(
        self,
        request: antdingopensdk_models.QueryUnSubscribeStaffIdBySceneRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryUnSubscribeStaffIdBySceneResponse:
        """
        按照场景查询当前场景退订员工工号
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryUnSubscribeStaffIdByScene',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.management.service.robot.RobotSubscriptionService/queryUnSubscribeStaffIdByScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryUnSubscribeStaffIdBySceneResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_un_subscribe_staff_id_by_scene_async(
        self,
        request: antdingopensdk_models.QueryUnSubscribeStaffIdBySceneRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryUnSubscribeStaffIdBySceneResponse:
        """
        按照场景查询当前场景退订员工工号
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryUnSubscribeStaffIdByScene',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.management.service.robot.RobotSubscriptionService/queryUnSubscribeStaffIdByScene',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryUnSubscribeStaffIdBySceneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def user_subscribe(
        self,
        request: antdingopensdk_models.UserSubscribeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UserSubscribeResponse:
        """
        用户订阅
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='userSubscribe',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.management.service.robot.RobotSubscriptionService/userSubscribe',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UserSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def user_subscribe_async(
        self,
        request: antdingopensdk_models.UserSubscribeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UserSubscribeResponse:
        """
        用户订阅
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='userSubscribe',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.management.service.robot.RobotSubscriptionService/userSubscribe',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UserSubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def hello(
        self,
        request: antdingopensdk_models.HelloRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.HelloResponse:
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='hello',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.rpc.SampleService/hello',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.HelloResponse(),
            self.call_api(params, req, runtime)
        )

    async def hello_async(
        self,
        request: antdingopensdk_models.HelloRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.HelloResponse:
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='hello',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.rpc.SampleService/hello',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.HelloResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_file_download_info(
        self,
        request: antdingopensdk_models.GetFileDownloadInfoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetFileDownloadInfoResponse:
        """
        获取文件下载信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getFileDownloadInfo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.StorageService/getFileDownloadInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetFileDownloadInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_file_download_info_async(
        self,
        request: antdingopensdk_models.GetFileDownloadInfoRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetFileDownloadInfoResponse:
        """
        获取文件下载信息
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getFileDownloadInfo',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.StorageService/getFileDownloadInfo',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetFileDownloadInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dentries(
        self,
        request: antdingopensdk_models.ListDentriesRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListDentriesResponse:
        """
        获取文件或文件夹列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listDentries',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.StorageService/listDentries',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListDentriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dentries_async(
        self,
        request: antdingopensdk_models.ListDentriesRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ListDentriesResponse:
        """
        获取文件或文件夹列表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='listDentries',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.StorageService/listDentries',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ListDentriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_personal_todo_task(
        self,
        request: antdingopensdk_models.CreatePersonalTodoTaskRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreatePersonalTodoTaskResponse:
        """
        创建钉钉个人待办任务
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createPersonalTodoTask',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/createPersonalTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreatePersonalTodoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_personal_todo_task_async(
        self,
        request: antdingopensdk_models.CreatePersonalTodoTaskRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreatePersonalTodoTaskResponse:
        """
        创建钉钉个人待办任务
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createPersonalTodoTask',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/createPersonalTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreatePersonalTodoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_todo_task(
        self,
        request: antdingopensdk_models.CreateTodoTaskRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateTodoTaskResponse:
        """
        创建代办
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createTodoTask',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/createTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateTodoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_todo_task_async(
        self,
        request: antdingopensdk_models.CreateTodoTaskRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateTodoTaskResponse:
        """
        创建代办
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createTodoTask',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/createTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateTodoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_todo_task(
        self,
        request: antdingopensdk_models.DeleteTodoTaskRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteTodoTaskResponse:
        """
        删除代办
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteTodoTask',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/deleteTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteTodoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_todo_task_async(
        self,
        request: antdingopensdk_models.DeleteTodoTaskRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteTodoTaskResponse:
        """
        删除代办
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteTodoTask',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/deleteTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteTodoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_org_todo_tasks(
        self,
        request: antdingopensdk_models.QueryOrgTodoTasksRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryOrgTodoTasksResponse:
        """
        查询企业代办
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryOrgTodoTasks',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/queryOrgTodoTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryOrgTodoTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_org_todo_tasks_async(
        self,
        request: antdingopensdk_models.QueryOrgTodoTasksRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.QueryOrgTodoTasksResponse:
        """
        查询企业代办
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='queryOrgTodoTasks',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/queryOrgTodoTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.QueryOrgTodoTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_todo_task(
        self,
        request: antdingopensdk_models.UpdateTodoTaskRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateTodoTaskResponse:
        """
        更新代办
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateTodoTask',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/updateTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateTodoTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_todo_task_async(
        self,
        request: antdingopensdk_models.UpdateTodoTaskRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateTodoTaskResponse:
        """
        更新代办
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateTodoTask',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/updateTodoTask',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateTodoTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_todo_task_executor_status(
        self,
        request: antdingopensdk_models.UpdateTodoTaskExecutorStatusRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateTodoTaskExecutorStatusResponse:
        """
        更新代办执行者状态
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateTodoTaskExecutorStatus',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/updateTodoTaskExecutorStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateTodoTaskExecutorStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_todo_task_executor_status_async(
        self,
        request: antdingopensdk_models.UpdateTodoTaskExecutorStatusRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateTodoTaskExecutorStatusResponse:
        """
        更新代办执行者状态
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateTodoTaskExecutorStatus',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.task.TodoTaskService/updateTodoTaskExecutorStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateTodoTaskExecutorStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear(
        self,
        request: antdingopensdk_models.ClearRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ClearResponse:
        """
        清除单元格所有内容
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='clear',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/clear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ClearResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_async(
        self,
        request: antdingopensdk_models.ClearRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ClearResponse:
        """
        清除单元格所有内容
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='clear',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/clear',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ClearResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clear_data(
        self,
        request: antdingopensdk_models.ClearDataRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ClearDataResponse:
        """
        清除单元格数据
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='clearData',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/clearData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ClearDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def clear_data_async(
        self,
        request: antdingopensdk_models.ClearDataRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.ClearDataResponse:
        """
        清除单元格数据
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='clearData',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/clearData',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.ClearDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_sheet(
        self,
        request: antdingopensdk_models.CreateSheetRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateSheetResponse:
        """
        创建工作表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createSheet',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/createSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateSheetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_sheet_async(
        self,
        request: antdingopensdk_models.CreateSheetRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.CreateSheetResponse:
        """
        创建工作表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='createSheet',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/createSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.CreateSheetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_columns(
        self,
        request: antdingopensdk_models.DeleteColumnsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteColumnsResponse:
        """
        删除指定列
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteColumns',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/deleteColumns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_columns_async(
        self,
        request: antdingopensdk_models.DeleteColumnsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteColumnsResponse:
        """
        删除指定列
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteColumns',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/deleteColumns',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rows(
        self,
        request: antdingopensdk_models.DeleteRowsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteRowsResponse:
        """
        删除指定行
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteRows',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/deleteRows',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteRowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rows_async(
        self,
        request: antdingopensdk_models.DeleteRowsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteRowsResponse:
        """
        删除指定行
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteRows',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/deleteRows',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteRowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sheet(
        self,
        request: antdingopensdk_models.DeleteSheetRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteSheetResponse:
        """
        删除一个工作表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteSheet',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/deleteSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteSheetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sheet_async(
        self,
        request: antdingopensdk_models.DeleteSheetRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.DeleteSheetResponse:
        """
        删除一个工作表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='deleteSheet',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/deleteSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.DeleteSheetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_all_sheets(
        self,
        request: antdingopensdk_models.GetAllSheetsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetAllSheetsResponse:
        """
        获取所有工作表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getAllSheets',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/getAllSheets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetAllSheetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_all_sheets_async(
        self,
        request: antdingopensdk_models.GetAllSheetsRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetAllSheetsResponse:
        """
        获取所有工作表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getAllSheets',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/getAllSheets',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetAllSheetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_range(
        self,
        request: antdingopensdk_models.GetRangeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetRangeResponse:
        """
        获取单元格区域
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getRange',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/getRange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_range_async(
        self,
        request: antdingopensdk_models.GetRangeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetRangeResponse:
        """
        获取单元格区域
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getRange',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/getRange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sheet(
        self,
        request: antdingopensdk_models.GetSheetRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetSheetResponse:
        """
        获取工作表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getSheet',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/getSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetSheetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sheet_async(
        self,
        request: antdingopensdk_models.GetSheetRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.GetSheetResponse:
        """
        获取工作表
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='getSheet',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/getSheet',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.GetSheetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_columns_before(
        self,
        request: antdingopensdk_models.InsertColumnsBeforeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.InsertColumnsBeforeResponse:
        """
        在指定列左侧插入若干列
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='insertColumnsBefore',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/insertColumnsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.InsertColumnsBeforeResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_columns_before_async(
        self,
        request: antdingopensdk_models.InsertColumnsBeforeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.InsertColumnsBeforeResponse:
        """
        在指定列左侧插入若干列
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='insertColumnsBefore',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/insertColumnsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.InsertColumnsBeforeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_rows_before(
        self,
        request: antdingopensdk_models.InsertRowsBeforeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.InsertRowsBeforeResponse:
        """
        在指定行上方插入若干行
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='insertRowsBefore',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/insertRowsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.InsertRowsBeforeResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_rows_before_async(
        self,
        request: antdingopensdk_models.InsertRowsBeforeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.InsertRowsBeforeResponse:
        """
        在指定行上方插入若干行
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='insertRowsBefore',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/insertRowsBefore',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.InsertRowsBeforeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_columns_visibility(
        self,
        request: antdingopensdk_models.SetColumnsVisibilityRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SetColumnsVisibilityResponse:
        """
        指定列隐藏
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='setColumnsVisibility',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/setColumnsVisibility',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SetColumnsVisibilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_columns_visibility_async(
        self,
        request: antdingopensdk_models.SetColumnsVisibilityRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SetColumnsVisibilityResponse:
        """
        指定列隐藏
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='setColumnsVisibility',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/setColumnsVisibility',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SetColumnsVisibilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_rows_visibility(
        self,
        request: antdingopensdk_models.SetRowsVisibilityRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SetRowsVisibilityResponse:
        """
        指定行隐藏
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='setRowsVisibility',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/setRowsVisibility',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SetRowsVisibilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_rows_visibility_async(
        self,
        request: antdingopensdk_models.SetRowsVisibilityRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.SetRowsVisibilityResponse:
        """
        指定行隐藏
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='setRowsVisibility',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/setRowsVisibility',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.SetRowsVisibilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_range(
        self,
        request: antdingopensdk_models.UpdateRangeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateRangeResponse:
        """
        更新单元格区域
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateRange',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/updateRange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateRangeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_range_async(
        self,
        request: antdingopensdk_models.UpdateRangeRequest,
        header_context: antdingopensdk_models.HttpHeader,
        runtime: util_models.RuntimeOptions,
    ) -> antdingopensdk_models.UpdateRangeResponse:
        """
        更新单元格区域
        """
        UtilClient.validate_model(request)
        headers = header_context.header
        headers['x-webgw-appId'] = self._webgw_app_id
        headers['x-webgw-secret'] = self._webgw_secret
        headers['x-webgw-version'] = self._webgw_version
        account_context_temp = antdingopensdk_models.AccountContext(
            account_id=header_context.account.account_id
        )
        amp_context_temp = antdingopensdk_models.AmpContext(
            access_key_id=self._access_key_id
        )
        context = antdingopensdk_models.GatewayContext(
            account_context=account_context_temp,
            amp_context=amp_context_temp,
            access_key_id=self._access_key_id
        )
        time = OpenApiUtilClient.get_timestamp()
        request_sign = f'{UtilClient.to_jsonstring(request)}__{self._access_key_secret}__{time}'
        hashed_request_payload = OpenApiUtilClient.hex_encode(OpenApiUtilClient.hash(UtilClient.to_bytes(request_sign), 'ACS3-HMAC-SHA256'))
        headers['X-Webgw-Sofa-Baggage-SIGN'] = hashed_request_payload
        headers['X-Webgw-Sofa-Baggage-SIGNTIME'] = time
        headers['X-Webgw-Sofa-Baggage-Sdkversion'] = self._sdk_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=f'[{UtilClient.to_jsonstring(context)},{UtilClient.to_jsonstring(request)}]'
        )
        params = open_api_models.Params(
            action='updateRange',
            version='2020-02-06',
            protocol='HTTPS',
            pathname=f'/antdingopen/com.alipay.antdingopen.facade.openapi.vendor.dingtalk.v1.documents.WorkbooksService/updateRange',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antdingopensdk_models.UpdateRangeResponse(),
            await self.call_api_async(params, req, runtime)
        )
