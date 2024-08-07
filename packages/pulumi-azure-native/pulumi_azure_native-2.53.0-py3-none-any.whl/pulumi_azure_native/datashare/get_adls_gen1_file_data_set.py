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
    'GetADLSGen1FileDataSetResult',
    'AwaitableGetADLSGen1FileDataSetResult',
    'get_adls_gen1_file_data_set',
    'get_adls_gen1_file_data_set_output',
]

@pulumi.output_type
class GetADLSGen1FileDataSetResult:
    """
    An ADLS Gen 1 file data set.
    """
    def __init__(__self__, account_name=None, data_set_id=None, file_name=None, folder_path=None, id=None, kind=None, name=None, resource_group=None, subscription_id=None, system_data=None, type=None):
        if account_name and not isinstance(account_name, str):
            raise TypeError("Expected argument 'account_name' to be a str")
        pulumi.set(__self__, "account_name", account_name)
        if data_set_id and not isinstance(data_set_id, str):
            raise TypeError("Expected argument 'data_set_id' to be a str")
        pulumi.set(__self__, "data_set_id", data_set_id)
        if file_name and not isinstance(file_name, str):
            raise TypeError("Expected argument 'file_name' to be a str")
        pulumi.set(__self__, "file_name", file_name)
        if folder_path and not isinstance(folder_path, str):
            raise TypeError("Expected argument 'folder_path' to be a str")
        pulumi.set(__self__, "folder_path", folder_path)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_group and not isinstance(resource_group, str):
            raise TypeError("Expected argument 'resource_group' to be a str")
        pulumi.set(__self__, "resource_group", resource_group)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        """
        The ADLS account name.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> str:
        """
        Unique id for identifying a data set resource
        """
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter(name="fileName")
    def file_name(self) -> str:
        """
        The file name in the ADLS account.
        """
        return pulumi.get(self, "file_name")

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> str:
        """
        The folder path within the ADLS account.
        """
        return pulumi.get(self, "folder_path")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of data set.
        Expected value is 'AdlsGen1File'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> str:
        """
        Resource group of ADLS account.
        """
        return pulumi.get(self, "resource_group")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        Subscription id of ADLS account.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")


class AwaitableGetADLSGen1FileDataSetResult(GetADLSGen1FileDataSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetADLSGen1FileDataSetResult(
            account_name=self.account_name,
            data_set_id=self.data_set_id,
            file_name=self.file_name,
            folder_path=self.folder_path,
            id=self.id,
            kind=self.kind,
            name=self.name,
            resource_group=self.resource_group,
            subscription_id=self.subscription_id,
            system_data=self.system_data,
            type=self.type)


def get_adls_gen1_file_data_set(account_name: Optional[str] = None,
                                data_set_name: Optional[str] = None,
                                resource_group_name: Optional[str] = None,
                                share_name: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetADLSGen1FileDataSetResult:
    """
    Get a DataSet in a share
    Azure REST API version: 2021-08-01.


    :param str account_name: The name of the share account.
    :param str data_set_name: The name of the dataSet.
    :param str resource_group_name: The resource group name.
    :param str share_name: The name of the share.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataSetName'] = data_set_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareName'] = share_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datashare:getADLSGen1FileDataSet', __args__, opts=opts, typ=GetADLSGen1FileDataSetResult).value

    return AwaitableGetADLSGen1FileDataSetResult(
        account_name=pulumi.get(__ret__, 'account_name'),
        data_set_id=pulumi.get(__ret__, 'data_set_id'),
        file_name=pulumi.get(__ret__, 'file_name'),
        folder_path=pulumi.get(__ret__, 'folder_path'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        resource_group=pulumi.get(__ret__, 'resource_group'),
        subscription_id=pulumi.get(__ret__, 'subscription_id'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_adls_gen1_file_data_set)
def get_adls_gen1_file_data_set_output(account_name: Optional[pulumi.Input[str]] = None,
                                       data_set_name: Optional[pulumi.Input[str]] = None,
                                       resource_group_name: Optional[pulumi.Input[str]] = None,
                                       share_name: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetADLSGen1FileDataSetResult]:
    """
    Get a DataSet in a share
    Azure REST API version: 2021-08-01.


    :param str account_name: The name of the share account.
    :param str data_set_name: The name of the dataSet.
    :param str resource_group_name: The resource group name.
    :param str share_name: The name of the share.
    """
    ...
