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
    'GetAgentPoolResult',
    'AwaitableGetAgentPoolResult',
    'get_agent_pool',
    'get_agent_pool_output',
]

@pulumi.output_type
class GetAgentPoolResult:
    """
    The agentpool that has the ARM resource and properties. 
    The agentpool will have all information to create an agent pool.
    """
    def __init__(__self__, count=None, id=None, location=None, name=None, os=None, provisioning_state=None, system_data=None, tags=None, tier=None, type=None, virtual_network_subnet_resource_id=None):
        if count and not isinstance(count, int):
            raise TypeError("Expected argument 'count' to be a int")
        pulumi.set(__self__, "count", count)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os and not isinstance(os, str):
            raise TypeError("Expected argument 'os' to be a str")
        pulumi.set(__self__, "os", os)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tier and not isinstance(tier, str):
            raise TypeError("Expected argument 'tier' to be a str")
        pulumi.set(__self__, "tier", tier)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_network_subnet_resource_id and not isinstance(virtual_network_subnet_resource_id, str):
            raise TypeError("Expected argument 'virtual_network_subnet_resource_id' to be a str")
        pulumi.set(__self__, "virtual_network_subnet_resource_id", virtual_network_subnet_resource_id)

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        The count of agent machine
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the resource. This cannot be changed after the resource is created.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def os(self) -> Optional[str]:
        """
        The OS of agent machine
        """
        return pulumi.get(self, "os")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of this agent pool
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        The Tier of agent machine
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkSubnetResourceId")
    def virtual_network_subnet_resource_id(self) -> Optional[str]:
        """
        The Virtual Network Subnet Resource Id of the agent machine
        """
        return pulumi.get(self, "virtual_network_subnet_resource_id")


class AwaitableGetAgentPoolResult(GetAgentPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgentPoolResult(
            count=self.count,
            id=self.id,
            location=self.location,
            name=self.name,
            os=self.os,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            tier=self.tier,
            type=self.type,
            virtual_network_subnet_resource_id=self.virtual_network_subnet_resource_id)


def get_agent_pool(agent_pool_name: Optional[str] = None,
                   registry_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgentPoolResult:
    """
    Gets the detailed information for a given agent pool.
    Azure REST API version: 2019-06-01-preview.


    :param str agent_pool_name: The name of the agent pool.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    """
    __args__ = dict()
    __args__['agentPoolName'] = agent_pool_name
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry:getAgentPool', __args__, opts=opts, typ=GetAgentPoolResult).value

    return AwaitableGetAgentPoolResult(
        count=pulumi.get(__ret__, 'count'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        os=pulumi.get(__ret__, 'os'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        tier=pulumi.get(__ret__, 'tier'),
        type=pulumi.get(__ret__, 'type'),
        virtual_network_subnet_resource_id=pulumi.get(__ret__, 'virtual_network_subnet_resource_id'))


@_utilities.lift_output_func(get_agent_pool)
def get_agent_pool_output(agent_pool_name: Optional[pulumi.Input[str]] = None,
                          registry_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgentPoolResult]:
    """
    Gets the detailed information for a given agent pool.
    Azure REST API version: 2019-06-01-preview.


    :param str agent_pool_name: The name of the agent pool.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    """
    ...
