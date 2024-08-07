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
    'GetDiskAccessAPrivateEndpointConnectionResult',
    'AwaitableGetDiskAccessAPrivateEndpointConnectionResult',
    'get_disk_access_a_private_endpoint_connection',
    'get_disk_access_a_private_endpoint_connection_output',
]

@pulumi.output_type
class GetDiskAccessAPrivateEndpointConnectionResult:
    """
    The Private Endpoint Connection resource.
    """
    def __init__(__self__, id=None, name=None, private_endpoint=None, private_link_service_connection_state=None, provisioning_state=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint and not isinstance(private_endpoint, dict):
            raise TypeError("Expected argument 'private_endpoint' to be a dict")
        pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_link_service_connection_state and not isinstance(private_link_service_connection_state, dict):
            raise TypeError("Expected argument 'private_link_service_connection_state' to be a dict")
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        private endpoint connection Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        private endpoint connection name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> 'outputs.PrivateEndpointResponse':
        """
        The resource of private end point.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> 'outputs.PrivateLinkServiceConnectionStateResponse':
        """
        A collection of information about the state of the connection between DiskAccess and Virtual Network.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        private endpoint connection type
        """
        return pulumi.get(self, "type")


class AwaitableGetDiskAccessAPrivateEndpointConnectionResult(GetDiskAccessAPrivateEndpointConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiskAccessAPrivateEndpointConnectionResult(
            id=self.id,
            name=self.name,
            private_endpoint=self.private_endpoint,
            private_link_service_connection_state=self.private_link_service_connection_state,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_disk_access_a_private_endpoint_connection(disk_access_name: Optional[str] = None,
                                                  private_endpoint_connection_name: Optional[str] = None,
                                                  resource_group_name: Optional[str] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiskAccessAPrivateEndpointConnectionResult:
    """
    Gets information about a private endpoint connection under a disk access resource.


    :param str disk_access_name: The name of the disk access resource that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The maximum name length is 80 characters.
    :param str private_endpoint_connection_name: The name of the private endpoint connection.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['diskAccessName'] = disk_access_name
    __args__['privateEndpointConnectionName'] = private_endpoint_connection_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20230102:getDiskAccessAPrivateEndpointConnection', __args__, opts=opts, typ=GetDiskAccessAPrivateEndpointConnectionResult).value

    return AwaitableGetDiskAccessAPrivateEndpointConnectionResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        private_endpoint=pulumi.get(__ret__, 'private_endpoint'),
        private_link_service_connection_state=pulumi.get(__ret__, 'private_link_service_connection_state'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_disk_access_a_private_endpoint_connection)
def get_disk_access_a_private_endpoint_connection_output(disk_access_name: Optional[pulumi.Input[str]] = None,
                                                         private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDiskAccessAPrivateEndpointConnectionResult]:
    """
    Gets information about a private endpoint connection under a disk access resource.


    :param str disk_access_name: The name of the disk access resource that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The maximum name length is 80 characters.
    :param str private_endpoint_connection_name: The name of the private endpoint connection.
    :param str resource_group_name: The name of the resource group.
    """
    ...
