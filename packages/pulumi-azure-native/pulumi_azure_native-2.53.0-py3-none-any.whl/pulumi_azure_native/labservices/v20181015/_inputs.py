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
from ._enums import *

__all__ = [
    'ReferenceVmArgs',
    'ReferenceVmArgsDict',
    'ResourceSettingsArgs',
    'ResourceSettingsArgsDict',
    'ResourceSetArgs',
    'ResourceSetArgsDict',
]

MYPY = False

if not MYPY:
    class ReferenceVmArgsDict(TypedDict):
        """
        Details of a Reference Vm
        """
        user_name: pulumi.Input[str]
        """
        The username of the virtual machine
        """
        password: NotRequired[pulumi.Input[str]]
        """
        The password of the virtual machine. This will be set to null in GET resource API
        """
elif False:
    ReferenceVmArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ReferenceVmArgs:
    def __init__(__self__, *,
                 user_name: pulumi.Input[str],
                 password: Optional[pulumi.Input[str]] = None):
        """
        Details of a Reference Vm
        :param pulumi.Input[str] user_name: The username of the virtual machine
        :param pulumi.Input[str] password: The password of the virtual machine. This will be set to null in GET resource API
        """
        pulumi.set(__self__, "user_name", user_name)
        if password is not None:
            pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[str]:
        """
        The username of the virtual machine
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password of the virtual machine. This will be set to null in GET resource API
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)


if not MYPY:
    class ResourceSettingsArgsDict(TypedDict):
        """
        Represents resource specific settings
        """
        reference_vm: pulumi.Input['ReferenceVmArgsDict']
        """
        Details specific to Reference Vm
        """
        gallery_image_resource_id: NotRequired[pulumi.Input[str]]
        """
        The resource id of the gallery image used for creating the virtual machine
        """
        size: NotRequired[pulumi.Input[Union[str, 'ManagedLabVmSize']]]
        """
        The size of the virtual machine
        """
elif False:
    ResourceSettingsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ResourceSettingsArgs:
    def __init__(__self__, *,
                 reference_vm: pulumi.Input['ReferenceVmArgs'],
                 gallery_image_resource_id: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[Union[str, 'ManagedLabVmSize']]] = None):
        """
        Represents resource specific settings
        :param pulumi.Input['ReferenceVmArgs'] reference_vm: Details specific to Reference Vm
        :param pulumi.Input[str] gallery_image_resource_id: The resource id of the gallery image used for creating the virtual machine
        :param pulumi.Input[Union[str, 'ManagedLabVmSize']] size: The size of the virtual machine
        """
        pulumi.set(__self__, "reference_vm", reference_vm)
        if gallery_image_resource_id is not None:
            pulumi.set(__self__, "gallery_image_resource_id", gallery_image_resource_id)
        if size is not None:
            pulumi.set(__self__, "size", size)

    @property
    @pulumi.getter(name="referenceVm")
    def reference_vm(self) -> pulumi.Input['ReferenceVmArgs']:
        """
        Details specific to Reference Vm
        """
        return pulumi.get(self, "reference_vm")

    @reference_vm.setter
    def reference_vm(self, value: pulumi.Input['ReferenceVmArgs']):
        pulumi.set(self, "reference_vm", value)

    @property
    @pulumi.getter(name="galleryImageResourceId")
    def gallery_image_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of the gallery image used for creating the virtual machine
        """
        return pulumi.get(self, "gallery_image_resource_id")

    @gallery_image_resource_id.setter
    def gallery_image_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gallery_image_resource_id", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[Union[str, 'ManagedLabVmSize']]]:
        """
        The size of the virtual machine
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[Union[str, 'ManagedLabVmSize']]]):
        pulumi.set(self, "size", value)


if not MYPY:
    class ResourceSetArgsDict(TypedDict):
        """
        Represents a VM and the setting Id it was created for.
        """
        resource_setting_id: NotRequired[pulumi.Input[str]]
        """
        resourceSettingId for the environment
        """
        vm_resource_id: NotRequired[pulumi.Input[str]]
        """
        VM resource Id for the environment
        """
elif False:
    ResourceSetArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ResourceSetArgs:
    def __init__(__self__, *,
                 resource_setting_id: Optional[pulumi.Input[str]] = None,
                 vm_resource_id: Optional[pulumi.Input[str]] = None):
        """
        Represents a VM and the setting Id it was created for.
        :param pulumi.Input[str] resource_setting_id: resourceSettingId for the environment
        :param pulumi.Input[str] vm_resource_id: VM resource Id for the environment
        """
        if resource_setting_id is not None:
            pulumi.set(__self__, "resource_setting_id", resource_setting_id)
        if vm_resource_id is not None:
            pulumi.set(__self__, "vm_resource_id", vm_resource_id)

    @property
    @pulumi.getter(name="resourceSettingId")
    def resource_setting_id(self) -> Optional[pulumi.Input[str]]:
        """
        resourceSettingId for the environment
        """
        return pulumi.get(self, "resource_setting_id")

    @resource_setting_id.setter
    def resource_setting_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_setting_id", value)

    @property
    @pulumi.getter(name="vmResourceId")
    def vm_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        VM resource Id for the environment
        """
        return pulumi.get(self, "vm_resource_id")

    @vm_resource_id.setter
    def vm_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vm_resource_id", value)


