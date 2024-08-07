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
    'GetFirmwareResult',
    'AwaitableGetFirmwareResult',
    'get_firmware',
    'get_firmware_output',
]

@pulumi.output_type
class GetFirmwareResult:
    """
    Firmware definition
    """
    def __init__(__self__, description=None, file_name=None, file_size=None, id=None, model=None, name=None, provisioning_state=None, status=None, status_messages=None, system_data=None, type=None, vendor=None, version=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if file_name and not isinstance(file_name, str):
            raise TypeError("Expected argument 'file_name' to be a str")
        pulumi.set(__self__, "file_name", file_name)
        if file_size and not isinstance(file_size, float):
            raise TypeError("Expected argument 'file_size' to be a float")
        pulumi.set(__self__, "file_size", file_size)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if model and not isinstance(model, str):
            raise TypeError("Expected argument 'model' to be a str")
        pulumi.set(__self__, "model", model)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if status_messages and not isinstance(status_messages, list):
            raise TypeError("Expected argument 'status_messages' to be a list")
        pulumi.set(__self__, "status_messages", status_messages)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vendor and not isinstance(vendor, str):
            raise TypeError("Expected argument 'vendor' to be a str")
        pulumi.set(__self__, "vendor", vendor)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        User-specified description of the firmware.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[str]:
        """
        File name for a firmware that user uploaded.
        """
        return pulumi.get(self, "file_name")

    @property
    @pulumi.getter(name="fileSize")
    def file_size(self) -> Optional[float]:
        """
        File size of the uploaded firmware image.
        """
        return pulumi.get(self, "file_size")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def model(self) -> Optional[str]:
        """
        Firmware model.
        """
        return pulumi.get(self, "model")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of firmware scan.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="statusMessages")
    def status_messages(self) -> Optional[Sequence[Any]]:
        """
        A list of errors or other messages generated during firmware analysis
        """
        return pulumi.get(self, "status_messages")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def vendor(self) -> Optional[str]:
        """
        Firmware vendor.
        """
        return pulumi.get(self, "vendor")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        Firmware version.
        """
        return pulumi.get(self, "version")


class AwaitableGetFirmwareResult(GetFirmwareResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirmwareResult(
            description=self.description,
            file_name=self.file_name,
            file_size=self.file_size,
            id=self.id,
            model=self.model,
            name=self.name,
            provisioning_state=self.provisioning_state,
            status=self.status,
            status_messages=self.status_messages,
            system_data=self.system_data,
            type=self.type,
            vendor=self.vendor,
            version=self.version)


def get_firmware(firmware_id: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 workspace_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirmwareResult:
    """
    Get firmware.
    Azure REST API version: 2023-02-08-preview.

    Other available API versions: 2024-01-10.


    :param str firmware_id: The id of the firmware.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the firmware analysis workspace.
    """
    __args__ = dict()
    __args__['firmwareId'] = firmware_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:iotfirmwaredefense:getFirmware', __args__, opts=opts, typ=GetFirmwareResult).value

    return AwaitableGetFirmwareResult(
        description=pulumi.get(__ret__, 'description'),
        file_name=pulumi.get(__ret__, 'file_name'),
        file_size=pulumi.get(__ret__, 'file_size'),
        id=pulumi.get(__ret__, 'id'),
        model=pulumi.get(__ret__, 'model'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        status_messages=pulumi.get(__ret__, 'status_messages'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        vendor=pulumi.get(__ret__, 'vendor'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_firmware)
def get_firmware_output(firmware_id: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        workspace_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirmwareResult]:
    """
    Get firmware.
    Azure REST API version: 2023-02-08-preview.

    Other available API versions: 2024-01-10.


    :param str firmware_id: The id of the firmware.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the firmware analysis workspace.
    """
    ...
