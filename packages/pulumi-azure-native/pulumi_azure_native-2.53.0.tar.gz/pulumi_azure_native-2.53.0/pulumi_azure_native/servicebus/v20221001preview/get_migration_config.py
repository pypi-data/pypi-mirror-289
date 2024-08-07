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
    'GetMigrationConfigResult',
    'AwaitableGetMigrationConfigResult',
    'get_migration_config',
    'get_migration_config_output',
]

@pulumi.output_type
class GetMigrationConfigResult:
    """
    Single item in List or Get Migration Config operation
    """
    def __init__(__self__, id=None, location=None, migration_state=None, name=None, pending_replication_operations_count=None, post_migration_name=None, provisioning_state=None, system_data=None, target_namespace=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if migration_state and not isinstance(migration_state, str):
            raise TypeError("Expected argument 'migration_state' to be a str")
        pulumi.set(__self__, "migration_state", migration_state)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pending_replication_operations_count and not isinstance(pending_replication_operations_count, float):
            raise TypeError("Expected argument 'pending_replication_operations_count' to be a float")
        pulumi.set(__self__, "pending_replication_operations_count", pending_replication_operations_count)
        if post_migration_name and not isinstance(post_migration_name, str):
            raise TypeError("Expected argument 'post_migration_name' to be a str")
        pulumi.set(__self__, "post_migration_name", post_migration_name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if target_namespace and not isinstance(target_namespace, str):
            raise TypeError("Expected argument 'target_namespace' to be a str")
        pulumi.set(__self__, "target_namespace", target_namespace)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="migrationState")
    def migration_state(self) -> str:
        """
        State in which Standard to Premium Migration is, possible values : Unknown, Reverting, Completing, Initiating, Syncing, Active
        """
        return pulumi.get(self, "migration_state")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pendingReplicationOperationsCount")
    def pending_replication_operations_count(self) -> float:
        """
        Number of entities pending to be replicated.
        """
        return pulumi.get(self, "pending_replication_operations_count")

    @property
    @pulumi.getter(name="postMigrationName")
    def post_migration_name(self) -> str:
        """
        Name to access Standard Namespace after migration
        """
        return pulumi.get(self, "post_migration_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of Migration Configuration 
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> str:
        """
        Existing premium Namespace ARM Id name which has no entities, will be used for migration
        """
        return pulumi.get(self, "target_namespace")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs"
        """
        return pulumi.get(self, "type")


class AwaitableGetMigrationConfigResult(GetMigrationConfigResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMigrationConfigResult(
            id=self.id,
            location=self.location,
            migration_state=self.migration_state,
            name=self.name,
            pending_replication_operations_count=self.pending_replication_operations_count,
            post_migration_name=self.post_migration_name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            target_namespace=self.target_namespace,
            type=self.type)


def get_migration_config(config_name: Optional[str] = None,
                         namespace_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMigrationConfigResult:
    """
    Retrieves Migration Config


    :param str config_name: The configuration name. Should always be "$default".
    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['configName'] = config_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicebus/v20221001preview:getMigrationConfig', __args__, opts=opts, typ=GetMigrationConfigResult).value

    return AwaitableGetMigrationConfigResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        migration_state=pulumi.get(__ret__, 'migration_state'),
        name=pulumi.get(__ret__, 'name'),
        pending_replication_operations_count=pulumi.get(__ret__, 'pending_replication_operations_count'),
        post_migration_name=pulumi.get(__ret__, 'post_migration_name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        target_namespace=pulumi.get(__ret__, 'target_namespace'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_migration_config)
def get_migration_config_output(config_name: Optional[pulumi.Input[str]] = None,
                                namespace_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMigrationConfigResult]:
    """
    Retrieves Migration Config


    :param str config_name: The configuration name. Should always be "$default".
    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...
