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
    'GetKeyGroupResult',
    'AwaitableGetKeyGroupResult',
    'get_key_group',
    'get_key_group_output',
]

@pulumi.output_type
class GetKeyGroupResult:
    """
    Contains a list of references of UrlSigningKey type secret objects.
    """
    def __init__(__self__, deployment_status=None, id=None, key_references=None, name=None, provisioning_state=None, system_data=None, type=None):
        if deployment_status and not isinstance(deployment_status, str):
            raise TypeError("Expected argument 'deployment_status' to be a str")
        pulumi.set(__self__, "deployment_status", deployment_status)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_references and not isinstance(key_references, list):
            raise TypeError("Expected argument 'key_references' to be a list")
        pulumi.set(__self__, "key_references", key_references)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> str:
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyReferences")
    def key_references(self) -> Optional[Sequence['outputs.ResourceReferenceResponse']]:
        """
        Names of UrlSigningKey type secret objects
        """
        return pulumi.get(self, "key_references")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning status
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetKeyGroupResult(GetKeyGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyGroupResult(
            deployment_status=self.deployment_status,
            id=self.id,
            key_references=self.key_references,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_key_group(key_group_name: Optional[str] = None,
                  profile_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyGroupResult:
    """
    Gets an existing KeyGroup within a profile.


    :param str key_group_name: Name of the KeyGroup under the profile.
    :param str profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium which is unique within the resource group.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['keyGroupName'] = key_group_name
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cdn/v20240501preview:getKeyGroup', __args__, opts=opts, typ=GetKeyGroupResult).value

    return AwaitableGetKeyGroupResult(
        deployment_status=pulumi.get(__ret__, 'deployment_status'),
        id=pulumi.get(__ret__, 'id'),
        key_references=pulumi.get(__ret__, 'key_references'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_key_group)
def get_key_group_output(key_group_name: Optional[pulumi.Input[str]] = None,
                         profile_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKeyGroupResult]:
    """
    Gets an existing KeyGroup within a profile.


    :param str key_group_name: Name of the KeyGroup under the profile.
    :param str profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium which is unique within the resource group.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
