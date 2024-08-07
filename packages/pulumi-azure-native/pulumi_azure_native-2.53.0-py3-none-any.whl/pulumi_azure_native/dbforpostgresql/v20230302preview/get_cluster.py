# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from ... import _utilities
from . import outputs

__all__ = [
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    """
    Represents a cluster.
    """
    def __init__(__self__, aad_auth_enabled=None, administrator_login=None, auth_config=None, citus_version=None, coordinator_enable_public_ip_access=None, coordinator_server_edition=None, coordinator_storage_quota_in_mb=None, coordinator_v_cores=None, data_encryption=None, database_name=None, earliest_restore_time=None, enable_geo_backup=None, enable_ha=None, enable_shards_on_coordinator=None, id=None, identity=None, location=None, maintenance_window=None, name=None, node_count=None, node_enable_public_ip_access=None, node_server_edition=None, node_storage_quota_in_mb=None, node_v_cores=None, password_enabled=None, point_in_time_utc=None, postgresql_version=None, preferred_primary_zone=None, private_endpoint_connections=None, provisioning_state=None, read_replicas=None, server_names=None, source_location=None, source_resource_id=None, state=None, system_data=None, tags=None, type=None):
        if aad_auth_enabled and not isinstance(aad_auth_enabled, str):
            raise TypeError("Expected argument 'aad_auth_enabled' to be a str")
        pulumi.set(__self__, "aad_auth_enabled", aad_auth_enabled)
        if administrator_login and not isinstance(administrator_login, str):
            raise TypeError("Expected argument 'administrator_login' to be a str")
        pulumi.set(__self__, "administrator_login", administrator_login)
        if auth_config and not isinstance(auth_config, dict):
            raise TypeError("Expected argument 'auth_config' to be a dict")
        pulumi.set(__self__, "auth_config", auth_config)
        if citus_version and not isinstance(citus_version, str):
            raise TypeError("Expected argument 'citus_version' to be a str")
        pulumi.set(__self__, "citus_version", citus_version)
        if coordinator_enable_public_ip_access and not isinstance(coordinator_enable_public_ip_access, bool):
            raise TypeError("Expected argument 'coordinator_enable_public_ip_access' to be a bool")
        pulumi.set(__self__, "coordinator_enable_public_ip_access", coordinator_enable_public_ip_access)
        if coordinator_server_edition and not isinstance(coordinator_server_edition, str):
            raise TypeError("Expected argument 'coordinator_server_edition' to be a str")
        pulumi.set(__self__, "coordinator_server_edition", coordinator_server_edition)
        if coordinator_storage_quota_in_mb and not isinstance(coordinator_storage_quota_in_mb, int):
            raise TypeError("Expected argument 'coordinator_storage_quota_in_mb' to be a int")
        pulumi.set(__self__, "coordinator_storage_quota_in_mb", coordinator_storage_quota_in_mb)
        if coordinator_v_cores and not isinstance(coordinator_v_cores, int):
            raise TypeError("Expected argument 'coordinator_v_cores' to be a int")
        pulumi.set(__self__, "coordinator_v_cores", coordinator_v_cores)
        if data_encryption and not isinstance(data_encryption, dict):
            raise TypeError("Expected argument 'data_encryption' to be a dict")
        pulumi.set(__self__, "data_encryption", data_encryption)
        if database_name and not isinstance(database_name, str):
            raise TypeError("Expected argument 'database_name' to be a str")
        pulumi.set(__self__, "database_name", database_name)
        if earliest_restore_time and not isinstance(earliest_restore_time, str):
            raise TypeError("Expected argument 'earliest_restore_time' to be a str")
        pulumi.set(__self__, "earliest_restore_time", earliest_restore_time)
        if enable_geo_backup and not isinstance(enable_geo_backup, bool):
            raise TypeError("Expected argument 'enable_geo_backup' to be a bool")
        pulumi.set(__self__, "enable_geo_backup", enable_geo_backup)
        if enable_ha and not isinstance(enable_ha, bool):
            raise TypeError("Expected argument 'enable_ha' to be a bool")
        pulumi.set(__self__, "enable_ha", enable_ha)
        if enable_shards_on_coordinator and not isinstance(enable_shards_on_coordinator, bool):
            raise TypeError("Expected argument 'enable_shards_on_coordinator' to be a bool")
        pulumi.set(__self__, "enable_shards_on_coordinator", enable_shards_on_coordinator)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maintenance_window and not isinstance(maintenance_window, dict):
            raise TypeError("Expected argument 'maintenance_window' to be a dict")
        pulumi.set(__self__, "maintenance_window", maintenance_window)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_count and not isinstance(node_count, int):
            raise TypeError("Expected argument 'node_count' to be a int")
        pulumi.set(__self__, "node_count", node_count)
        if node_enable_public_ip_access and not isinstance(node_enable_public_ip_access, bool):
            raise TypeError("Expected argument 'node_enable_public_ip_access' to be a bool")
        pulumi.set(__self__, "node_enable_public_ip_access", node_enable_public_ip_access)
        if node_server_edition and not isinstance(node_server_edition, str):
            raise TypeError("Expected argument 'node_server_edition' to be a str")
        pulumi.set(__self__, "node_server_edition", node_server_edition)
        if node_storage_quota_in_mb and not isinstance(node_storage_quota_in_mb, int):
            raise TypeError("Expected argument 'node_storage_quota_in_mb' to be a int")
        pulumi.set(__self__, "node_storage_quota_in_mb", node_storage_quota_in_mb)
        if node_v_cores and not isinstance(node_v_cores, int):
            raise TypeError("Expected argument 'node_v_cores' to be a int")
        pulumi.set(__self__, "node_v_cores", node_v_cores)
        if password_enabled and not isinstance(password_enabled, str):
            raise TypeError("Expected argument 'password_enabled' to be a str")
        pulumi.set(__self__, "password_enabled", password_enabled)
        if point_in_time_utc and not isinstance(point_in_time_utc, str):
            raise TypeError("Expected argument 'point_in_time_utc' to be a str")
        pulumi.set(__self__, "point_in_time_utc", point_in_time_utc)
        if postgresql_version and not isinstance(postgresql_version, str):
            raise TypeError("Expected argument 'postgresql_version' to be a str")
        pulumi.set(__self__, "postgresql_version", postgresql_version)
        if preferred_primary_zone and not isinstance(preferred_primary_zone, str):
            raise TypeError("Expected argument 'preferred_primary_zone' to be a str")
        pulumi.set(__self__, "preferred_primary_zone", preferred_primary_zone)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if read_replicas and not isinstance(read_replicas, list):
            raise TypeError("Expected argument 'read_replicas' to be a list")
        pulumi.set(__self__, "read_replicas", read_replicas)
        if server_names and not isinstance(server_names, list):
            raise TypeError("Expected argument 'server_names' to be a list")
        pulumi.set(__self__, "server_names", server_names)
        if source_location and not isinstance(source_location, str):
            raise TypeError("Expected argument 'source_location' to be a str")
        pulumi.set(__self__, "source_location", source_location)
        if source_resource_id and not isinstance(source_resource_id, str):
            raise TypeError("Expected argument 'source_resource_id' to be a str")
        pulumi.set(__self__, "source_resource_id", source_resource_id)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="aadAuthEnabled")
    def aad_auth_enabled(self) -> str:
        """
        Indicates whether the cluster was created using AAD authentication.
        """
        return pulumi.get(self, "aad_auth_enabled")

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> str:
        """
        The administrator's login name of the servers in the cluster.
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="authConfig")
    def auth_config(self) -> Optional['outputs.AuthConfigResponse']:
        """
        Authentication configuration of a cluster.
        """
        return pulumi.get(self, "auth_config")

    @property
    @pulumi.getter(name="citusVersion")
    def citus_version(self) -> Optional[str]:
        """
        The Citus extension version on all cluster servers.
        """
        return pulumi.get(self, "citus_version")

    @property
    @pulumi.getter(name="coordinatorEnablePublicIpAccess")
    def coordinator_enable_public_ip_access(self) -> Optional[bool]:
        """
        If public access is enabled on coordinator.
        """
        return pulumi.get(self, "coordinator_enable_public_ip_access")

    @property
    @pulumi.getter(name="coordinatorServerEdition")
    def coordinator_server_edition(self) -> Optional[str]:
        """
        The edition of a coordinator server (default: GeneralPurpose). Required for creation.
        """
        return pulumi.get(self, "coordinator_server_edition")

    @property
    @pulumi.getter(name="coordinatorStorageQuotaInMb")
    def coordinator_storage_quota_in_mb(self) -> Optional[int]:
        """
        The storage of a server in MB. Required for creation. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.
        """
        return pulumi.get(self, "coordinator_storage_quota_in_mb")

    @property
    @pulumi.getter(name="coordinatorVCores")
    def coordinator_v_cores(self) -> Optional[int]:
        """
        The vCores count of a server (max: 96). Required for creation. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.
        """
        return pulumi.get(self, "coordinator_v_cores")

    @property
    @pulumi.getter(name="dataEncryption")
    def data_encryption(self) -> Optional['outputs.DataEncryptionResponse']:
        """
        The data encryption properties of a cluster.
        """
        return pulumi.get(self, "data_encryption")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[str]:
        """
        The database name of the cluster. Only one database per cluster is supported.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="earliestRestoreTime")
    def earliest_restore_time(self) -> str:
        """
        The earliest restore point time (ISO8601 format) for the cluster.
        """
        return pulumi.get(self, "earliest_restore_time")

    @property
    @pulumi.getter(name="enableGeoBackup")
    def enable_geo_backup(self) -> Optional[bool]:
        """
        If cluster backup is stored in another Azure region in addition to the copy of the backup stored in the cluster's region. Enabled only at the time of cluster creation.
        """
        return pulumi.get(self, "enable_geo_backup")

    @property
    @pulumi.getter(name="enableHa")
    def enable_ha(self) -> Optional[bool]:
        """
        If high availability (HA) is enabled or not for the cluster.
        """
        return pulumi.get(self, "enable_ha")

    @property
    @pulumi.getter(name="enableShardsOnCoordinator")
    def enable_shards_on_coordinator(self) -> Optional[bool]:
        """
        If distributed tables are placed on coordinator or not. Should be set to 'true' on single node clusters. Requires shard rebalancing after value is changed.
        """
        return pulumi.get(self, "enable_shards_on_coordinator")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityPropertiesResponse']:
        """
        Describes the identity of the cluster.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional['outputs.MaintenanceWindowResponse']:
        """
        Maintenance window of a cluster.
        """
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeCount")
    def node_count(self) -> Optional[int]:
        """
        Worker node count of the cluster. When node count is 0, it represents a single node configuration with the ability to create distributed tables on that node. 2 or more worker nodes represent multi-node configuration. Node count value cannot be 1. Required for creation.
        """
        return pulumi.get(self, "node_count")

    @property
    @pulumi.getter(name="nodeEnablePublicIpAccess")
    def node_enable_public_ip_access(self) -> Optional[bool]:
        """
        If public access is enabled on worker nodes.
        """
        return pulumi.get(self, "node_enable_public_ip_access")

    @property
    @pulumi.getter(name="nodeServerEdition")
    def node_server_edition(self) -> Optional[str]:
        """
        The edition of a node server (default: MemoryOptimized).
        """
        return pulumi.get(self, "node_server_edition")

    @property
    @pulumi.getter(name="nodeStorageQuotaInMb")
    def node_storage_quota_in_mb(self) -> Optional[int]:
        """
        The storage in MB on each worker node. See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.
        """
        return pulumi.get(self, "node_storage_quota_in_mb")

    @property
    @pulumi.getter(name="nodeVCores")
    def node_v_cores(self) -> Optional[int]:
        """
        The compute in vCores on each worker node (max: 104). See https://learn.microsoft.com/azure/cosmos-db/postgresql/resources-compute for more information.
        """
        return pulumi.get(self, "node_v_cores")

    @property
    @pulumi.getter(name="passwordEnabled")
    def password_enabled(self) -> str:
        """
        Indicates whether the cluster was created with a password or using AAD authentication.
        """
        return pulumi.get(self, "password_enabled")

    @property
    @pulumi.getter(name="pointInTimeUTC")
    def point_in_time_utc(self) -> Optional[str]:
        """
        Date and time in UTC (ISO8601 format) for cluster restore.
        """
        return pulumi.get(self, "point_in_time_utc")

    @property
    @pulumi.getter(name="postgresqlVersion")
    def postgresql_version(self) -> Optional[str]:
        """
        The major PostgreSQL version on all cluster servers.
        """
        return pulumi.get(self, "postgresql_version")

    @property
    @pulumi.getter(name="preferredPrimaryZone")
    def preferred_primary_zone(self) -> Optional[str]:
        """
        Preferred primary availability zone (AZ) for all cluster servers.
        """
        return pulumi.get(self, "preferred_primary_zone")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.SimplePrivateEndpointConnectionResponse']:
        """
        The private endpoint connections for a cluster.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the cluster
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="readReplicas")
    def read_replicas(self) -> Sequence[str]:
        """
        The array of read replica clusters.
        """
        return pulumi.get(self, "read_replicas")

    @property
    @pulumi.getter(name="serverNames")
    def server_names(self) -> Sequence['outputs.ServerNameItemResponse']:
        """
        The list of server names in the cluster
        """
        return pulumi.get(self, "server_names")

    @property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[str]:
        """
        The Azure region of source cluster for read replica clusters.
        """
        return pulumi.get(self, "source_location")

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[str]:
        """
        The resource id of source cluster for read replica clusters.
        """
        return pulumi.get(self, "source_resource_id")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        A state of a cluster/server that is visible to user.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            aad_auth_enabled=self.aad_auth_enabled,
            administrator_login=self.administrator_login,
            auth_config=self.auth_config,
            citus_version=self.citus_version,
            coordinator_enable_public_ip_access=self.coordinator_enable_public_ip_access,
            coordinator_server_edition=self.coordinator_server_edition,
            coordinator_storage_quota_in_mb=self.coordinator_storage_quota_in_mb,
            coordinator_v_cores=self.coordinator_v_cores,
            data_encryption=self.data_encryption,
            database_name=self.database_name,
            earliest_restore_time=self.earliest_restore_time,
            enable_geo_backup=self.enable_geo_backup,
            enable_ha=self.enable_ha,
            enable_shards_on_coordinator=self.enable_shards_on_coordinator,
            id=self.id,
            identity=self.identity,
            location=self.location,
            maintenance_window=self.maintenance_window,
            name=self.name,
            node_count=self.node_count,
            node_enable_public_ip_access=self.node_enable_public_ip_access,
            node_server_edition=self.node_server_edition,
            node_storage_quota_in_mb=self.node_storage_quota_in_mb,
            node_v_cores=self.node_v_cores,
            password_enabled=self.password_enabled,
            point_in_time_utc=self.point_in_time_utc,
            postgresql_version=self.postgresql_version,
            preferred_primary_zone=self.preferred_primary_zone,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            read_replicas=self.read_replicas,
            server_names=self.server_names,
            source_location=self.source_location,
            source_resource_id=self.source_resource_id,
            state=self.state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_cluster(cluster_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Gets information about a cluster such as compute and storage configuration and cluster lifecycle metadata such as cluster creation date and time.


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbforpostgresql/v20230302preview:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        aad_auth_enabled=pulumi.get(__ret__, 'aad_auth_enabled'),
        administrator_login=pulumi.get(__ret__, 'administrator_login'),
        auth_config=pulumi.get(__ret__, 'auth_config'),
        citus_version=pulumi.get(__ret__, 'citus_version'),
        coordinator_enable_public_ip_access=pulumi.get(__ret__, 'coordinator_enable_public_ip_access'),
        coordinator_server_edition=pulumi.get(__ret__, 'coordinator_server_edition'),
        coordinator_storage_quota_in_mb=pulumi.get(__ret__, 'coordinator_storage_quota_in_mb'),
        coordinator_v_cores=pulumi.get(__ret__, 'coordinator_v_cores'),
        data_encryption=pulumi.get(__ret__, 'data_encryption'),
        database_name=pulumi.get(__ret__, 'database_name'),
        earliest_restore_time=pulumi.get(__ret__, 'earliest_restore_time'),
        enable_geo_backup=pulumi.get(__ret__, 'enable_geo_backup'),
        enable_ha=pulumi.get(__ret__, 'enable_ha'),
        enable_shards_on_coordinator=pulumi.get(__ret__, 'enable_shards_on_coordinator'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_window=pulumi.get(__ret__, 'maintenance_window'),
        name=pulumi.get(__ret__, 'name'),
        node_count=pulumi.get(__ret__, 'node_count'),
        node_enable_public_ip_access=pulumi.get(__ret__, 'node_enable_public_ip_access'),
        node_server_edition=pulumi.get(__ret__, 'node_server_edition'),
        node_storage_quota_in_mb=pulumi.get(__ret__, 'node_storage_quota_in_mb'),
        node_v_cores=pulumi.get(__ret__, 'node_v_cores'),
        password_enabled=pulumi.get(__ret__, 'password_enabled'),
        point_in_time_utc=pulumi.get(__ret__, 'point_in_time_utc'),
        postgresql_version=pulumi.get(__ret__, 'postgresql_version'),
        preferred_primary_zone=pulumi.get(__ret__, 'preferred_primary_zone'),
        private_endpoint_connections=pulumi.get(__ret__, 'private_endpoint_connections'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        read_replicas=pulumi.get(__ret__, 'read_replicas'),
        server_names=pulumi.get(__ret__, 'server_names'),
        source_location=pulumi.get(__ret__, 'source_location'),
        source_resource_id=pulumi.get(__ret__, 'source_resource_id'),
        state=pulumi.get(__ret__, 'state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(cluster_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    Gets information about a cluster such as compute and storage configuration and cluster lifecycle metadata such as cluster creation date and time.


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
