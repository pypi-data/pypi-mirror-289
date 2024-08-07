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
    'ListStaticSiteBuildFunctionAppSettingsResult',
    'AwaitableListStaticSiteBuildFunctionAppSettingsResult',
    'list_static_site_build_function_app_settings',
    'list_static_site_build_function_app_settings_output',
]

@pulumi.output_type
class ListStaticSiteBuildFunctionAppSettingsResult:
    """
    String dictionary resource.
    """
    def __init__(__self__, id=None, kind=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Mapping[str, str]:
        """
        Settings.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableListStaticSiteBuildFunctionAppSettingsResult(ListStaticSiteBuildFunctionAppSettingsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListStaticSiteBuildFunctionAppSettingsResult(
            id=self.id,
            kind=self.kind,
            name=self.name,
            properties=self.properties,
            type=self.type)


def list_static_site_build_function_app_settings(environment_name: Optional[str] = None,
                                                 name: Optional[str] = None,
                                                 resource_group_name: Optional[str] = None,
                                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListStaticSiteBuildFunctionAppSettingsResult:
    """
    Description for Gets the application settings of a static site build.


    :param str environment_name: The stage site identifier.
    :param str name: Name of the static site.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20220901:listStaticSiteBuildFunctionAppSettings', __args__, opts=opts, typ=ListStaticSiteBuildFunctionAppSettingsResult).value

    return AwaitableListStaticSiteBuildFunctionAppSettingsResult(
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        properties=pulumi.get(__ret__, 'properties'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(list_static_site_build_function_app_settings)
def list_static_site_build_function_app_settings_output(environment_name: Optional[pulumi.Input[str]] = None,
                                                        name: Optional[pulumi.Input[str]] = None,
                                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListStaticSiteBuildFunctionAppSettingsResult]:
    """
    Description for Gets the application settings of a static site build.


    :param str environment_name: The stage site identifier.
    :param str name: Name of the static site.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
