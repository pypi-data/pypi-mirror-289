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
    'GetIntegrationRuntimeObjectMetadatumResult',
    'AwaitableGetIntegrationRuntimeObjectMetadatumResult',
    'get_integration_runtime_object_metadatum',
    'get_integration_runtime_object_metadatum_output',
]

@pulumi.output_type
class GetIntegrationRuntimeObjectMetadatumResult:
    """
    A list of SSIS object metadata.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        The link to the next page of results, if any remaining results exist.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence[Any]]:
        """
        List of SSIS object metadata.
        """
        return pulumi.get(self, "value")


class AwaitableGetIntegrationRuntimeObjectMetadatumResult(GetIntegrationRuntimeObjectMetadatumResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIntegrationRuntimeObjectMetadatumResult(
            next_link=self.next_link,
            value=self.value)


def get_integration_runtime_object_metadatum(factory_name: Optional[str] = None,
                                             integration_runtime_name: Optional[str] = None,
                                             metadata_path: Optional[str] = None,
                                             resource_group_name: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIntegrationRuntimeObjectMetadatumResult:
    """
    Get a SSIS integration runtime object metadata by specified path. The return is pageable metadata list.
    Azure REST API version: 2018-06-01.


    :param str factory_name: The factory name.
    :param str integration_runtime_name: The integration runtime name.
    :param str metadata_path: Metadata path.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['factoryName'] = factory_name
    __args__['integrationRuntimeName'] = integration_runtime_name
    __args__['metadataPath'] = metadata_path
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datafactory:getIntegrationRuntimeObjectMetadatum', __args__, opts=opts, typ=GetIntegrationRuntimeObjectMetadatumResult).value

    return AwaitableGetIntegrationRuntimeObjectMetadatumResult(
        next_link=pulumi.get(__ret__, 'next_link'),
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(get_integration_runtime_object_metadatum)
def get_integration_runtime_object_metadatum_output(factory_name: Optional[pulumi.Input[str]] = None,
                                                    integration_runtime_name: Optional[pulumi.Input[str]] = None,
                                                    metadata_path: Optional[pulumi.Input[Optional[str]]] = None,
                                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIntegrationRuntimeObjectMetadatumResult]:
    """
    Get a SSIS integration runtime object metadata by specified path. The return is pageable metadata list.
    Azure REST API version: 2018-06-01.


    :param str factory_name: The factory name.
    :param str integration_runtime_name: The integration runtime name.
    :param str metadata_path: Metadata path.
    :param str resource_group_name: The resource group name.
    """
    ...
