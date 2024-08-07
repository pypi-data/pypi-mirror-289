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
    'GetActionRequestResult',
    'AwaitableGetActionRequestResult',
    'get_action_request',
    'get_action_request_output',
]

@pulumi.output_type
class GetActionRequestResult:
    def __init__(__self__, creation_date=None, id=None, name=None, pre_release_access_request_spec=None, provisioning_state=None, request_type=None, status=None, system_data=None, type=None):
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if pre_release_access_request_spec and not isinstance(pre_release_access_request_spec, dict):
            raise TypeError("Expected argument 'pre_release_access_request_spec' to be a dict")
        pulumi.set(__self__, "pre_release_access_request_spec", pre_release_access_request_spec)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if request_type and not isinstance(request_type, str):
            raise TypeError("Expected argument 'request_type' to be a str")
        pulumi.set(__self__, "request_type", request_type)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
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
    @pulumi.getter(name="preReleaseAccessRequestSpec")
    def pre_release_access_request_spec(self) -> Optional['outputs.PreReleaseAccessRequestSpecResponse']:
        return pulumi.get(self, "pre_release_access_request_spec")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="requestType")
    def request_type(self) -> str:
        return pulumi.get(self, "request_type")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

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


class AwaitableGetActionRequestResult(GetActionRequestResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetActionRequestResult(
            creation_date=self.creation_date,
            id=self.id,
            name=self.name,
            pre_release_access_request_spec=self.pre_release_access_request_spec,
            provisioning_state=self.provisioning_state,
            request_type=self.request_type,
            status=self.status,
            system_data=self.system_data,
            type=self.type)


def get_action_request(action_request_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       test_base_account_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetActionRequestResult:
    """
    Get the action request under the specified test base account.
    Azure REST API version: 2023-11-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    __args__ = dict()
    __args__['actionRequestName'] = action_request_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['testBaseAccountName'] = test_base_account_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:testbase:getActionRequest', __args__, opts=opts, typ=GetActionRequestResult).value

    return AwaitableGetActionRequestResult(
        creation_date=pulumi.get(__ret__, 'creation_date'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        pre_release_access_request_spec=pulumi.get(__ret__, 'pre_release_access_request_spec'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        request_type=pulumi.get(__ret__, 'request_type'),
        status=pulumi.get(__ret__, 'status'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_action_request)
def get_action_request_output(action_request_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              test_base_account_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetActionRequestResult]:
    """
    Get the action request under the specified test base account.
    Azure REST API version: 2023-11-01-preview.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    ...
