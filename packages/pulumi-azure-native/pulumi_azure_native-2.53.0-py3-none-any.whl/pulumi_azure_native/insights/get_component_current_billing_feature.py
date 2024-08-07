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
    'GetComponentCurrentBillingFeatureResult',
    'AwaitableGetComponentCurrentBillingFeatureResult',
    'get_component_current_billing_feature',
    'get_component_current_billing_feature_output',
]

@pulumi.output_type
class GetComponentCurrentBillingFeatureResult:
    """
    An Application Insights component billing features
    """
    def __init__(__self__, current_billing_features=None, data_volume_cap=None):
        if current_billing_features and not isinstance(current_billing_features, list):
            raise TypeError("Expected argument 'current_billing_features' to be a list")
        pulumi.set(__self__, "current_billing_features", current_billing_features)
        if data_volume_cap and not isinstance(data_volume_cap, dict):
            raise TypeError("Expected argument 'data_volume_cap' to be a dict")
        pulumi.set(__self__, "data_volume_cap", data_volume_cap)

    @property
    @pulumi.getter(name="currentBillingFeatures")
    def current_billing_features(self) -> Optional[Sequence[str]]:
        """
        Current enabled pricing plan. When the component is in the Enterprise plan, this will list both 'Basic' and 'Application Insights Enterprise'.
        """
        return pulumi.get(self, "current_billing_features")

    @property
    @pulumi.getter(name="dataVolumeCap")
    def data_volume_cap(self) -> Optional['outputs.ApplicationInsightsComponentDataVolumeCapResponse']:
        """
        An Application Insights component daily data volume cap
        """
        return pulumi.get(self, "data_volume_cap")


class AwaitableGetComponentCurrentBillingFeatureResult(GetComponentCurrentBillingFeatureResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetComponentCurrentBillingFeatureResult(
            current_billing_features=self.current_billing_features,
            data_volume_cap=self.data_volume_cap)


def get_component_current_billing_feature(resource_group_name: Optional[str] = None,
                                          resource_name: Optional[str] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetComponentCurrentBillingFeatureResult:
    """
    Returns current billing features for an Application Insights component.
    Azure REST API version: 2015-05-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights:getComponentCurrentBillingFeature', __args__, opts=opts, typ=GetComponentCurrentBillingFeatureResult).value

    return AwaitableGetComponentCurrentBillingFeatureResult(
        current_billing_features=pulumi.get(__ret__, 'current_billing_features'),
        data_volume_cap=pulumi.get(__ret__, 'data_volume_cap'))


@_utilities.lift_output_func(get_component_current_billing_feature)
def get_component_current_billing_feature_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                 resource_name: Optional[pulumi.Input[str]] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetComponentCurrentBillingFeatureResult]:
    """
    Returns current billing features for an Application Insights component.
    Azure REST API version: 2015-05-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    """
    ...
