from typing import Dict, Optional

class ServiceCatalog(object):
    def __init__(self, resource_dict: Dict) -> None: ...
    def get_token(self) -> str: ...
    def url_for(
        self,
        attr: Optional[str] = None,
        filter_value: Optional[str] = None,
        service_type: Optional[str] = None,
        endpoint_type: str = "publicURL",
        service_name: Optional[str] = None,
        database_service_name: Optional[str] = None,
    ): ...
