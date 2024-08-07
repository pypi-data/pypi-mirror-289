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
    'GetManagedPrivateEndpointResult',
    'AwaitableGetManagedPrivateEndpointResult',
    'get_managed_private_endpoint',
    'get_managed_private_endpoint_output',
]

@pulumi.output_type
class GetManagedPrivateEndpointResult:
    """
    Class representing a managed private endpoint.
    """
    def __init__(__self__, group_id=None, id=None, name=None, private_link_resource_id=None, private_link_resource_region=None, provisioning_state=None, request_message=None, system_data=None, type=None):
        if group_id and not isinstance(group_id, str):
            raise TypeError("Expected argument 'group_id' to be a str")
        pulumi.set(__self__, "group_id", group_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_link_resource_id and not isinstance(private_link_resource_id, str):
            raise TypeError("Expected argument 'private_link_resource_id' to be a str")
        pulumi.set(__self__, "private_link_resource_id", private_link_resource_id)
        if private_link_resource_region and not isinstance(private_link_resource_region, str):
            raise TypeError("Expected argument 'private_link_resource_region' to be a str")
        pulumi.set(__self__, "private_link_resource_region", private_link_resource_region)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if request_message and not isinstance(request_message, str):
            raise TypeError("Expected argument 'request_message' to be a str")
        pulumi.set(__self__, "request_message", request_message)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> str:
        """
        The groupId in which the managed private endpoint is created.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkResourceId")
    def private_link_resource_id(self) -> str:
        """
        The ARM resource ID of the resource for which the managed private endpoint is created.
        """
        return pulumi.get(self, "private_link_resource_id")

    @property
    @pulumi.getter(name="privateLinkResourceRegion")
    def private_link_resource_region(self) -> Optional[str]:
        """
        The region of the resource to which the managed private endpoint is created.
        """
        return pulumi.get(self, "private_link_resource_region")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="requestMessage")
    def request_message(self) -> Optional[str]:
        """
        The user request message.
        """
        return pulumi.get(self, "request_message")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedPrivateEndpointResult(GetManagedPrivateEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedPrivateEndpointResult(
            group_id=self.group_id,
            id=self.id,
            name=self.name,
            private_link_resource_id=self.private_link_resource_id,
            private_link_resource_region=self.private_link_resource_region,
            provisioning_state=self.provisioning_state,
            request_message=self.request_message,
            system_data=self.system_data,
            type=self.type)


def get_managed_private_endpoint(cluster_name: Optional[str] = None,
                                 managed_private_endpoint_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedPrivateEndpointResult:
    """
    Gets a managed private endpoint.


    :param str cluster_name: The name of the Kusto cluster.
    :param str managed_private_endpoint_name: The name of the managed private endpoint.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['managedPrivateEndpointName'] = managed_private_endpoint_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kusto/v20221229:getManagedPrivateEndpoint', __args__, opts=opts, typ=GetManagedPrivateEndpointResult).value

    return AwaitableGetManagedPrivateEndpointResult(
        group_id=pulumi.get(__ret__, 'group_id'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        private_link_resource_id=pulumi.get(__ret__, 'private_link_resource_id'),
        private_link_resource_region=pulumi.get(__ret__, 'private_link_resource_region'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        request_message=pulumi.get(__ret__, 'request_message'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_managed_private_endpoint)
def get_managed_private_endpoint_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                        managed_private_endpoint_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedPrivateEndpointResult]:
    """
    Gets a managed private endpoint.


    :param str cluster_name: The name of the Kusto cluster.
    :param str managed_private_endpoint_name: The name of the managed private endpoint.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    ...
