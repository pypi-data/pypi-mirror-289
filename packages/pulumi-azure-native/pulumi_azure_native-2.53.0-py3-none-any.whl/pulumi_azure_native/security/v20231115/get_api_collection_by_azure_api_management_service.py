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
    'GetAPICollectionByAzureApiManagementServiceResult',
    'AwaitableGetAPICollectionByAzureApiManagementServiceResult',
    'get_api_collection_by_azure_api_management_service',
    'get_api_collection_by_azure_api_management_service_output',
]

@pulumi.output_type
class GetAPICollectionByAzureApiManagementServiceResult:
    """
    An API collection as represented by Microsoft Defender for APIs.
    """
    def __init__(__self__, base_url=None, discovered_via=None, display_name=None, id=None, name=None, number_of_api_endpoints=None, number_of_api_endpoints_with_sensitive_data_exposed=None, number_of_external_api_endpoints=None, number_of_inactive_api_endpoints=None, number_of_unauthenticated_api_endpoints=None, provisioning_state=None, sensitivity_label=None, type=None):
        if base_url and not isinstance(base_url, str):
            raise TypeError("Expected argument 'base_url' to be a str")
        pulumi.set(__self__, "base_url", base_url)
        if discovered_via and not isinstance(discovered_via, str):
            raise TypeError("Expected argument 'discovered_via' to be a str")
        pulumi.set(__self__, "discovered_via", discovered_via)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if number_of_api_endpoints and not isinstance(number_of_api_endpoints, float):
            raise TypeError("Expected argument 'number_of_api_endpoints' to be a float")
        pulumi.set(__self__, "number_of_api_endpoints", number_of_api_endpoints)
        if number_of_api_endpoints_with_sensitive_data_exposed and not isinstance(number_of_api_endpoints_with_sensitive_data_exposed, float):
            raise TypeError("Expected argument 'number_of_api_endpoints_with_sensitive_data_exposed' to be a float")
        pulumi.set(__self__, "number_of_api_endpoints_with_sensitive_data_exposed", number_of_api_endpoints_with_sensitive_data_exposed)
        if number_of_external_api_endpoints and not isinstance(number_of_external_api_endpoints, float):
            raise TypeError("Expected argument 'number_of_external_api_endpoints' to be a float")
        pulumi.set(__self__, "number_of_external_api_endpoints", number_of_external_api_endpoints)
        if number_of_inactive_api_endpoints and not isinstance(number_of_inactive_api_endpoints, float):
            raise TypeError("Expected argument 'number_of_inactive_api_endpoints' to be a float")
        pulumi.set(__self__, "number_of_inactive_api_endpoints", number_of_inactive_api_endpoints)
        if number_of_unauthenticated_api_endpoints and not isinstance(number_of_unauthenticated_api_endpoints, float):
            raise TypeError("Expected argument 'number_of_unauthenticated_api_endpoints' to be a float")
        pulumi.set(__self__, "number_of_unauthenticated_api_endpoints", number_of_unauthenticated_api_endpoints)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sensitivity_label and not isinstance(sensitivity_label, str):
            raise TypeError("Expected argument 'sensitivity_label' to be a str")
        pulumi.set(__self__, "sensitivity_label", sensitivity_label)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> str:
        """
        The base URI for this API collection. All endpoints of this API collection extend this base URI.
        """
        return pulumi.get(self, "base_url")

    @property
    @pulumi.getter(name="discoveredVia")
    def discovered_via(self) -> str:
        """
        The resource Id of the resource from where this API collection was discovered.
        """
        return pulumi.get(self, "discovered_via")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the API collection.
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
    @pulumi.getter(name="numberOfApiEndpoints")
    def number_of_api_endpoints(self) -> float:
        """
        The number of API endpoints discovered in this API collection.
        """
        return pulumi.get(self, "number_of_api_endpoints")

    @property
    @pulumi.getter(name="numberOfApiEndpointsWithSensitiveDataExposed")
    def number_of_api_endpoints_with_sensitive_data_exposed(self) -> float:
        """
        The number of API endpoints in this API collection which are exposing sensitive data in their requests and/or responses.
        """
        return pulumi.get(self, "number_of_api_endpoints_with_sensitive_data_exposed")

    @property
    @pulumi.getter(name="numberOfExternalApiEndpoints")
    def number_of_external_api_endpoints(self) -> float:
        """
        The number of API endpoints in this API collection for which API traffic from the internet was observed.
        """
        return pulumi.get(self, "number_of_external_api_endpoints")

    @property
    @pulumi.getter(name="numberOfInactiveApiEndpoints")
    def number_of_inactive_api_endpoints(self) -> float:
        """
        The number of API endpoints in this API collection that have not received any API traffic in the last 30 days.
        """
        return pulumi.get(self, "number_of_inactive_api_endpoints")

    @property
    @pulumi.getter(name="numberOfUnauthenticatedApiEndpoints")
    def number_of_unauthenticated_api_endpoints(self) -> float:
        """
        The number of API endpoints in this API collection that are unauthenticated.
        """
        return pulumi.get(self, "number_of_unauthenticated_api_endpoints")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets the provisioning state of the API collection.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sensitivityLabel")
    def sensitivity_label(self) -> str:
        """
        The highest priority sensitivity label from Microsoft Purview in this API collection.
        """
        return pulumi.get(self, "sensitivity_label")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetAPICollectionByAzureApiManagementServiceResult(GetAPICollectionByAzureApiManagementServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAPICollectionByAzureApiManagementServiceResult(
            base_url=self.base_url,
            discovered_via=self.discovered_via,
            display_name=self.display_name,
            id=self.id,
            name=self.name,
            number_of_api_endpoints=self.number_of_api_endpoints,
            number_of_api_endpoints_with_sensitive_data_exposed=self.number_of_api_endpoints_with_sensitive_data_exposed,
            number_of_external_api_endpoints=self.number_of_external_api_endpoints,
            number_of_inactive_api_endpoints=self.number_of_inactive_api_endpoints,
            number_of_unauthenticated_api_endpoints=self.number_of_unauthenticated_api_endpoints,
            provisioning_state=self.provisioning_state,
            sensitivity_label=self.sensitivity_label,
            type=self.type)


def get_api_collection_by_azure_api_management_service(api_id: Optional[str] = None,
                                                       resource_group_name: Optional[str] = None,
                                                       service_name: Optional[str] = None,
                                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAPICollectionByAzureApiManagementServiceResult:
    """
    Gets an Azure API Management API if it has been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected.


    :param str api_id: API revision identifier. Must be unique in the API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:security/v20231115:getAPICollectionByAzureApiManagementService', __args__, opts=opts, typ=GetAPICollectionByAzureApiManagementServiceResult).value

    return AwaitableGetAPICollectionByAzureApiManagementServiceResult(
        base_url=pulumi.get(__ret__, 'base_url'),
        discovered_via=pulumi.get(__ret__, 'discovered_via'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        number_of_api_endpoints=pulumi.get(__ret__, 'number_of_api_endpoints'),
        number_of_api_endpoints_with_sensitive_data_exposed=pulumi.get(__ret__, 'number_of_api_endpoints_with_sensitive_data_exposed'),
        number_of_external_api_endpoints=pulumi.get(__ret__, 'number_of_external_api_endpoints'),
        number_of_inactive_api_endpoints=pulumi.get(__ret__, 'number_of_inactive_api_endpoints'),
        number_of_unauthenticated_api_endpoints=pulumi.get(__ret__, 'number_of_unauthenticated_api_endpoints'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        sensitivity_label=pulumi.get(__ret__, 'sensitivity_label'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_api_collection_by_azure_api_management_service)
def get_api_collection_by_azure_api_management_service_output(api_id: Optional[pulumi.Input[str]] = None,
                                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                                              service_name: Optional[pulumi.Input[str]] = None,
                                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAPICollectionByAzureApiManagementServiceResult]:
    """
    Gets an Azure API Management API if it has been onboarded to Microsoft Defender for APIs. If an Azure API Management API is onboarded to Microsoft Defender for APIs, the system will monitor the operations within the Azure API Management API for intrusive behaviors and provide alerts for attacks that have been detected.


    :param str api_id: API revision identifier. Must be unique in the API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
