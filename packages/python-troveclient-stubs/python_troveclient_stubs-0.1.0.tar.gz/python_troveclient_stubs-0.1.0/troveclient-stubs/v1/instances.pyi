from typing import Any, Dict, List, Literal, Optional, Type, TypedDict, Union

from swiftclient import client as swift_client  # type: ignore
from troveclient import base

class Access(TypedDict):
    is_public: Optional[bool]
    allowed_cidrs: Optional[List[str]]

class Datastore(TypedDict):
    type: str
    version: str
    version_number: str

class Volume(TypedDict):
    size: int
    used: float

class Address(TypedDict):
    network: Optional[str]
    address: str
    type: Literal["private"] | Literal["public"]

class Flavor(TypedDict):
    id: str
    name: str
    description: Optional[str]
    links: list[Link]

class Link(TypedDict):
    href: str
    rel: str

class Instance(base.Resource):
    id: str
    name: str
    status: (
        Literal["ACTIVE"]
        | Literal["BLOCKED"]
        | Literal["BUILD"]
        | Literal["FAILED"]
        | Literal["REBOOT"]
        | Literal["RESIZE"]
        | Literal["SHUTDOWN"]
        | Literal["RESTART_REQUIRED"]
        | Literal["PROMOTING"]
        | Literal["EJECTING"]
        | Literal["LOGGING"]
    )
    access: Access
    addresses: list[Address]
    datastore: Datastore
    flavor: Flavor
    links: list[Link]
    operating_status: str
    region: str
    volume: Volume
    created: str
    updated: str
    service_status_updated: str

    def list_databases(self) -> List[Any]: ...  # TODO: Add database type
    def delete(self) -> None: ...
    def force_delete(self) -> None: ...
    def restart(self) -> None: ...
    def detach_replica(self) -> None: ...

class DatastoreLog(base.Resource): ...

class Database(TypedDict):
    name: str

class User(TypedDict):
    name: str
    password: str
    databases: List[Database]

class RestorePoint(TypedDict):
    backupRef: str

Network = TypedDict("Network", {"net-id": str})

class Instances(base.ManagerWithFind):
    resource_class: Type[Instance]

    def _get_swift_client(self) -> swift_client.Connection: ...
    def create(
        self,
        name: str,
        flavor_id: Optional[str] = None,
        volume: Optional[Volume] = None,
        databases: Optional[List[Database]] = None,
        users: Optional[List[User]] = None,
        restorePoint: Optional[RestorePoint] = None,
        availability_zone: Optional[str] = None,
        datastore: Optional[str] = None,
        datastore_version: Optional[str] = None,
        nics: Optional[List[Network]] = None,
        configuration: Optional[str] = None,  # TODO: Add configuration type
        replica_of: Optional[Union[Instance, str]] = None,
        replica_count: Optional[int] = None,
        modules: Optional[List[str]] = None,  # TODO: Add module type
        locality: Optional[str] = None,
        region_name: Optional[str] = None,
        access: Optional[Access] = None,
        datastore_version_number: Optional[str] = None,
        **kwargs
    ) -> Instance: ...
    def modify(self, instance: Union[Instance, str], configuration=None): ...
    def update(
        self,
        instance: Union[Instance, str],
        configuration: Optional[str] = None,  # TODO: Add configuration type
        name: Optional[str] = None,
        detach_replica_source: bool = False,
        remove_configuration: bool = False,
        is_public: Optional[bool] = None,
        allowed_cidrs: Optional[List[str]] = None,
    ): ...
    def upgrade(self, instance: Union[Instance, str], datastore_version: str): ...
    def list(
        self,
        limit: Optional[int] = None,
        marker: Any = None,
        include_clustered: bool = False,
        detailed: bool = False,
    ) -> List[Instance]: ...
    def get(self, instance: Union[Instance, str]): ...
    def backups(
        self, instance: Union[Instance, str], limit: Optional[int] = None, marker=None
    ): ...
    def delete(self, instance: Union[Instance, str]): ...
    def reset_status(self, instance: Union[Instance, str]): ...
    def force_delete(self, instance: Union[Instance, str]): ...
    def _action(self, instance: Union[Instance, str], body: Dict): ...
    def resize_volume(self, instance: Union[Instance, str], volume_size: int): ...
    def resize_instance(self, instance: Union[Instance, str], flavor_id: str): ...
    def restart(self, instance: Union[Instance, str]): ...
    def configuration(self, instance: Union[Instance, str]): ...
    def promote_to_replica_source(self, instance: Union[Instance, str]): ...
    def eject_replica_source(self, instance: Union[Instance, str]): ...
    def modules(self, instance: Union[Instance, str]): ...
    def module_retrieve(
        self, instance: Union[Instance, str], directory=None, prefix=None
    ): ...
    def _modules_get(
        self, instance: Union[Instance, str], from_guest=None, include_contents=None
    ): ...
    def module_apply(self, instance: Union[Instance, str], modules): ...
    def _get_module_list(self, modules): ...
    def module_remove(self, instance: Union[Instance, str], module): ...
    def log_list(self, instance: Union[Instance, str]) -> List[DatastoreLog]: ...
    def log_show(self, instance: Union[Instance, str], log_name) -> DatastoreLog: ...
    def log_action(
        self,
        instance: Union[Instance, str],
        log_name,
        enable=None,
        disable=None,
        publish=None,
        discard=None,
    ) -> DatastoreLog: ...
    def _get_container_info(self, instance: Union[Instance, str], log_name): ...
    def log_generator(
        self, instance: Union[Instance, str], log_name, lines=50, swift=None
    ): ...
    def log_save(
        self, instance: Union[Instance, str], log_name, filename=None
    ) -> str: ...
