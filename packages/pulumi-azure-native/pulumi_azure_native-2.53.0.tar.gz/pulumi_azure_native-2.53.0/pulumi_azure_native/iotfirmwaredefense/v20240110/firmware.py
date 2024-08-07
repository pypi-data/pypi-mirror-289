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
from ._enums import *
from ._inputs import *

__all__ = ['FirmwareArgs', 'Firmware']

@pulumi.input_type
class FirmwareArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 file_name: Optional[pulumi.Input[str]] = None,
                 file_size: Optional[pulumi.Input[float]] = None,
                 firmware_id: Optional[pulumi.Input[str]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'Status']]] = None,
                 status_messages: Optional[pulumi.Input[Sequence[pulumi.Input['StatusMessageArgs']]]] = None,
                 vendor: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Firmware resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the firmware analysis workspace.
        :param pulumi.Input[str] description: User-specified description of the firmware.
        :param pulumi.Input[str] file_name: File name for a firmware that user uploaded.
        :param pulumi.Input[float] file_size: File size of the uploaded firmware image.
        :param pulumi.Input[str] firmware_id: The id of the firmware.
        :param pulumi.Input[str] model: Firmware model.
        :param pulumi.Input[Union[str, 'Status']] status: The status of firmware scan.
        :param pulumi.Input[Sequence[pulumi.Input['StatusMessageArgs']]] status_messages: A list of errors or other messages generated during firmware analysis
        :param pulumi.Input[str] vendor: Firmware vendor.
        :param pulumi.Input[str] version: Firmware version.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if file_name is not None:
            pulumi.set(__self__, "file_name", file_name)
        if file_size is not None:
            pulumi.set(__self__, "file_size", file_size)
        if firmware_id is not None:
            pulumi.set(__self__, "firmware_id", firmware_id)
        if model is not None:
            pulumi.set(__self__, "model", model)
        if status is None:
            status = 'Pending'
        if status is not None:
            pulumi.set(__self__, "status", status)
        if status_messages is not None:
            pulumi.set(__self__, "status_messages", status_messages)
        if vendor is not None:
            pulumi.set(__self__, "vendor", vendor)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the firmware analysis workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        User-specified description of the firmware.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[pulumi.Input[str]]:
        """
        File name for a firmware that user uploaded.
        """
        return pulumi.get(self, "file_name")

    @file_name.setter
    def file_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_name", value)

    @property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> Optional[pulumi.Input[float]]:
        """
        File size of the uploaded firmware image.
        """
        return pulumi.get(self, "file_size")

    @file_size.setter
    def file_size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "file_size", value)

    @property
    @pulumi.getter(name="firmwareId")
    def firmware_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id of the firmware.
        """
        return pulumi.get(self, "firmware_id")

    @firmware_id.setter
    def firmware_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "firmware_id", value)

    @property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[str]]:
        """
        Firmware model.
        """
        return pulumi.get(self, "model")

    @model.setter
    def model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'Status']]]:
        """
        The status of firmware scan.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'Status']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="statusMessages")
    def status_messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['StatusMessageArgs']]]]:
        """
        A list of errors or other messages generated during firmware analysis
        """
        return pulumi.get(self, "status_messages")

    @status_messages.setter
    def status_messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['StatusMessageArgs']]]]):
        pulumi.set(self, "status_messages", value)

    @property
    @pulumi.getter
    def vendor(self) -> Optional[pulumi.Input[str]]:
        """
        Firmware vendor.
        """
        return pulumi.get(self, "vendor")

    @vendor.setter
    def vendor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vendor", value)

    @property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[str]]:
        """
        Firmware version.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version", value)


class Firmware(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 file_name: Optional[pulumi.Input[str]] = None,
                 file_size: Optional[pulumi.Input[float]] = None,
                 firmware_id: Optional[pulumi.Input[str]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'Status']]] = None,
                 status_messages: Optional[pulumi.Input[Sequence[pulumi.Input[Union['StatusMessageArgs', 'StatusMessageArgsDict']]]]] = None,
                 vendor: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Firmware definition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: User-specified description of the firmware.
        :param pulumi.Input[str] file_name: File name for a firmware that user uploaded.
        :param pulumi.Input[float] file_size: File size of the uploaded firmware image.
        :param pulumi.Input[str] firmware_id: The id of the firmware.
        :param pulumi.Input[str] model: Firmware model.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'Status']] status: The status of firmware scan.
        :param pulumi.Input[Sequence[pulumi.Input[Union['StatusMessageArgs', 'StatusMessageArgsDict']]]] status_messages: A list of errors or other messages generated during firmware analysis
        :param pulumi.Input[str] vendor: Firmware vendor.
        :param pulumi.Input[str] version: Firmware version.
        :param pulumi.Input[str] workspace_name: The name of the firmware analysis workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FirmwareArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Firmware definition

        :param str resource_name: The name of the resource.
        :param FirmwareArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FirmwareArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 file_name: Optional[pulumi.Input[str]] = None,
                 file_size: Optional[pulumi.Input[float]] = None,
                 firmware_id: Optional[pulumi.Input[str]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'Status']]] = None,
                 status_messages: Optional[pulumi.Input[Sequence[pulumi.Input[Union['StatusMessageArgs', 'StatusMessageArgsDict']]]]] = None,
                 vendor: Optional[pulumi.Input[str]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FirmwareArgs.__new__(FirmwareArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["file_name"] = file_name
            __props__.__dict__["file_size"] = file_size
            __props__.__dict__["firmware_id"] = firmware_id
            __props__.__dict__["model"] = model
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if status is None:
                status = 'Pending'
            __props__.__dict__["status"] = status
            __props__.__dict__["status_messages"] = status_messages
            __props__.__dict__["vendor"] = vendor
            __props__.__dict__["version"] = version
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:iotfirmwaredefense:Firmware"), pulumi.Alias(type_="azure-native:iotfirmwaredefense/v20230208preview:Firmware")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Firmware, __self__).__init__(
            'azure-native:iotfirmwaredefense/v20240110:Firmware',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Firmware':
        """
        Get an existing Firmware resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FirmwareArgs.__new__(FirmwareArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["file_name"] = None
        __props__.__dict__["file_size"] = None
        __props__.__dict__["model"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["status_messages"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vendor"] = None
        __props__.__dict__["version"] = None
        return Firmware(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        User-specified description of the firmware.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="fileName")
    def file_name(self) -> pulumi.Output[Optional[str]]:
        """
        File name for a firmware that user uploaded.
        """
        return pulumi.get(self, "file_name")

    @property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> pulumi.Output[Optional[float]]:
        """
        File size of the uploaded firmware image.
        """
        return pulumi.get(self, "file_size")

    @property
    @pulumi.getter
    def model(self) -> pulumi.Output[Optional[str]]:
        """
        Firmware model.
        """
        return pulumi.get(self, "model")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of firmware scan.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessages")
    def status_messages(self) -> pulumi.Output[Optional[Sequence['outputs.StatusMessageResponse']]]:
        """
        A list of errors or other messages generated during firmware analysis
        """
        return pulumi.get(self, "status_messages")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def vendor(self) -> pulumi.Output[Optional[str]]:
        """
        Firmware vendor.
        """
        return pulumi.get(self, "vendor")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[Optional[str]]:
        """
        Firmware version.
        """
        return pulumi.get(self, "version")

