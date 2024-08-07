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
    'ListEnergyServicePartitionsResult',
    'AwaitableListEnergyServicePartitionsResult',
    'list_energy_service_partitions',
    'list_energy_service_partitions_output',
]

@pulumi.output_type
class ListEnergyServicePartitionsResult:
    """
    List of data partitions.
    """
    def __init__(__self__, data_partition_info=None):
        if data_partition_info and not isinstance(data_partition_info, list):
            raise TypeError("Expected argument 'data_partition_info' to be a list")
        pulumi.set(__self__, "data_partition_info", data_partition_info)

    @property
    @pulumi.getter(name="dataPartitionInfo")
    def data_partition_info(self) -> Optional[Sequence['outputs.DataPartitionPropertiesResponse']]:
        """
        List of data partitions along with their properties in a given OEP resource.
        """
        return pulumi.get(self, "data_partition_info")


class AwaitableListEnergyServicePartitionsResult(ListEnergyServicePartitionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListEnergyServicePartitionsResult(
            data_partition_info=self.data_partition_info)


def list_energy_service_partitions(resource_group_name: Optional[str] = None,
                                   resource_name: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListEnergyServicePartitionsResult:
    """
    Method that gets called when list of partitions is requested.
    Azure REST API version: 2022-04-04-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The resource name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:openenergyplatform:listEnergyServicePartitions', __args__, opts=opts, typ=ListEnergyServicePartitionsResult).value

    return AwaitableListEnergyServicePartitionsResult(
        data_partition_info=pulumi.get(__ret__, 'data_partition_info'))


@_utilities.lift_output_func(list_energy_service_partitions)
def list_energy_service_partitions_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                          resource_name: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListEnergyServicePartitionsResult]:
    """
    Method that gets called when list of partitions is requested.
    Azure REST API version: 2022-04-04-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The resource name.
    """
    ...
