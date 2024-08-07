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
    'GetStandbyContainerGroupPoolResult',
    'AwaitableGetStandbyContainerGroupPoolResult',
    'get_standby_container_group_pool',
    'get_standby_container_group_pool_output',
]

@pulumi.output_type
class GetStandbyContainerGroupPoolResult:
    """
    A StandbyContainerGroupPoolResource.
    """
    def __init__(__self__, container_group_properties=None, elasticity_profile=None, id=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if container_group_properties and not isinstance(container_group_properties, dict):
            raise TypeError("Expected argument 'container_group_properties' to be a dict")
        pulumi.set(__self__, "container_group_properties", container_group_properties)
        if elasticity_profile and not isinstance(elasticity_profile, dict):
            raise TypeError("Expected argument 'elasticity_profile' to be a dict")
        pulumi.set(__self__, "elasticity_profile", elasticity_profile)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
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
    @pulumi.getter(name="containerGroupProperties")
    def container_group_properties(self) -> 'outputs.ContainerGroupPropertiesResponse':
        """
        Specifies container group properties of standby container group pools.
        """
        return pulumi.get(self, "container_group_properties")

    @property
    @pulumi.getter(name="elasticityProfile")
    def elasticity_profile(self) -> 'outputs.StandbyContainerGroupPoolElasticityProfileResponse':
        """
        Specifies elasticity profile of standby container group pools.
        """
        return pulumi.get(self, "elasticity_profile")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

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


class AwaitableGetStandbyContainerGroupPoolResult(GetStandbyContainerGroupPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStandbyContainerGroupPoolResult(
            container_group_properties=self.container_group_properties,
            elasticity_profile=self.elasticity_profile,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_standby_container_group_pool(resource_group_name: Optional[str] = None,
                                     standby_container_group_pool_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStandbyContainerGroupPoolResult:
    """
    Get a StandbyContainerGroupPoolResource
    Azure REST API version: 2023-12-01-preview.

    Other available API versions: 2024-03-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str standby_container_group_pool_name: Name of the standby container group pool
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['standbyContainerGroupPoolName'] = standby_container_group_pool_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:standbypool:getStandbyContainerGroupPool', __args__, opts=opts, typ=GetStandbyContainerGroupPoolResult).value

    return AwaitableGetStandbyContainerGroupPoolResult(
        container_group_properties=pulumi.get(__ret__, 'container_group_properties'),
        elasticity_profile=pulumi.get(__ret__, 'elasticity_profile'),
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_standby_container_group_pool)
def get_standby_container_group_pool_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                            standby_container_group_pool_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStandbyContainerGroupPoolResult]:
    """
    Get a StandbyContainerGroupPoolResource
    Azure REST API version: 2023-12-01-preview.

    Other available API versions: 2024-03-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str standby_container_group_pool_name: Name of the standby container group pool
    """
    ...
