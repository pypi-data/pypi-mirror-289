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
    'GetFavoriteProcessResult',
    'AwaitableGetFavoriteProcessResult',
    'get_favorite_process',
    'get_favorite_process_output',
]

@pulumi.output_type
class GetFavoriteProcessResult:
    """
    A favorite process identifier.
    """
    def __init__(__self__, actual_process_name=None, id=None, name=None, system_data=None, type=None):
        if actual_process_name and not isinstance(actual_process_name, str):
            raise TypeError("Expected argument 'actual_process_name' to be a str")
        pulumi.set(__self__, "actual_process_name", actual_process_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="actualProcessName")
    def actual_process_name(self) -> str:
        """
        The actual name of the favorite process. It will be equal to resource name except for the scenario that the process name contains characters that are not allowed in the resource name.
        """
        return pulumi.get(self, "actual_process_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetFavoriteProcessResult(GetFavoriteProcessResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFavoriteProcessResult(
            actual_process_name=self.actual_process_name,
            id=self.id,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_favorite_process(favorite_process_resource_name: Optional[str] = None,
                         package_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         test_base_account_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFavoriteProcessResult:
    """
    Gets a favorite process for a Test Base Package.


    :param str favorite_process_resource_name: The resource name of a favorite process in a package. If the process name contains characters that are not allowed in Azure Resource Name, we use 'actualProcessName' in request body to submit the name.
    :param str package_name: The resource name of the Test Base Package.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    __args__ = dict()
    __args__['favoriteProcessResourceName'] = favorite_process_resource_name
    __args__['packageName'] = package_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['testBaseAccountName'] = test_base_account_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:testbase/v20231101preview:getFavoriteProcess', __args__, opts=opts, typ=GetFavoriteProcessResult).value

    return AwaitableGetFavoriteProcessResult(
        actual_process_name=pulumi.get(__ret__, 'actual_process_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_favorite_process)
def get_favorite_process_output(favorite_process_resource_name: Optional[pulumi.Input[str]] = None,
                                package_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                test_base_account_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFavoriteProcessResult]:
    """
    Gets a favorite process for a Test Base Package.


    :param str favorite_process_resource_name: The resource name of a favorite process in a package. If the process name contains characters that are not allowed in Azure Resource Name, we use 'actualProcessName' in request body to submit the name.
    :param str package_name: The resource name of the Test Base Package.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    ...
