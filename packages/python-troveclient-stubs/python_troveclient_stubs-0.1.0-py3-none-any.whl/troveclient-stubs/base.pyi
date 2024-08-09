import abc
from typing import Any, Dict, List, Optional, Tuple, Type, TypeVar, Union

import requests
from troveclient import utils
from troveclient.apiclient import base

T = TypeVar("T")

def getid(obj: Any) -> Union[str, Any]: ...

class Manager(utils.HookableMixin):
    resource_class: Optional[Type[Any]]

    def __init__(self, api): ...
    def _paginated(
        self,
        url: str,
        response_key: str,
        limit: Optional[int] = None,
        marker=None,
        query_strings: Optional[Dict] = None,
    ): ...
    def _list(
        self,
        url: str,
        response_key: str,
        obj_class: Optional[Type[T]] = None,
        body: Optional[Dict] = None,
    ) -> Union[List[T], List[Any]]: ...
    def _get(self, url: str, response_key: Optional[str] = None): ...
    def _create(
        self,
        url: str,
        body: Dict,
        response_key: str,
        return_raw: bool = False,
        **kwargs
    ): ...
    def _delete(self, url: str) -> Tuple[requests.Response, Dict]: ...
    def _update(self, url: str, body: Dict, **kwargs) -> Dict: ...
    def _edit(self, url: str, body: Dict) -> Dict: ...

class ManagerWithFind(Manager, metaclass=abc.ABCMeta):
    def find(self, **kwargs) -> Any: ...
    def findall(self, **kwargs) -> List[Any]: ...

class Resource(base.Resource):
    def __init__(self, manager: Manager, info: Dict, loaded: bool = False): ...
