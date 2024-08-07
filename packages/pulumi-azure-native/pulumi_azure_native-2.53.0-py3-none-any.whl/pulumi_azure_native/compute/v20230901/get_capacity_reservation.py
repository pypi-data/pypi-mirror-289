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
    'GetCapacityReservationResult',
    'AwaitableGetCapacityReservationResult',
    'get_capacity_reservation',
    'get_capacity_reservation_output',
]

@pulumi.output_type
class GetCapacityReservationResult:
    """
    Specifies information about the capacity reservation.
    """
    def __init__(__self__, id=None, instance_view=None, location=None, name=None, platform_fault_domain_count=None, provisioning_state=None, provisioning_time=None, reservation_id=None, sku=None, tags=None, time_created=None, type=None, virtual_machines_associated=None, zones=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_view and not isinstance(instance_view, dict):
            raise TypeError("Expected argument 'instance_view' to be a dict")
        pulumi.set(__self__, "instance_view", instance_view)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if platform_fault_domain_count and not isinstance(platform_fault_domain_count, int):
            raise TypeError("Expected argument 'platform_fault_domain_count' to be a int")
        pulumi.set(__self__, "platform_fault_domain_count", platform_fault_domain_count)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if provisioning_time and not isinstance(provisioning_time, str):
            raise TypeError("Expected argument 'provisioning_time' to be a str")
        pulumi.set(__self__, "provisioning_time", provisioning_time)
        if reservation_id and not isinstance(reservation_id, str):
            raise TypeError("Expected argument 'reservation_id' to be a str")
        pulumi.set(__self__, "reservation_id", reservation_id)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_machines_associated and not isinstance(virtual_machines_associated, list):
            raise TypeError("Expected argument 'virtual_machines_associated' to be a list")
        pulumi.set(__self__, "virtual_machines_associated", virtual_machines_associated)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> 'outputs.CapacityReservationInstanceViewResponse':
        """
        The Capacity reservation instance view.
        """
        return pulumi.get(self, "instance_view")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="platformFaultDomainCount")
    def platform_fault_domain_count(self) -> int:
        """
        Specifies the value of fault domain count that Capacity Reservation supports for requested VM size. **Note:** The fault domain count specified for a resource (like virtual machines scale set) must be less than or equal to this value if it deploys using capacity reservation. Minimum api-version: 2022-08-01.
        """
        return pulumi.get(self, "platform_fault_domain_count")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="provisioningTime")
    def provisioning_time(self) -> str:
        """
        The date time when the capacity reservation was last updated.
        """
        return pulumi.get(self, "provisioning_time")

    @property
    @pulumi.getter(name="reservationId")
    def reservation_id(self) -> str:
        """
        A unique id generated and assigned to the capacity reservation by the platform which does not change throughout the lifetime of the resource.
        """
        return pulumi.get(self, "reservation_id")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        SKU of the resource for which capacity needs be reserved. The SKU name and capacity is required to be set. Currently VM Skus with the capability called 'CapacityReservationSupported' set to true are supported. Refer to List Microsoft.Compute SKUs in a region (https://docs.microsoft.com/rest/api/compute/resourceskus/list) for supported values.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        Specifies the time at which the Capacity Reservation resource was created. Minimum api-version: 2021-11-01.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualMachinesAssociated")
    def virtual_machines_associated(self) -> Sequence['outputs.SubResourceReadOnlyResponse']:
        """
        A list of all virtual machine resource ids that are associated with the capacity reservation.
        """
        return pulumi.get(self, "virtual_machines_associated")

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        Availability Zone to use for this capacity reservation. The zone has to be single value and also should be part for the list of zones specified during the capacity reservation group creation. The zone can be assigned only during creation. If not provided, the reservation supports only non-zonal deployments. If provided, enforces VM/VMSS using this capacity reservation to be in same zone.
        """
        return pulumi.get(self, "zones")


class AwaitableGetCapacityReservationResult(GetCapacityReservationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCapacityReservationResult(
            id=self.id,
            instance_view=self.instance_view,
            location=self.location,
            name=self.name,
            platform_fault_domain_count=self.platform_fault_domain_count,
            provisioning_state=self.provisioning_state,
            provisioning_time=self.provisioning_time,
            reservation_id=self.reservation_id,
            sku=self.sku,
            tags=self.tags,
            time_created=self.time_created,
            type=self.type,
            virtual_machines_associated=self.virtual_machines_associated,
            zones=self.zones)


def get_capacity_reservation(capacity_reservation_group_name: Optional[str] = None,
                             capacity_reservation_name: Optional[str] = None,
                             expand: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCapacityReservationResult:
    """
    The operation that retrieves information about the capacity reservation.


    :param str capacity_reservation_group_name: The name of the capacity reservation group.
    :param str capacity_reservation_name: The name of the capacity reservation.
    :param str expand: The expand expression to apply on the operation. 'InstanceView' retrieves a snapshot of the runtime properties of the capacity reservation that is managed by the platform and can change outside of control plane operations.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['capacityReservationGroupName'] = capacity_reservation_group_name
    __args__['capacityReservationName'] = capacity_reservation_name
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20230901:getCapacityReservation', __args__, opts=opts, typ=GetCapacityReservationResult).value

    return AwaitableGetCapacityReservationResult(
        id=pulumi.get(__ret__, 'id'),
        instance_view=pulumi.get(__ret__, 'instance_view'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        platform_fault_domain_count=pulumi.get(__ret__, 'platform_fault_domain_count'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        provisioning_time=pulumi.get(__ret__, 'provisioning_time'),
        reservation_id=pulumi.get(__ret__, 'reservation_id'),
        sku=pulumi.get(__ret__, 'sku'),
        tags=pulumi.get(__ret__, 'tags'),
        time_created=pulumi.get(__ret__, 'time_created'),
        type=pulumi.get(__ret__, 'type'),
        virtual_machines_associated=pulumi.get(__ret__, 'virtual_machines_associated'),
        zones=pulumi.get(__ret__, 'zones'))


@_utilities.lift_output_func(get_capacity_reservation)
def get_capacity_reservation_output(capacity_reservation_group_name: Optional[pulumi.Input[str]] = None,
                                    capacity_reservation_name: Optional[pulumi.Input[str]] = None,
                                    expand: Optional[pulumi.Input[Optional[str]]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCapacityReservationResult]:
    """
    The operation that retrieves information about the capacity reservation.


    :param str capacity_reservation_group_name: The name of the capacity reservation group.
    :param str capacity_reservation_name: The name of the capacity reservation.
    :param str expand: The expand expression to apply on the operation. 'InstanceView' retrieves a snapshot of the runtime properties of the capacity reservation that is managed by the platform and can change outside of control plane operations.
    :param str resource_group_name: The name of the resource group.
    """
    ...
