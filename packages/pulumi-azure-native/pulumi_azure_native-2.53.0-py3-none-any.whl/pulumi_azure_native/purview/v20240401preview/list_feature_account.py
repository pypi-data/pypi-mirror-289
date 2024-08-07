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
    'ListFeatureAccountResult',
    'AwaitableListFeatureAccountResult',
    'list_feature_account',
    'list_feature_account_output',
]

@pulumi.output_type
class ListFeatureAccountResult:
    """
    List of features with enabled status
    """
    def __init__(__self__, features=None):
        if features and not isinstance(features, dict):
            raise TypeError("Expected argument 'features' to be a dict")
        pulumi.set(__self__, "features", features)

    @property
    @pulumi.getter
    def features(self) -> Mapping[str, bool]:
        """
        Features with enabled status
        """
        return pulumi.get(self, "features")


class AwaitableListFeatureAccountResult(ListFeatureAccountResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListFeatureAccountResult(
            features=self.features)


def list_feature_account(account_name: Optional[str] = None,
                         features: Optional[Sequence[str]] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListFeatureAccountResult:
    """
    Gets details from a list of feature names.


    :param str account_name: The name of the account.
    :param Sequence[str] features: Set of features
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['features'] = features
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:purview/v20240401preview:listFeatureAccount', __args__, opts=opts, typ=ListFeatureAccountResult).value

    return AwaitableListFeatureAccountResult(
        features=pulumi.get(__ret__, 'features'))


@_utilities.lift_output_func(list_feature_account)
def list_feature_account_output(account_name: Optional[pulumi.Input[str]] = None,
                                features: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListFeatureAccountResult]:
    """
    Gets details from a list of feature names.


    :param str account_name: The name of the account.
    :param Sequence[str] features: Set of features
    :param str resource_group_name: The resource group name.
    """
    ...
