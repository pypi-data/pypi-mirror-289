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
    'GetServerResult',
    'AwaitableGetServerResult',
    'get_server',
    'get_server_output',
]

@pulumi.output_type
class GetServerResult:
    """
    Represents a server.
    """
    def __init__(__self__, administrator_login=None, auth_config=None, availability_zone=None, backup=None, data_encryption=None, fully_qualified_domain_name=None, high_availability=None, id=None, identity=None, location=None, maintenance_window=None, minor_version=None, name=None, network=None, replica_capacity=None, replication_role=None, sku=None, state=None, storage=None, system_data=None, tags=None, type=None, version=None):
        if administrator_login and not isinstance(administrator_login, str):
            raise TypeError("Expected argument 'administrator_login' to be a str")
        pulumi.set(__self__, "administrator_login", administrator_login)
        if auth_config and not isinstance(auth_config, dict):
            raise TypeError("Expected argument 'auth_config' to be a dict")
        pulumi.set(__self__, "auth_config", auth_config)
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if backup and not isinstance(backup, dict):
            raise TypeError("Expected argument 'backup' to be a dict")
        pulumi.set(__self__, "backup", backup)
        if data_encryption and not isinstance(data_encryption, dict):
            raise TypeError("Expected argument 'data_encryption' to be a dict")
        pulumi.set(__self__, "data_encryption", data_encryption)
        if fully_qualified_domain_name and not isinstance(fully_qualified_domain_name, str):
            raise TypeError("Expected argument 'fully_qualified_domain_name' to be a str")
        pulumi.set(__self__, "fully_qualified_domain_name", fully_qualified_domain_name)
        if high_availability and not isinstance(high_availability, dict):
            raise TypeError("Expected argument 'high_availability' to be a dict")
        pulumi.set(__self__, "high_availability", high_availability)
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
        if minor_version and not isinstance(minor_version, str):
            raise TypeError("Expected argument 'minor_version' to be a str")
        pulumi.set(__self__, "minor_version", minor_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network and not isinstance(network, dict):
            raise TypeError("Expected argument 'network' to be a dict")
        pulumi.set(__self__, "network", network)
        if replica_capacity and not isinstance(replica_capacity, int):
            raise TypeError("Expected argument 'replica_capacity' to be a int")
        pulumi.set(__self__, "replica_capacity", replica_capacity)
        if replication_role and not isinstance(replication_role, str):
            raise TypeError("Expected argument 'replication_role' to be a str")
        pulumi.set(__self__, "replication_role", replication_role)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage and not isinstance(storage, dict):
            raise TypeError("Expected argument 'storage' to be a dict")
        pulumi.set(__self__, "storage", storage)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="administratorLogin")
    def administrator_login(self) -> Optional[str]:
        """
        The administrator's login name of a server. Can only be specified when the server is being created (and is required for creation).
        """
        return pulumi.get(self, "administrator_login")

    @property
    @pulumi.getter(name="authConfig")
    def auth_config(self) -> Optional['outputs.AuthConfigResponse']:
        """
        AuthConfig properties of a server.
        """
        return pulumi.get(self, "auth_config")

    @property
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        """
        availability zone information of the server.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter
    def backup(self) -> Optional['outputs.BackupResponse']:
        """
        Backup properties of a server.
        """
        return pulumi.get(self, "backup")

    @property
    @pulumi.getter(name="dataEncryption")
    def data_encryption(self) -> Optional['outputs.DataEncryptionResponse']:
        """
        Data encryption properties of a server.
        """
        return pulumi.get(self, "data_encryption")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> str:
        """
        The fully qualified domain name of a server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter(name="highAvailability")
    def high_availability(self) -> Optional['outputs.HighAvailabilityResponse']:
        """
        High availability properties of a server.
        """
        return pulumi.get(self, "high_availability")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.UserAssignedIdentityResponse']:
        """
        Describes the identity of the application.
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
        Maintenance window properties of a server.
        """
        return pulumi.get(self, "maintenance_window")

    @property
    @pulumi.getter(name="minorVersion")
    def minor_version(self) -> str:
        """
        The minor version of the server.
        """
        return pulumi.get(self, "minor_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def network(self) -> Optional['outputs.NetworkResponse']:
        """
        Network properties of a server.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter(name="replicaCapacity")
    def replica_capacity(self) -> Optional[int]:
        """
        Replicas allowed for a server.
        """
        return pulumi.get(self, "replica_capacity")

    @property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> Optional[str]:
        """
        Replication role of the server
        """
        return pulumi.get(self, "replication_role")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The SKU (pricing tier) of the server.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        A state of a server that is visible to user.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def storage(self) -> Optional['outputs.StorageResponse']:
        """
        Storage properties of a server.
        """
        return pulumi.get(self, "storage")

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

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        PostgreSQL Server version.
        """
        return pulumi.get(self, "version")


class AwaitableGetServerResult(GetServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerResult(
            administrator_login=self.administrator_login,
            auth_config=self.auth_config,
            availability_zone=self.availability_zone,
            backup=self.backup,
            data_encryption=self.data_encryption,
            fully_qualified_domain_name=self.fully_qualified_domain_name,
            high_availability=self.high_availability,
            id=self.id,
            identity=self.identity,
            location=self.location,
            maintenance_window=self.maintenance_window,
            minor_version=self.minor_version,
            name=self.name,
            network=self.network,
            replica_capacity=self.replica_capacity,
            replication_role=self.replication_role,
            sku=self.sku,
            state=self.state,
            storage=self.storage,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            version=self.version)


def get_server(resource_group_name: Optional[str] = None,
               server_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerResult:
    """
    Gets information about a server.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbforpostgresql/v20220308preview:getServer', __args__, opts=opts, typ=GetServerResult).value

    return AwaitableGetServerResult(
        administrator_login=pulumi.get(__ret__, 'administrator_login'),
        auth_config=pulumi.get(__ret__, 'auth_config'),
        availability_zone=pulumi.get(__ret__, 'availability_zone'),
        backup=pulumi.get(__ret__, 'backup'),
        data_encryption=pulumi.get(__ret__, 'data_encryption'),
        fully_qualified_domain_name=pulumi.get(__ret__, 'fully_qualified_domain_name'),
        high_availability=pulumi.get(__ret__, 'high_availability'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_window=pulumi.get(__ret__, 'maintenance_window'),
        minor_version=pulumi.get(__ret__, 'minor_version'),
        name=pulumi.get(__ret__, 'name'),
        network=pulumi.get(__ret__, 'network'),
        replica_capacity=pulumi.get(__ret__, 'replica_capacity'),
        replication_role=pulumi.get(__ret__, 'replication_role'),
        sku=pulumi.get(__ret__, 'sku'),
        state=pulumi.get(__ret__, 'state'),
        storage=pulumi.get(__ret__, 'storage'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_server)
def get_server_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                      server_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerResult]:
    """
    Gets information about a server.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_name: The name of the server.
    """
    ...
