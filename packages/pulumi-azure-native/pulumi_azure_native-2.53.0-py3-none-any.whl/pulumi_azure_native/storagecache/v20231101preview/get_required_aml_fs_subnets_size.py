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
from ._inputs import *

__all__ = [
    'GetRequiredAmlFSSubnetsSizeResult',
    'AwaitableGetRequiredAmlFSSubnetsSizeResult',
    'get_required_aml_fs_subnets_size',
    'get_required_aml_fs_subnets_size_output',
]

@pulumi.output_type
class GetRequiredAmlFSSubnetsSizeResult:
    """
    Information about the number of available IP addresses that are required for the AML file system.
    """
    def __init__(__self__, filesystem_subnet_size=None):
        if filesystem_subnet_size and not isinstance(filesystem_subnet_size, int):
            raise TypeError("Expected argument 'filesystem_subnet_size' to be a int")
        pulumi.set(__self__, "filesystem_subnet_size", filesystem_subnet_size)

    @property
    @pulumi.getter(name="filesystemSubnetSize")
    def filesystem_subnet_size(self) -> Optional[int]:
        """
        The number of available IP addresses that are required for the AML file system.
        """
        return pulumi.get(self, "filesystem_subnet_size")


class AwaitableGetRequiredAmlFSSubnetsSizeResult(GetRequiredAmlFSSubnetsSizeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRequiredAmlFSSubnetsSizeResult(
            filesystem_subnet_size=self.filesystem_subnet_size)


def get_required_aml_fs_subnets_size(sku: Optional[Union['SkuName', 'SkuNameDict']] = None,
                                     storage_capacity_ti_b: Optional[float] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRequiredAmlFSSubnetsSizeResult:
    """
    Get the number of available IP addresses needed for the AML file system information provided.


    :param Union['SkuName', 'SkuNameDict'] sku: SKU for the resource.
    :param float storage_capacity_ti_b: The size of the AML file system, in TiB.
    """
    __args__ = dict()
    __args__['sku'] = sku
    __args__['storageCapacityTiB'] = storage_capacity_ti_b
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storagecache/v20231101preview:getRequiredAmlFSSubnetsSize', __args__, opts=opts, typ=GetRequiredAmlFSSubnetsSizeResult).value

    return AwaitableGetRequiredAmlFSSubnetsSizeResult(
        filesystem_subnet_size=pulumi.get(__ret__, 'filesystem_subnet_size'))


@_utilities.lift_output_func(get_required_aml_fs_subnets_size)
def get_required_aml_fs_subnets_size_output(sku: Optional[pulumi.Input[Optional[Union['SkuName', 'SkuNameDict']]]] = None,
                                            storage_capacity_ti_b: Optional[pulumi.Input[Optional[float]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRequiredAmlFSSubnetsSizeResult]:
    """
    Get the number of available IP addresses needed for the AML file system information provided.


    :param Union['SkuName', 'SkuNameDict'] sku: SKU for the resource.
    :param float storage_capacity_ti_b: The size of the AML file system, in TiB.
    """
    ...
