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
    'GetLabAccountRegionalAvailabilityResult',
    'AwaitableGetLabAccountRegionalAvailabilityResult',
    'get_lab_account_regional_availability',
    'get_lab_account_regional_availability_output',
]

@pulumi.output_type
class GetLabAccountRegionalAvailabilityResult:
    """
    The response model from the GetRegionalAvailability action
    """
    def __init__(__self__, regional_availability=None):
        if regional_availability and not isinstance(regional_availability, list):
            raise TypeError("Expected argument 'regional_availability' to be a list")
        pulumi.set(__self__, "regional_availability", regional_availability)

    @property
    @pulumi.getter(name="regionalAvailability")
    def regional_availability(self) -> Optional[Sequence['outputs.RegionalAvailabilityResponse']]:
        """
        Availability information for different size categories per region
        """
        return pulumi.get(self, "regional_availability")


class AwaitableGetLabAccountRegionalAvailabilityResult(GetLabAccountRegionalAvailabilityResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLabAccountRegionalAvailabilityResult(
            regional_availability=self.regional_availability)


def get_lab_account_regional_availability(lab_account_name: Optional[str] = None,
                                          resource_group_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLabAccountRegionalAvailabilityResult:
    """
    Get regional availability information for each size category configured under a lab account


    :param str lab_account_name: The name of the lab Account.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['labAccountName'] = lab_account_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:labservices/v20181015:getLabAccountRegionalAvailability', __args__, opts=opts, typ=GetLabAccountRegionalAvailabilityResult).value

    return AwaitableGetLabAccountRegionalAvailabilityResult(
        regional_availability=pulumi.get(__ret__, 'regional_availability'))


@_utilities.lift_output_func(get_lab_account_regional_availability)
def get_lab_account_regional_availability_output(lab_account_name: Optional[pulumi.Input[str]] = None,
                                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLabAccountRegionalAvailabilityResult]:
    """
    Get regional availability information for each size category configured under a lab account


    :param str lab_account_name: The name of the lab Account.
    :param str resource_group_name: The name of the resource group.
    """
    ...
