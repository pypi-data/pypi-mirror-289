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
    'GetDeviceGroupResult',
    'AwaitableGetDeviceGroupResult',
    'get_device_group',
    'get_device_group_output',
]

@pulumi.output_type
class GetDeviceGroupResult:
    """
    An device group resource belonging to a product resource.
    """
    def __init__(__self__, allow_crash_dumps_collection=None, description=None, has_deployment=None, id=None, name=None, os_feed_type=None, provisioning_state=None, regional_data_boundary=None, system_data=None, type=None, update_policy=None):
        if allow_crash_dumps_collection and not isinstance(allow_crash_dumps_collection, str):
            raise TypeError("Expected argument 'allow_crash_dumps_collection' to be a str")
        pulumi.set(__self__, "allow_crash_dumps_collection", allow_crash_dumps_collection)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if has_deployment and not isinstance(has_deployment, bool):
            raise TypeError("Expected argument 'has_deployment' to be a bool")
        pulumi.set(__self__, "has_deployment", has_deployment)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_feed_type and not isinstance(os_feed_type, str):
            raise TypeError("Expected argument 'os_feed_type' to be a str")
        pulumi.set(__self__, "os_feed_type", os_feed_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if regional_data_boundary and not isinstance(regional_data_boundary, str):
            raise TypeError("Expected argument 'regional_data_boundary' to be a str")
        pulumi.set(__self__, "regional_data_boundary", regional_data_boundary)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if update_policy and not isinstance(update_policy, str):
            raise TypeError("Expected argument 'update_policy' to be a str")
        pulumi.set(__self__, "update_policy", update_policy)

    @property
    @pulumi.getter(name="allowCrashDumpsCollection")
    def allow_crash_dumps_collection(self) -> Optional[str]:
        """
        Flag to define if the user allows for crash dump collection.
        """
        return pulumi.get(self, "allow_crash_dumps_collection")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the device group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="hasDeployment")
    def has_deployment(self) -> bool:
        """
        Deployment status for the device group.
        """
        return pulumi.get(self, "has_deployment")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osFeedType")
    def os_feed_type(self) -> Optional[str]:
        """
        Operating system feed type of the device group.
        """
        return pulumi.get(self, "os_feed_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="regionalDataBoundary")
    def regional_data_boundary(self) -> Optional[str]:
        """
        Regional data boundary for the device group.
        """
        return pulumi.get(self, "regional_data_boundary")

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
    @pulumi.getter(name="updatePolicy")
    def update_policy(self) -> Optional[str]:
        """
        Update policy of the device group.
        """
        return pulumi.get(self, "update_policy")


class AwaitableGetDeviceGroupResult(GetDeviceGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDeviceGroupResult(
            allow_crash_dumps_collection=self.allow_crash_dumps_collection,
            description=self.description,
            has_deployment=self.has_deployment,
            id=self.id,
            name=self.name,
            os_feed_type=self.os_feed_type,
            provisioning_state=self.provisioning_state,
            regional_data_boundary=self.regional_data_boundary,
            system_data=self.system_data,
            type=self.type,
            update_policy=self.update_policy)


def get_device_group(catalog_name: Optional[str] = None,
                     device_group_name: Optional[str] = None,
                     product_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDeviceGroupResult:
    """
    Get a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.


    :param str catalog_name: Name of catalog
    :param str device_group_name: Name of device group.
    :param str product_name: Name of product.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['catalogName'] = catalog_name
    __args__['deviceGroupName'] = device_group_name
    __args__['productName'] = product_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azuresphere/v20220901preview:getDeviceGroup', __args__, opts=opts, typ=GetDeviceGroupResult).value

    return AwaitableGetDeviceGroupResult(
        allow_crash_dumps_collection=pulumi.get(__ret__, 'allow_crash_dumps_collection'),
        description=pulumi.get(__ret__, 'description'),
        has_deployment=pulumi.get(__ret__, 'has_deployment'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        os_feed_type=pulumi.get(__ret__, 'os_feed_type'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        regional_data_boundary=pulumi.get(__ret__, 'regional_data_boundary'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'),
        update_policy=pulumi.get(__ret__, 'update_policy'))


@_utilities.lift_output_func(get_device_group)
def get_device_group_output(catalog_name: Optional[pulumi.Input[str]] = None,
                            device_group_name: Optional[pulumi.Input[str]] = None,
                            product_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDeviceGroupResult]:
    """
    Get a DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name.


    :param str catalog_name: Name of catalog
    :param str device_group_name: Name of device group.
    :param str product_name: Name of product.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
