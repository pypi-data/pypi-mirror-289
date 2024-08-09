from typing import Any, List, Optional, Union

from keystoneauth1 import session  # type: ignore
from troveclient.auth_plugin import BaseAuthPlugin
from troveclient.client import HTTPClient, SessionClient
from troveclient.extension import Extension
from troveclient.v1 import (  # type: ignore
    backup_strategy,
    backups,
    clusters,
    configurations,
    databases,
    datastores,
    flavors,
    instances,
    limits,
    management,
    metadata,
    modules,
    quota,
    root,
    security_groups,
    users,
    volume_types,
)

class Client(object):
    flavors: flavors.Flavors  # type: ignore
    volume_types: volume_types.VolumeTypes  # type: ignore
    users: users.Users  # type: ignore
    databases: databases.Databases  # type: ignore
    backups: backups.Backups  # type: ignore
    backup_strategies: backup_strategy.BackupStrategiesManager  # type: ignore
    clusters: clusters.Clusters  # type: ignore
    instances: instances.Instances
    limits: limits.Limits  # type: ignore
    root: root.Root  # type: ignore
    security_group_rules: security_groups.SecurityGroupRules  # type: ignore
    security_groups: security_groups.SecurityGroups  # type: ignore
    datastores: datastores.Datastores  # type: ignore
    datastore_versions: datastores.DatastoreVersions  # type: ignore
    configurations: configurations.Configurations  # type: ignore
    configuration_parameters: configurations.ConfigurationParameters  # type: ignore
    metadata: metadata.Metadata  # type: ignore
    modules: modules.Modules  # type: ignore
    quota: quota.Quotas  # type: ignore
    mgmt_instances: management.Management  # type: ignore
    mgmt_ds_versions: management.MgmtDatastoreVersions  # type: ignore
    client: Union[HTTPClient, SessionClient]
    def __init__(
        self,
        username: Optional[str] = None,
        password: Optional[str] = None,
        project_id: Optional[str] = None,
        auth_url: str = "",
        insecure: bool = False,
        timeout: Optional[int] = None,
        tenant_id: Optional[str] = None,
        proxy_tenant_id: Optional[str] = None,
        proxy_token: Optional[str] = None,
        region_name: Optional[str] = None,
        endpoint_type: str = "publicURL",
        extensions: Optional[List[Extension]] = None,
        service_type: str = "database",
        service_name: Optional[str] = None,
        database_service_name: Optional[str] = None,
        retries: Optional[int] = None,
        http_log_debug: bool = False,
        cacert=None,
        bypass_url: Optional[str] = None,
        auth_system: str = "keystone",
        auth_plugin: Optional[BaseAuthPlugin] = None,
        session: Optional[session.Session] = None,
        auth: Any = None,
        **kwargs
    ): ...
