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
from .. import _utilities
from . import outputs

__all__ = [
    'GetPrivateEndpointResult',
    'AwaitableGetPrivateEndpointResult',
    'get_private_endpoint',
    'get_private_endpoint_output',
]

@pulumi.output_type
class GetPrivateEndpointResult:
    """
    Complete information about the private endpoint.
    """
    def __init__(__self__, created_date=None, etag=None, id=None, manual_private_link_service_connections=None, name=None, type=None):
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if manual_private_link_service_connections and not isinstance(manual_private_link_service_connections, list):
            raise TypeError("Expected argument 'manual_private_link_service_connections' to be a list")
        pulumi.set(__self__, "manual_private_link_service_connections", manual_private_link_service_connections)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        """
        The date when this private endpoint was created.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Unique opaque string (generally a GUID) that represents the metadata state of the resource (private endpoint) and changes whenever the resource is updated. Required on PUT (CreateOrUpdate) requests.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="manualPrivateLinkServiceConnections")
    def manual_private_link_service_connections(self) -> Optional[Sequence['outputs.PrivateLinkServiceConnectionResponse']]:
        """
        A list of connections to the remote resource. Immutable after it is set.
        """
        return pulumi.get(self, "manual_private_link_service_connections")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. Ex- Microsoft.Compute/virtualMachines or Microsoft.Storage/storageAccounts.
        """
        return pulumi.get(self, "type")


class AwaitableGetPrivateEndpointResult(GetPrivateEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateEndpointResult(
            created_date=self.created_date,
            etag=self.etag,
            id=self.id,
            manual_private_link_service_connections=self.manual_private_link_service_connections,
            name=self.name,
            type=self.type)


def get_private_endpoint(cluster_name: Optional[str] = None,
                         private_endpoint_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateEndpointResult:
    """
    Gets information about the specified Private Endpoint.
    Azure REST API version: 2020-03-01.

    Other available API versions: 2020-03-01-preview.


    :param str cluster_name: The name of the cluster.
    :param str private_endpoint_name: The name of the private endpoint.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['privateEndpointName'] = private_endpoint_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:streamanalytics:getPrivateEndpoint', __args__, opts=opts, typ=GetPrivateEndpointResult).value

    return AwaitableGetPrivateEndpointResult(
        created_date=pulumi.get(__ret__, 'created_date'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        manual_private_link_service_connections=pulumi.get(__ret__, 'manual_private_link_service_connections'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_private_endpoint)
def get_private_endpoint_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                private_endpoint_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateEndpointResult]:
    """
    Gets information about the specified Private Endpoint.
    Azure REST API version: 2020-03-01.

    Other available API versions: 2020-03-01-preview.


    :param str cluster_name: The name of the cluster.
    :param str private_endpoint_name: The name of the private endpoint.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
