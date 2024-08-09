from typing import Any, Dict, List, Optional, Tuple, Union

import requests
from keystoneauth1 import adapter, session  # type: ignore
from troveclient.auth_plugin import BaseAuthPlugin
from troveclient.v1 import client

class TroveClientMixin(object):
    def get_database_api_version_from_endpoint(self) -> str: ...

class HTTPClient(TroveClientMixin):
    def __init__(
        self,
        user: str,
        password: str,
        projectid: str,
        auth_url: str,
        insecure: bool = False,
        timeout: Optional[int] = None,
        tenant_id: Optional[str] = None,
        proxy_tenant_id: Optional[str] = None,
        proxy_token: Optional[str] = None,
        region_name: Optional[str] = None,
        endpoint_type: str = "publicURL",
        service_type: Optional[str] = None,
        service_name: Optional[str] = None,
        database_service_name: Optional[str] = None,
        retries: Optional[int] = None,
        http_log_debug: bool = False,
        cacert=None,
        bypass_url: Optional[str] = None,
        auth_system: str = "keystone",
        auth_plugin: Optional[BaseAuthPlugin] = None,
    ): ...
    def http_log_req(self, args: List[Any], kwargs: Dict[Any, Any]): ...
    def http_log_resp(self, resp: requests.Response): ...
    def request(
        self, url: str, method: str, **kwargs
    ) -> Tuple[requests.Response, Dict]: ...
    def _cs_request(
        self, url: str, method: str, **kwargs
    ) -> Tuple[requests.Response, Dict]: ...
    def get(self, url: str, **kwargs) -> Tuple[requests.Response, Dict]: ...
    def patch(self, url: str, **kwargs) -> Tuple[requests.Response, Dict]: ...
    def post(self, url: str, **kwargs) -> Tuple[requests.Response, Dict]: ...
    def put(self, url: str, **kwargs) -> Tuple[requests.Response, Dict]: ...
    def delete(self, url: str, **kwargs) -> Tuple[requests.Response, Dict]: ...
    def _extract_service_catalog(
        self, url: str, resp: requests.Response, body: Dict, extract_token: bool = True
    ) -> Optional[str]: ...
    def _fetch_endpoints_from_auth(self, url: str) -> Optional[str]: ...
    def _plugin_auth(self, auth_url: str) -> Any: ...
    def _v1_auth(self, url: str) -> Optional[str]: ...
    def _v2_auth(self, url: str): ...
    def _authenticate(self, url: str, body: Dict) -> Optional[str]: ...

class SessionClient(adapter.LegacyJsonAdapter, TroveClientMixin):
    def __init__(self, session: session.Session, auth: Any, **kwargs): ...
    def request(
        self, url: str, method: str, **kwargs
    ) -> Tuple[requests.Response, Dict]: ...

def _construct_http_client(
    username: Optional[str] = None,
    password: Optional[str] = None,
    project_id: Optional[str] = None,
    auth_url: Optional[str] = None,
    insecure: bool = False,
    timeout: Optional[int] = None,
    proxy_tenant_id: Optional[str] = None,
    proxy_token: Optional[str] = None,
    region_name: Optional[str] = None,
    endpoint_type: str = "publicURL",
    service_type: str = "database",
    service_name: Optional[str] = None,
    database_service_name: Optional[str] = None,
    retries: Optional[int] = None,
    http_log_debug: bool = False,
    auth_system: str = "keystone",
    auth_plugin: Optional[BaseAuthPlugin] = None,
    cacert=None,
    bypass_url: Optional[str] = None,
    tenant_id: Optional[str] = None,
    session: session.Session = None,
    **kwargs
) -> Union[HTTPClient, SessionClient]: ...
def get_version_map() -> Dict[str, str]: ...
def Client(version: str, *args, **kwargs) -> client.Client: ...
