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
    'GetSAPDatabaseInstanceResult',
    'AwaitableGetSAPDatabaseInstanceResult',
    'get_sap_database_instance',
    'get_sap_database_instance_output',
]

@pulumi.output_type
class GetSAPDatabaseInstanceResult:
    """
    Define the Database resource.
    """
    def __init__(__self__, database_sid=None, database_type=None, errors=None, id=None, ip_address=None, load_balancer_details=None, location=None, name=None, provisioning_state=None, status=None, subnet=None, system_data=None, tags=None, type=None, vm_details=None):
        if database_sid and not isinstance(database_sid, str):
            raise TypeError("Expected argument 'database_sid' to be a str")
        pulumi.set(__self__, "database_sid", database_sid)
        if database_type and not isinstance(database_type, str):
            raise TypeError("Expected argument 'database_type' to be a str")
        pulumi.set(__self__, "database_type", database_type)
        if errors and not isinstance(errors, dict):
            raise TypeError("Expected argument 'errors' to be a dict")
        pulumi.set(__self__, "errors", errors)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        pulumi.set(__self__, "ip_address", ip_address)
        if load_balancer_details and not isinstance(load_balancer_details, dict):
            raise TypeError("Expected argument 'load_balancer_details' to be a dict")
        pulumi.set(__self__, "load_balancer_details", load_balancer_details)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subnet and not isinstance(subnet, str):
            raise TypeError("Expected argument 'subnet' to be a str")
        pulumi.set(__self__, "subnet", subnet)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vm_details and not isinstance(vm_details, list):
            raise TypeError("Expected argument 'vm_details' to be a list")
        pulumi.set(__self__, "vm_details", vm_details)

    @property
    @pulumi.getter(name="databaseSid")
    def database_sid(self) -> str:
        """
        Database SID name.
        """
        return pulumi.get(self, "database_sid")

    @property
    @pulumi.getter(name="databaseType")
    def database_type(self) -> str:
        """
        Database type, that is if the DB is HANA, DB2, Oracle, SAP ASE, Max DB or MS SQL Server.
        """
        return pulumi.get(self, "database_type")

    @property
    @pulumi.getter
    def errors(self) -> 'outputs.SAPVirtualInstanceErrorResponse':
        """
        Defines the errors related to Database resource.
        """
        return pulumi.get(self, "errors")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> str:
        """
        Database IP Address.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="loadBalancerDetails")
    def load_balancer_details(self) -> 'outputs.LoadBalancerDetailsResponse':
        """
        The Load Balancer details such as LoadBalancer ID attached to Database Virtual Machines
        """
        return pulumi.get(self, "load_balancer_details")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

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
        Defines the provisioning states.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Defines the SAP Instance status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def subnet(self) -> str:
        """
        Database subnet.
        """
        return pulumi.get(self, "subnet")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmDetails")
    def vm_details(self) -> Sequence['outputs.DatabaseVmDetailsResponse']:
        """
        The list of virtual machines corresponding to the Database resource.
        """
        return pulumi.get(self, "vm_details")


class AwaitableGetSAPDatabaseInstanceResult(GetSAPDatabaseInstanceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSAPDatabaseInstanceResult(
            database_sid=self.database_sid,
            database_type=self.database_type,
            errors=self.errors,
            id=self.id,
            ip_address=self.ip_address,
            load_balancer_details=self.load_balancer_details,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            status=self.status,
            subnet=self.subnet,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vm_details=self.vm_details)


def get_sap_database_instance(database_instance_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              sap_virtual_instance_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSAPDatabaseInstanceResult:
    """
    Gets the SAP Database Instance resource.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2023-10-01-preview.


    :param str database_instance_name: Database resource name string modeled as parameter for auto generation to work correctly.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sap_virtual_instance_name: The name of the Virtual Instances for SAP solutions resource
    """
    __args__ = dict()
    __args__['databaseInstanceName'] = database_instance_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['sapVirtualInstanceName'] = sap_virtual_instance_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:workloads:getSAPDatabaseInstance', __args__, opts=opts, typ=GetSAPDatabaseInstanceResult).value

    return AwaitableGetSAPDatabaseInstanceResult(
        database_sid=pulumi.get(__ret__, 'database_sid'),
        database_type=pulumi.get(__ret__, 'database_type'),
        errors=pulumi.get(__ret__, 'errors'),
        id=pulumi.get(__ret__, 'id'),
        ip_address=pulumi.get(__ret__, 'ip_address'),
        load_balancer_details=pulumi.get(__ret__, 'load_balancer_details'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        status=pulumi.get(__ret__, 'status'),
        subnet=pulumi.get(__ret__, 'subnet'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        vm_details=pulumi.get(__ret__, 'vm_details'))


@_utilities.lift_output_func(get_sap_database_instance)
def get_sap_database_instance_output(database_instance_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     sap_virtual_instance_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSAPDatabaseInstanceResult]:
    """
    Gets the SAP Database Instance resource.
    Azure REST API version: 2023-04-01.

    Other available API versions: 2023-10-01-preview.


    :param str database_instance_name: Database resource name string modeled as parameter for auto generation to work correctly.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sap_virtual_instance_name: The name of the Virtual Instances for SAP solutions resource
    """
    ...
