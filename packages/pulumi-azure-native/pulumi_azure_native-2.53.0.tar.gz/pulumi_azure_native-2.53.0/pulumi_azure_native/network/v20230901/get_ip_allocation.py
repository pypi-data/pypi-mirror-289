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
    'GetIpAllocationResult',
    'AwaitableGetIpAllocationResult',
    'get_ip_allocation',
    'get_ip_allocation_output',
]

@pulumi.output_type
class GetIpAllocationResult:
    """
    IpAllocation resource.
    """
    def __init__(__self__, allocation_tags=None, etag=None, id=None, ipam_allocation_id=None, location=None, name=None, prefix=None, prefix_length=None, prefix_type=None, subnet=None, tags=None, type=None, virtual_network=None):
        if allocation_tags and not isinstance(allocation_tags, dict):
            raise TypeError("Expected argument 'allocation_tags' to be a dict")
        pulumi.set(__self__, "allocation_tags", allocation_tags)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipam_allocation_id and not isinstance(ipam_allocation_id, str):
            raise TypeError("Expected argument 'ipam_allocation_id' to be a str")
        pulumi.set(__self__, "ipam_allocation_id", ipam_allocation_id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if prefix and not isinstance(prefix, str):
            raise TypeError("Expected argument 'prefix' to be a str")
        pulumi.set(__self__, "prefix", prefix)
        if prefix_length and not isinstance(prefix_length, int):
            raise TypeError("Expected argument 'prefix_length' to be a int")
        pulumi.set(__self__, "prefix_length", prefix_length)
        if prefix_type and not isinstance(prefix_type, str):
            raise TypeError("Expected argument 'prefix_type' to be a str")
        pulumi.set(__self__, "prefix_type", prefix_type)
        if subnet and not isinstance(subnet, dict):
            raise TypeError("Expected argument 'subnet' to be a dict")
        pulumi.set(__self__, "subnet", subnet)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_network and not isinstance(virtual_network, dict):
            raise TypeError("Expected argument 'virtual_network' to be a dict")
        pulumi.set(__self__, "virtual_network", virtual_network)

    @property
    @pulumi.getter(name="allocationTags")
    def allocation_tags(self) -> Optional[Mapping[str, str]]:
        """
        IpAllocation tags.
        """
        return pulumi.get(self, "allocation_tags")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipamAllocationId")
    def ipam_allocation_id(self) -> Optional[str]:
        """
        The IPAM allocation ID.
        """
        return pulumi.get(self, "ipam_allocation_id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def prefix(self) -> Optional[str]:
        """
        The address prefix for the IpAllocation.
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter(name="prefixLength")
    def prefix_length(self) -> Optional[int]:
        """
        The address prefix length for the IpAllocation.
        """
        return pulumi.get(self, "prefix_length")

    @property
    @pulumi.getter(name="prefixType")
    def prefix_type(self) -> Optional[str]:
        """
        The address prefix Type for the IpAllocation.
        """
        return pulumi.get(self, "prefix_type")

    @property
    @pulumi.getter
    def subnet(self) -> 'outputs.SubResourceResponse':
        """
        The Subnet that using the prefix of this IpAllocation resource.
        """
        return pulumi.get(self, "subnet")

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
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetwork")
    def virtual_network(self) -> 'outputs.SubResourceResponse':
        """
        The VirtualNetwork that using the prefix of this IpAllocation resource.
        """
        return pulumi.get(self, "virtual_network")


class AwaitableGetIpAllocationResult(GetIpAllocationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIpAllocationResult(
            allocation_tags=self.allocation_tags,
            etag=self.etag,
            id=self.id,
            ipam_allocation_id=self.ipam_allocation_id,
            location=self.location,
            name=self.name,
            prefix=self.prefix,
            prefix_length=self.prefix_length,
            prefix_type=self.prefix_type,
            subnet=self.subnet,
            tags=self.tags,
            type=self.type,
            virtual_network=self.virtual_network)


def get_ip_allocation(expand: Optional[str] = None,
                      ip_allocation_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIpAllocationResult:
    """
    Gets the specified IpAllocation by resource group.


    :param str expand: Expands referenced resources.
    :param str ip_allocation_name: The name of the IpAllocation.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['ipAllocationName'] = ip_allocation_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20230901:getIpAllocation', __args__, opts=opts, typ=GetIpAllocationResult).value

    return AwaitableGetIpAllocationResult(
        allocation_tags=pulumi.get(__ret__, 'allocation_tags'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        ipam_allocation_id=pulumi.get(__ret__, 'ipam_allocation_id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        prefix=pulumi.get(__ret__, 'prefix'),
        prefix_length=pulumi.get(__ret__, 'prefix_length'),
        prefix_type=pulumi.get(__ret__, 'prefix_type'),
        subnet=pulumi.get(__ret__, 'subnet'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        virtual_network=pulumi.get(__ret__, 'virtual_network'))


@_utilities.lift_output_func(get_ip_allocation)
def get_ip_allocation_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                             ip_allocation_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIpAllocationResult]:
    """
    Gets the specified IpAllocation by resource group.


    :param str expand: Expands referenced resources.
    :param str ip_allocation_name: The name of the IpAllocation.
    :param str resource_group_name: The name of the resource group.
    """
    ...
