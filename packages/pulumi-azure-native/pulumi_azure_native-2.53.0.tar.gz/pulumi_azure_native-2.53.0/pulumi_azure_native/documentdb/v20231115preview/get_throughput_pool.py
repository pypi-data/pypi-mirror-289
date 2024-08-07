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
    'GetThroughputPoolResult',
    'AwaitableGetThroughputPoolResult',
    'get_throughput_pool',
    'get_throughput_pool_output',
]

@pulumi.output_type
class GetThroughputPoolResult:
    """
    An Azure Cosmos DB Throughputpool.
    """
    def __init__(__self__, id=None, location=None, max_throughput=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if max_throughput and not isinstance(max_throughput, int):
            raise TypeError("Expected argument 'max_throughput' to be a int")
        pulumi.set(__self__, "max_throughput", max_throughput)
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
    @pulumi.getter(name="maxThroughput")
    def max_throughput(self) -> Optional[int]:
        """
        Value for throughput to be shared among CosmosDB resources in the pool.
        """
        return pulumi.get(self, "max_throughput")

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
        A provisioning state of the ThroughputPool.
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


class AwaitableGetThroughputPoolResult(GetThroughputPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetThroughputPoolResult(
            id=self.id,
            location=self.location,
            max_throughput=self.max_throughput,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_throughput_pool(resource_group_name: Optional[str] = None,
                        throughput_pool_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetThroughputPoolResult:
    """
    Retrieves the properties of an existing Azure Cosmos DB Throughput Pool


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str throughput_pool_name: Cosmos DB Throughput Pool name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['throughputPoolName'] = throughput_pool_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb/v20231115preview:getThroughputPool', __args__, opts=opts, typ=GetThroughputPoolResult).value

    return AwaitableGetThroughputPoolResult(
        id=pulumi.get(__ret__, 'id'),
        location=pulumi.get(__ret__, 'location'),
        max_throughput=pulumi.get(__ret__, 'max_throughput'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_throughput_pool)
def get_throughput_pool_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                               throughput_pool_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetThroughputPoolResult]:
    """
    Retrieves the properties of an existing Azure Cosmos DB Throughput Pool


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str throughput_pool_name: Cosmos DB Throughput Pool name.
    """
    ...
