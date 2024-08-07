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

__all__ = [
    'GetAPICollectionResult',
    'AwaitableGetAPICollectionResult',
    'get_api_collection',
    'get_api_collection_output',
]

@pulumi.output_type
class GetAPICollectionResult:
    """
    An API collection as represented by Defender for APIs.
    """
    def __init__(__self__, additional_data=None, display_name=None, id=None, name=None, type=None):
        if additional_data and not isinstance(additional_data, dict):
            raise TypeError("Expected argument 'additional_data' to be a dict")
        pulumi.set(__self__, "additional_data", additional_data)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="additionalData")
    def additional_data(self) -> Optional[Mapping[str, str]]:
        """
        Additional data regarding the API collection.
        """
        return pulumi.get(self, "additional_data")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the Azure API Management API.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetAPICollectionResult(GetAPICollectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAPICollectionResult(
            additional_data=self.additional_data,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            type=self.type)


def get_api_collection(api_collection_id: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       service_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAPICollectionResult:
    """
    Gets an Azure API Management API if it has been onboarded to Defender for APIs. If an Azure API Management API is onboarded to Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected.
    Azure REST API version: 2022-11-20-preview.


    :param str api_collection_id: A string representing the apiCollections resource within the Microsoft.Security provider namespace. This string matches the Azure API Management API name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['apiCollectionId'] = api_collection_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security:getAPICollection', __args__, opts=opts, typ=GetAPICollectionResult).value

    return AwaitableGetAPICollectionResult(
        additional_data=pulumi.get(__ret__, 'additional_data'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_api_collection)
def get_api_collection_output(api_collection_id: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              service_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAPICollectionResult]:
    """
    Gets an Azure API Management API if it has been onboarded to Defender for APIs. If an Azure API Management API is onboarded to Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected.
    Azure REST API version: 2022-11-20-preview.


    :param str api_collection_id: A string representing the apiCollections resource within the Microsoft.Security provider namespace. This string matches the Azure API Management API name.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
