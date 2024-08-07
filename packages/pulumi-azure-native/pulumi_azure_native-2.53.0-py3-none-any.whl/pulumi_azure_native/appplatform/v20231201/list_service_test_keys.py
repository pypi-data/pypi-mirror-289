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
    'ListServiceTestKeysResult',
    'AwaitableListServiceTestKeysResult',
    'list_service_test_keys',
    'list_service_test_keys_output',
]

@pulumi.output_type
class ListServiceTestKeysResult:
    """
    Test keys payload
    """
    def __init__(__self__, enabled=None, primary_key=None, primary_test_endpoint=None, secondary_key=None, secondary_test_endpoint=None):
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if primary_test_endpoint and not isinstance(primary_test_endpoint, str):
            raise TypeError("Expected argument 'primary_test_endpoint' to be a str")
        pulumi.set(__self__, "primary_test_endpoint", primary_test_endpoint)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)
        if secondary_test_endpoint and not isinstance(secondary_test_endpoint, str):
            raise TypeError("Expected argument 'secondary_test_endpoint' to be a str")
        pulumi.set(__self__, "secondary_test_endpoint", secondary_test_endpoint)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Indicates whether the test endpoint feature enabled or not
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[str]:
        """
        Primary key
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="primaryTestEndpoint")
    def primary_test_endpoint(self) -> Optional[str]:
        """
        Primary test endpoint
        """
        return pulumi.get(self, "primary_test_endpoint")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[str]:
        """
        Secondary key
        """
        return pulumi.get(self, "secondary_key")

    @property
    @pulumi.getter(name="secondaryTestEndpoint")
    def secondary_test_endpoint(self) -> Optional[str]:
        """
        Secondary test endpoint
        """
        return pulumi.get(self, "secondary_test_endpoint")


class AwaitableListServiceTestKeysResult(ListServiceTestKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListServiceTestKeysResult(
            enabled=self.enabled,
            primary_key=self.primary_key,
            primary_test_endpoint=self.primary_test_endpoint,
            secondary_key=self.secondary_key,
            secondary_test_endpoint=self.secondary_test_endpoint)


def list_service_test_keys(resource_group_name: Optional[str] = None,
                           service_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListServiceTestKeysResult:
    """
    List test keys for a Service.


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:appplatform/v20231201:listServiceTestKeys', __args__, opts=opts, typ=ListServiceTestKeysResult).value

    return AwaitableListServiceTestKeysResult(
        enabled=pulumi.get(__ret__, 'enabled'),
        primary_key=pulumi.get(__ret__, 'primary_key'),
        primary_test_endpoint=pulumi.get(__ret__, 'primary_test_endpoint'),
        secondary_key=pulumi.get(__ret__, 'secondary_key'),
        secondary_test_endpoint=pulumi.get(__ret__, 'secondary_test_endpoint'))


@_utilities.lift_output_func(list_service_test_keys)
def list_service_test_keys_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                  service_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListServiceTestKeysResult]:
    """
    List test keys for a Service.


    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str service_name: The name of the Service resource.
    """
    ...
