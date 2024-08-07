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
    'GetDeviceResult',
    'AwaitableGetDeviceResult',
    'get_device',
    'get_device_output',
]

@pulumi.output_type
class GetDeviceResult:
    """
    An device resource belonging to a device group resource.
    """
    def __init__(__self__, chip_sku=None, device_id=None, id=None, last_available_os_version=None, last_installed_os_version=None, last_os_update_utc=None, last_update_request_utc=None, name=None, provisioning_state=None, system_data=None, type=None):
        if chip_sku and not isinstance(chip_sku, str):
            raise TypeError("Expected argument 'chip_sku' to be a str")
        pulumi.set(__self__, "chip_sku", chip_sku)
        if device_id and not isinstance(device_id, str):
            raise TypeError("Expected argument 'device_id' to be a str")
        pulumi.set(__self__, "device_id", device_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_available_os_version and not isinstance(last_available_os_version, str):
            raise TypeError("Expected argument 'last_available_os_version' to be a str")
        pulumi.set(__self__, "last_available_os_version", last_available_os_version)
        if last_installed_os_version and not isinstance(last_installed_os_version, str):
            raise TypeError("Expected argument 'last_installed_os_version' to be a str")
        pulumi.set(__self__, "last_installed_os_version", last_installed_os_version)
        if last_os_update_utc and not isinstance(last_os_update_utc, str):
            raise TypeError("Expected argument 'last_os_update_utc' to be a str")
        pulumi.set(__self__, "last_os_update_utc", last_os_update_utc)
        if last_update_request_utc and not isinstance(last_update_request_utc, str):
            raise TypeError("Expected argument 'last_update_request_utc' to be a str")
        pulumi.set(__self__, "last_update_request_utc", last_update_request_utc)
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
    @pulumi.getter(name="chipSku")
    def chip_sku(self) -> str:
        """
        SKU of the chip
        """
        return pulumi.get(self, "chip_sku")

    @property
    @pulumi.getter(name="deviceId")
    def device_id(self) -> Optional[str]:
        """
        Device ID
        """
        return pulumi.get(self, "device_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastAvailableOsVersion")
    def last_available_os_version(self) -> str:
        """
        OS version available for installation when update requested
        """
        return pulumi.get(self, "last_available_os_version")

    @property
    @pulumi.getter(name="lastInstalledOsVersion")
    def last_installed_os_version(self) -> str:
        """
        OS version running on device when update requested
        """
        return pulumi.get(self, "last_installed_os_version")

    @property
    @pulumi.getter(name="lastOsUpdateUtc")
    def last_os_update_utc(self) -> str:
        """
        Time when update requested and new OS version available
        """
        return pulumi.get(self, "last_os_update_utc")

    @property
    @pulumi.getter(name="lastUpdateRequestUtc")
    def last_update_request_utc(self) -> str:
        """
        Time when update was last requested
        """
        return pulumi.get(self, "last_update_request_utc")

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
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

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


class AwaitableGetDeviceResult(GetDeviceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeviceResult(
            chip_sku=self.chip_sku,
            device_id=self.device_id,
            id=self.id,
            last_available_os_version=self.last_available_os_version,
            last_installed_os_version=self.last_installed_os_version,
            last_os_update_utc=self.last_os_update_utc,
            last_update_request_utc=self.last_update_request_utc,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_device(catalog_name: Optional[str] = None,
               device_group_name: Optional[str] = None,
               device_name: Optional[str] = None,
               product_name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeviceResult:
    """
    Get a Device. Use '.unassigned' or '.default' for the device group and product names when a device does not belong to a device group and product.


    :param str catalog_name: Name of catalog
    :param str device_group_name: Name of device group.
    :param str device_name: Device name
    :param str product_name: Name of product.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['catalogName'] = catalog_name
    __args__['deviceGroupName'] = device_group_name
    __args__['deviceName'] = device_name
    __args__['productName'] = product_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azuresphere/v20220901preview:getDevice', __args__, opts=opts, typ=GetDeviceResult).value

    return AwaitableGetDeviceResult(
        chip_sku=pulumi.get(__ret__, 'chip_sku'),
        device_id=pulumi.get(__ret__, 'device_id'),
        id=pulumi.get(__ret__, 'id'),
        last_available_os_version=pulumi.get(__ret__, 'last_available_os_version'),
        last_installed_os_version=pulumi.get(__ret__, 'last_installed_os_version'),
        last_os_update_utc=pulumi.get(__ret__, 'last_os_update_utc'),
        last_update_request_utc=pulumi.get(__ret__, 'last_update_request_utc'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_device)
def get_device_output(catalog_name: Optional[pulumi.Input[str]] = None,
                      device_group_name: Optional[pulumi.Input[str]] = None,
                      device_name: Optional[pulumi.Input[str]] = None,
                      product_name: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeviceResult]:
    """
    Get a Device. Use '.unassigned' or '.default' for the device group and product names when a device does not belong to a device group and product.


    :param str catalog_name: Name of catalog
    :param str device_group_name: Name of device group.
    :param str device_name: Device name
    :param str product_name: Name of product.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
