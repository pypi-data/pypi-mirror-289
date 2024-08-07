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

__all__ = [
    'ListComputeKeysResult',
    'AwaitableListComputeKeysResult',
    'list_compute_keys',
    'list_compute_keys_output',
]

@pulumi.output_type
class ListComputeKeysResult:
    """
    Secrets related to a Machine Learning compute. Might differ for every type of compute.
    """
    def __init__(__self__, compute_type=None):
        if compute_type and not isinstance(compute_type, str):
            raise TypeError("Expected argument 'compute_type' to be a str")
        pulumi.set(__self__, "compute_type", compute_type)

    @property
    @pulumi.getter(name="computeType")
    def compute_type(self) -> str:
        """
        The type of compute
        """
        return pulumi.get(self, "compute_type")


class AwaitableListComputeKeysResult(ListComputeKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListComputeKeysResult(
            compute_type=self.compute_type)


def list_compute_keys(compute_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      workspace_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListComputeKeysResult:
    """
    Gets secrets related to Machine Learning compute (storage keys, service credentials, etc).


    :param str compute_name: Name of the Azure Machine Learning compute.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['computeName'] = compute_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20230401:listComputeKeys', __args__, opts=opts, typ=ListComputeKeysResult).value

    return AwaitableListComputeKeysResult(
        compute_type=pulumi.get(__ret__, 'compute_type'))


@_utilities.lift_output_func(list_compute_keys)
def list_compute_keys_output(compute_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             workspace_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListComputeKeysResult]:
    """
    Gets secrets related to Machine Learning compute (storage keys, service credentials, etc).


    :param str compute_name: Name of the Azure Machine Learning compute.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
