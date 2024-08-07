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
    'GetWatcherResult',
    'AwaitableGetWatcherResult',
    'get_watcher',
    'get_watcher_output',
]

@pulumi.output_type
class GetWatcherResult:
    """
    The DatabaseWatcherProviderHub resource.
    """
    def __init__(__self__, datastore=None, id=None, identity=None, location=None, name=None, provisioning_state=None, status=None, system_data=None, tags=None, type=None):
        if datastore and not isinstance(datastore, dict):
            raise TypeError("Expected argument 'datastore' to be a dict")
        pulumi.set(__self__, "datastore", datastore)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
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
    @pulumi.getter
    def datastore(self) -> Optional['outputs.DatastoreResponse']:
        """
        The data store for collected monitoring data.
        """
        return pulumi.get(self, "datastore")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        The managed service identities assigned to this resource.
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
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource watcher.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The monitoring collection status of the watcher.
        """
        return pulumi.get(self, "status")

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


class AwaitableGetWatcherResult(GetWatcherResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWatcherResult(
            datastore=self.datastore,
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_watcher(resource_group_name: Optional[str] = None,
                watcher_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWatcherResult:
    """
    Get a Watcher


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str watcher_name: The database watcher name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['watcherName'] = watcher_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:databasewatcher/v20230901preview:getWatcher', __args__, opts=opts, typ=GetWatcherResult).value

    return AwaitableGetWatcherResult(
        datastore=pulumi.get(__ret__, 'datastore'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_watcher)
def get_watcher_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                       watcher_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWatcherResult]:
    """
    Get a Watcher


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str watcher_name: The database watcher name.
    """
    ...
