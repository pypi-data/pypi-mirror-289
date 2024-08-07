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
    'GetSettingResult',
    'AwaitableGetSettingResult',
    'get_setting',
    'get_setting_output',
]

@pulumi.output_type
class GetSettingResult:
    """
    State of the myscope setting.
    """
    def __init__(__self__, cache=None, id=None, kind=None, name=None, scope=None, start_on=None, type=None):
        if cache and not isinstance(cache, list):
            raise TypeError("Expected argument 'cache' to be a list")
        pulumi.set(__self__, "cache", cache)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if start_on and not isinstance(start_on, str):
            raise TypeError("Expected argument 'start_on' to be a str")
        pulumi.set(__self__, "start_on", start_on)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def cache(self) -> Optional[Sequence['outputs.SettingsPropertiesResponseCache']]:
        """
        Array of scopes with additional details used by Cost Management in the Azure portal.
        """
        return pulumi.get(self, "cache")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Resource kind.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scope(self) -> str:
        """
        Sets the default scope the current user will see when they sign into Azure Cost Management in the Azure portal.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="startOn")
    def start_on(self) -> Optional[str]:
        """
        Indicates what scope Cost Management in the Azure portal should default to. Allowed values: LastUsed.
        """
        return pulumi.get(self, "start_on")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetSettingResult(GetSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSettingResult(
            cache=self.cache,
            id=self.id,
            kind=self.kind,
            name=self.name,
            scope=self.scope,
            start_on=self.start_on,
            type=self.type)


def get_setting(setting_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSettingResult:
    """
    Retrieves the current value for a specific setting.
    Azure REST API version: 2019-11-01.


    :param str setting_name: Name of the setting. Allowed values: myscope
    """
    __args__ = dict()
    __args__['settingName'] = setting_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:costmanagement:getSetting', __args__, opts=opts, typ=GetSettingResult).value

    return AwaitableGetSettingResult(
        cache=pulumi.get(__ret__, 'cache'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        scope=pulumi.get(__ret__, 'scope'),
        start_on=pulumi.get(__ret__, 'start_on'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_setting)
def get_setting_output(setting_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSettingResult]:
    """
    Retrieves the current value for a specific setting.
    Azure REST API version: 2019-11-01.


    :param str setting_name: Name of the setting. Allowed values: myscope
    """
    ...
