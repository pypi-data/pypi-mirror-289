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
    'GetManagedServerDnsAliasResult',
    'AwaitableGetManagedServerDnsAliasResult',
    'get_managed_server_dns_alias',
    'get_managed_server_dns_alias_output',
]

@pulumi.output_type
class GetManagedServerDnsAliasResult:
    """
    A managed server DNS alias.
    """
    def __init__(__self__, azure_dns_record=None, id=None, name=None, public_azure_dns_record=None, type=None):
        if azure_dns_record and not isinstance(azure_dns_record, str):
            raise TypeError("Expected argument 'azure_dns_record' to be a str")
        pulumi.set(__self__, "azure_dns_record", azure_dns_record)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if public_azure_dns_record and not isinstance(public_azure_dns_record, str):
            raise TypeError("Expected argument 'public_azure_dns_record' to be a str")
        pulumi.set(__self__, "public_azure_dns_record", public_azure_dns_record)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="azureDnsRecord")
    def azure_dns_record(self) -> str:
        """
        The fully qualified DNS record for managed server alias
        """
        return pulumi.get(self, "azure_dns_record")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicAzureDnsRecord")
    def public_azure_dns_record(self) -> str:
        """
        The fully qualified public DNS record for managed server alias
        """
        return pulumi.get(self, "public_azure_dns_record")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedServerDnsAliasResult(GetManagedServerDnsAliasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedServerDnsAliasResult(
            azure_dns_record=self.azure_dns_record,
            id=self.id,
            name=self.name,
            public_azure_dns_record=self.public_azure_dns_record,
            type=self.type)


def get_managed_server_dns_alias(dns_alias_name: Optional[str] = None,
                                 managed_instance_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedServerDnsAliasResult:
    """
    Gets a server DNS alias.


    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['dnsAliasName'] = dns_alias_name
    __args__['managedInstanceName'] = managed_instance_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20221101preview:getManagedServerDnsAlias', __args__, opts=opts, typ=GetManagedServerDnsAliasResult).value

    return AwaitableGetManagedServerDnsAliasResult(
        azure_dns_record=pulumi.get(__ret__, 'azure_dns_record'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        public_azure_dns_record=pulumi.get(__ret__, 'public_azure_dns_record'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_managed_server_dns_alias)
def get_managed_server_dns_alias_output(dns_alias_name: Optional[pulumi.Input[str]] = None,
                                        managed_instance_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedServerDnsAliasResult]:
    """
    Gets a server DNS alias.


    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    ...
