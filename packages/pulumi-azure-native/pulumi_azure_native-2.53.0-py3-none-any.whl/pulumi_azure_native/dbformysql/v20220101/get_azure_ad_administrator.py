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
    'GetAzureADAdministratorResult',
    'AwaitableGetAzureADAdministratorResult',
    'get_azure_ad_administrator',
    'get_azure_ad_administrator_output',
]

@pulumi.output_type
class GetAzureADAdministratorResult:
    """
    Represents a Administrator.
    """
    def __init__(__self__, administrator_type=None, id=None, identity_resource_id=None, login=None, name=None, sid=None, system_data=None, tenant_id=None, type=None):
        if administrator_type and not isinstance(administrator_type, str):
            raise TypeError("Expected argument 'administrator_type' to be a str")
        pulumi.set(__self__, "administrator_type", administrator_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity_resource_id and not isinstance(identity_resource_id, str):
            raise TypeError("Expected argument 'identity_resource_id' to be a str")
        pulumi.set(__self__, "identity_resource_id", identity_resource_id)
        if login and not isinstance(login, str):
            raise TypeError("Expected argument 'login' to be a str")
        pulumi.set(__self__, "login", login)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sid and not isinstance(sid, str):
            raise TypeError("Expected argument 'sid' to be a str")
        pulumi.set(__self__, "sid", sid)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> Optional[str]:
        """
        Type of the sever administrator.
        """
        return pulumi.get(self, "administrator_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="identityResourceId")
    def identity_resource_id(self) -> Optional[str]:
        """
        The resource id of the identity used for AAD Authentication.
        """
        return pulumi.get(self, "identity_resource_id")

    @property
    @pulumi.getter
    def login(self) -> Optional[str]:
        """
        Login name of the server administrator.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sid(self) -> Optional[str]:
        """
        SID (object ID) of the server administrator.
        """
        return pulumi.get(self, "sid")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        Tenant ID of the administrator.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAzureADAdministratorResult(GetAzureADAdministratorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAzureADAdministratorResult(
            administrator_type=self.administrator_type,
            id=self.id,
            identity_resource_id=self.identity_resource_id,
            login=self.login,
            name=self.name,
            sid=self.sid,
            system_data=self.system_data,
            tenant_id=self.tenant_id,
            type=self.type)


def get_azure_ad_administrator(administrator_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               server_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAzureADAdministratorResult:
    """
    Gets information about an azure ad administrator.


    :param str administrator_name: The name of the Azure AD Administrator.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['administratorName'] = administrator_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbformysql/v20220101:getAzureADAdministrator', __args__, opts=opts, typ=GetAzureADAdministratorResult).value

    return AwaitableGetAzureADAdministratorResult(
        administrator_type=pulumi.get(__ret__, 'administrator_type'),
        id=pulumi.get(__ret__, 'id'),
        identity_resource_id=pulumi.get(__ret__, 'identity_resource_id'),
        login=pulumi.get(__ret__, 'login'),
        name=pulumi.get(__ret__, 'name'),
        sid=pulumi.get(__ret__, 'sid'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tenant_id=pulumi.get(__ret__, 'tenant_id'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_azure_ad_administrator)
def get_azure_ad_administrator_output(administrator_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      server_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAzureADAdministratorResult]:
    """
    Gets information about an azure ad administrator.


    :param str administrator_name: The name of the Azure AD Administrator.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str server_name: The name of the server.
    """
    ...
