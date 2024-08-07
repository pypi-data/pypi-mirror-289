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
    def __init__(__self__, administrator_login=None, availability_zone=None, byok_enforcement=None, delegated_subnet_arguments=None, earliest_restore_date=None, fully_qualified_domain_name=None, ha_enabled=None, ha_state=None, id=None, identity=None, location=None, maintenance_window=None, name=None, public_network_access=None, replica_capacity=None, replication_role=None, sku=None, source_server_id=None, ssl_enforcement=None, standby_availability_zone=None, state=None, storage_profile=None, tags=None, type=None, version=None):
        if administrator_login and not isinstance(administrator_login, str):
            raise TypeError("Expected argument 'administrator_login' to be a str")
        pulumi.set(__self__, "administrator_login", administrator_login)
        if availability_zone and not isinstance(availability_zone, str):
            raise TypeError("Expected argument 'availability_zone' to be a str")
        pulumi.set(__self__, "availability_zone", availability_zone)
        if byok_enforcement and not isinstance(byok_enforcement, str):
            raise TypeError("Expected argument 'byok_enforcement' to be a str")
        pulumi.set(__self__, "byok_enforcement", byok_enforcement)
        if delegated_subnet_arguments and not isinstance(delegated_subnet_arguments, dict):
            raise TypeError("Expected argument 'delegated_subnet_arguments' to be a dict")
        pulumi.set(__self__, "delegated_subnet_arguments", delegated_subnet_arguments)
        if earliest_restore_date and not isinstance(earliest_restore_date, str):
            raise TypeError("Expected argument 'earliest_restore_date' to be a str")
        pulumi.set(__self__, "earliest_restore_date", earliest_restore_date)
        if fully_qualified_domain_name and not isinstance(fully_qualified_domain_name, str):
            raise TypeError("Expected argument 'fully_qualified_domain_name' to be a str")
        pulumi.set(__self__, "fully_qualified_domain_name", fully_qualified_domain_name)
        if ha_enabled and not isinstance(ha_enabled, str):
            raise TypeError("Expected argument 'ha_enabled' to be a str")
        pulumi.set(__self__, "ha_enabled", ha_enabled)
        if ha_state and not isinstance(ha_state, str):
            raise TypeError("Expected argument 'ha_state' to be a str")
        pulumi.set(__self__, "ha_state", ha_state)
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
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if replica_capacity and not isinstance(replica_capacity, int):
            raise TypeError("Expected argument 'replica_capacity' to be a int")
        pulumi.set(__self__, "replica_capacity", replica_capacity)
        if replication_role and not isinstance(replication_role, str):
            raise TypeError("Expected argument 'replication_role' to be a str")
        pulumi.set(__self__, "replication_role", replication_role)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if source_server_id and not isinstance(source_server_id, str):
            raise TypeError("Expected argument 'source_server_id' to be a str")
        pulumi.set(__self__, "source_server_id", source_server_id)
        if ssl_enforcement and not isinstance(ssl_enforcement, str):
            raise TypeError("Expected argument 'ssl_enforcement' to be a str")
        pulumi.set(__self__, "ssl_enforcement", ssl_enforcement)
        if standby_availability_zone and not isinstance(standby_availability_zone, str):
            raise TypeError("Expected argument 'standby_availability_zone' to be a str")
        pulumi.set(__self__, "standby_availability_zone", standby_availability_zone)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_profile and not isinstance(storage_profile, dict):
            raise TypeError("Expected argument 'storage_profile' to be a dict")
        pulumi.set(__self__, "storage_profile", storage_profile)
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
    @pulumi.getter(name="availabilityZone")
    def availability_zone(self) -> Optional[str]:
        """
        availability Zone information of the server.
        """
        return pulumi.get(self, "availability_zone")

    @property
    @pulumi.getter(name="byokEnforcement")
    def byok_enforcement(self) -> str:
        """
        Status showing whether the data encryption is enabled with customer-managed keys.
        """
        return pulumi.get(self, "byok_enforcement")

    @property
    @pulumi.getter(name="delegatedSubnetArguments")
    def delegated_subnet_arguments(self) -> Optional['outputs.DelegatedSubnetArgumentsResponse']:
        """
        Delegated subnet arguments.
        """
        return pulumi.get(self, "delegated_subnet_arguments")

    @property
    @pulumi.getter(name="earliestRestoreDate")
    def earliest_restore_date(self) -> str:
        """
        Earliest restore point creation time (ISO8601 format)
        """
        return pulumi.get(self, "earliest_restore_date")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> str:
        """
        The fully qualified domain name of a server.
        """
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter(name="haEnabled")
    def ha_enabled(self) -> Optional[str]:
        """
        Enable HA or not for a server.
        """
        return pulumi.get(self, "ha_enabled")

    @property
    @pulumi.getter(name="haState")
    def ha_state(self) -> str:
        """
        The state of a HA server.
        """
        return pulumi.get(self, "ha_state")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityResponse']:
        """
        The Azure Active Directory identity of the server.
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
        Maintenance window of a server.
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
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> str:
        """
        Whether or not public network access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="replicaCapacity")
    def replica_capacity(self) -> int:
        """
        The maximum number of replicas that a primary server can have.
        """
        return pulumi.get(self, "replica_capacity")

    @property
    @pulumi.getter(name="replicationRole")
    def replication_role(self) -> Optional[str]:
        """
        The replication role.
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
    @pulumi.getter(name="sourceServerId")
    def source_server_id(self) -> Optional[str]:
        """
        The source MySQL server id.
        """
        return pulumi.get(self, "source_server_id")

    @property
    @pulumi.getter(name="sslEnforcement")
    def ssl_enforcement(self) -> Optional[str]:
        """
        Enable ssl enforcement or not when connect to server.
        """
        return pulumi.get(self, "ssl_enforcement")

    @property
    @pulumi.getter(name="standbyAvailabilityZone")
    def standby_availability_zone(self) -> str:
        """
        availability Zone information of the server.
        """
        return pulumi.get(self, "standby_availability_zone")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of a server.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageProfile")
    def storage_profile(self) -> Optional['outputs.StorageProfileResponse']:
        """
        Storage profile of a server.
        """
        return pulumi.get(self, "storage_profile")

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
        Server version.
        """
        return pulumi.get(self, "version")


