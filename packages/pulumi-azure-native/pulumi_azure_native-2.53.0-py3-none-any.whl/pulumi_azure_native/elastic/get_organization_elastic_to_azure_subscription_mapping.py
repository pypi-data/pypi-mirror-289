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
    'GetOrganizationElasticToAzureSubscriptionMappingResult',
    'AwaitableGetOrganizationElasticToAzureSubscriptionMappingResult',
    'get_organization_elastic_to_azure_subscription_mapping',
    'get_organization_elastic_to_azure_subscription_mapping_output',
]

@pulumi.output_type
class GetOrganizationElasticToAzureSubscriptionMappingResult:
    """
    The Azure Subscription ID to which the Organization of the logged in user belongs and gets billed into.
    """
    def __init__(__self__, properties=None):
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.ElasticOrganizationToAzureSubscriptionMappingResponsePropertiesResponse':
        """
        The properties of Azure Subscription ID to which the Organization of the logged in user belongs and gets billed into.
        """
        return pulumi.get(self, "properties")


class AwaitableGetOrganizationElasticToAzureSubscriptionMappingResult(GetOrganizationElasticToAzureSubscriptionMappingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetOrganizationElasticToAzureSubscriptionMappingResult(
            properties=self.properties)


def get_organization_elastic_to_azure_subscription_mapping(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetOrganizationElasticToAzureSubscriptionMappingResult:
    """
    Get Elastic Organization To Azure Subscription Mapping details for the logged-in user.
    Azure REST API version: 2023-06-15-preview.

    Other available API versions: 2023-07-01-preview, 2023-10-01-preview, 2023-11-01-preview, 2024-01-01-preview, 2024-03-01, 2024-05-01-preview, 2024-06-15-preview.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:elastic:getOrganizationElasticToAzureSubscriptionMapping', __args__, opts=opts, typ=GetOrganizationElasticToAzureSubscriptionMappingResult).value

    return AwaitableGetOrganizationElasticToAzureSubscriptionMappingResult(
        properties=pulumi.get(__ret__, 'properties'))


@_utilities.lift_output_func(get_organization_elastic_to_azure_subscription_mapping)
def get_organization_elastic_to_azure_subscription_mapping_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetOrganizationElasticToAzureSubscriptionMappingResult]:
    """
    Get Elastic Organization To Azure Subscription Mapping details for the logged-in user.
    Azure REST API version: 2023-06-15-preview.

    Other available API versions: 2023-07-01-preview, 2023-10-01-preview, 2023-11-01-preview, 2024-01-01-preview, 2024-03-01, 2024-05-01-preview, 2024-06-15-preview.
    """
    ...
