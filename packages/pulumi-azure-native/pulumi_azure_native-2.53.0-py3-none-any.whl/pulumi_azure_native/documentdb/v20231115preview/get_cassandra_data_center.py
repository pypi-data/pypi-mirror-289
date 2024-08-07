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
    'GetCassandraDataCenterResult',
    'AwaitableGetCassandraDataCenterResult',
    'get_cassandra_data_center',
    'get_cassandra_data_center_output',
]

@pulumi.output_type
class GetCassandraDataCenterResult:
    """
    A managed Cassandra data center.
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique resource identifier of the database account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the database account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.DataCenterResourceResponseProperties':
        """
        Properties of a managed Cassandra data center.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of Azure resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetCassandraDataCenterResult(GetCassandraDataCenterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCassandraDataCenterResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_cassandra_data_center(cluster_name: Optional[str] = None,
                              data_center_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCassandraDataCenterResult:
    """
    Get the properties of a managed Cassandra data center.


    :param str cluster_name: Managed Cassandra cluster name.
    :param str data_center_name: Data center name in a managed Cassandra cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['dataCenterName'] = data_center_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:documentdb/v20231115preview:getCassandraDataCenter', __args__, opts=opts, typ=GetCassandraDataCenterResult).value

    return AwaitableGetCassandraDataCenterResult(
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_cassandra_data_center)
def get_cassandra_data_center_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                     data_center_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCassandraDataCenterResult]:
    """
    Get the properties of a managed Cassandra data center.


    :param str cluster_name: Managed Cassandra cluster name.
    :param str data_center_name: Data center name in a managed Cassandra cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