class AwaitableGetServerResult(GetServerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerResult(
            administrator_login=self.administrator_login,
            availability_zone=self.availability_zone,
            byok_enforcement=self.byok_enforcement,
            delegated_subnet_arguments=self.delegated_subnet_arguments,
            earliest_restore_date=self.earliest_restore_date,
            fully_qualified_domain_name=self.fully_qualified_domain_name,
            ha_enabled=self.ha_enabled,
            ha_state=self.ha_state,
            id=self.id,
            identity=self.identity,
            location=self.location,
            maintenance_window=self.maintenance_window,
            name=self.name,
            public_network_access=self.public_network_access,
            replica_capacity=self.replica_capacity,
            replication_role=self.replication_role,
            sku=self.sku,
            source_server_id=self.source_server_id,
            ssl_enforcement=self.ssl_enforcement,
            standby_availability_zone=self.standby_availability_zone,
            state=self.state,
            storage_profile=self.storage_profile,
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
    __ret__ = pulumi.runtime.invoke('azure-native:dbformysql/v20200701privatepreview:getServer', __args__, opts=opts, typ=GetServerResult).value

    return AwaitableGetServerResult(
        administrator_login=pulumi.get(__ret__, 'administrator_login'),
        availability_zone=pulumi.get(__ret__, 'availability_zone'),
        byok_enforcement=pulumi.get(__ret__, 'byok_enforcement'),
        delegated_subnet_arguments=pulumi.get(__ret__, 'delegated_subnet_arguments'),
        earliest_restore_date=pulumi.get(__ret__, 'earliest_restore_date'),
        fully_qualified_domain_name=pulumi.get(__ret__, 'fully_qualified_domain_name'),
        ha_enabled=pulumi.get(__ret__, 'ha_enabled'),
        ha_state=pulumi.get(__ret__, 'ha_state'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        maintenance_window=pulumi.get(__ret__, 'maintenance_window'),
        name=pulumi.get(__ret__, 'name'),
        public_network_access=pulumi.get(__ret__, 'public_network_access'),
        replica_capacity=pulumi.get(__ret__, 'replica_capacity'),
        replication_role=pulumi.get(__ret__, 'replication_role'),
        sku=pulumi.get(__ret__, 'sku'),
        source_server_id=pulumi.get(__ret__, 'source_server_id'),
        ssl_enforcement=pulumi.get(__ret__, 'ssl_enforcement'),
        standby_availability_zone=pulumi.get(__ret__, 'standby_availability_zone'),
        state=pulumi.get(__ret__, 'state'),
        storage_profile=pulumi.get(__ret__, 'storage_profile'),
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
