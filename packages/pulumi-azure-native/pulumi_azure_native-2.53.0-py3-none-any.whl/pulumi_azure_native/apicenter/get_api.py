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
    'GetApiResult',
    'AwaitableGetApiResult',
    'get_api',
    'get_api_output',
]

@pulumi.output_type
class GetApiResult:
    """
    API entity.
    """
    def __init__(__self__, contacts=None, custom_properties=None, description=None, external_documentation=None, id=None, kind=None, license=None, lifecycle_stage=None, name=None, summary=None, system_data=None, terms_of_service=None, title=None, type=None):
        if contacts and not isinstance(contacts, list):
            raise TypeError("Expected argument 'contacts' to be a list")
        pulumi.set(__self__, "contacts", contacts)
        if custom_properties and not isinstance(custom_properties, dict):
            raise TypeError("Expected argument 'custom_properties' to be a dict")
        pulumi.set(__self__, "custom_properties", custom_properties)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if external_documentation and not isinstance(external_documentation, list):
            raise TypeError("Expected argument 'external_documentation' to be a list")
        pulumi.set(__self__, "external_documentation", external_documentation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if license and not isinstance(license, dict):
            raise TypeError("Expected argument 'license' to be a dict")
        pulumi.set(__self__, "license", license)
        if lifecycle_stage and not isinstance(lifecycle_stage, str):
            raise TypeError("Expected argument 'lifecycle_stage' to be a str")
        pulumi.set(__self__, "lifecycle_stage", lifecycle_stage)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if summary and not isinstance(summary, str):
            raise TypeError("Expected argument 'summary' to be a str")
        pulumi.set(__self__, "summary", summary)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if terms_of_service and not isinstance(terms_of_service, dict):
            raise TypeError("Expected argument 'terms_of_service' to be a dict")
        pulumi.set(__self__, "terms_of_service", terms_of_service)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def contacts(self) -> Optional[Sequence['outputs.ContactResponse']]:
        """
        The set of contacts
        """
        return pulumi.get(self, "contacts")

    @property
    @pulumi.getter(name="customProperties")
    def custom_properties(self) -> Optional[Any]:
        """
        The custom metadata defined for API catalog entities.
        """
        return pulumi.get(self, "custom_properties")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of the API.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="externalDocumentation")
    def external_documentation(self) -> Optional[Sequence['outputs.ExternalDocumentationResponse']]:
        """
        The set of external documentation
        """
        return pulumi.get(self, "external_documentation")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of API. For example, REST or GraphQL.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def license(self) -> Optional['outputs.LicenseResponse']:
        """
        The license information for the API.
        """
        return pulumi.get(self, "license")

    @property
    @pulumi.getter(name="lifecycleStage")
    def lifecycle_stage(self) -> str:
        """
        Current lifecycle stage of the API.
        """
        return pulumi.get(self, "lifecycle_stage")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def summary(self) -> Optional[str]:
        """
        Short description of the API.
        """
        return pulumi.get(self, "summary")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="termsOfService")
    def terms_of_service(self) -> Optional['outputs.TermsOfServiceResponse']:
        """
        Terms of service for the API.
        """
        return pulumi.get(self, "terms_of_service")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        API title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetApiResult(GetApiResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiResult(
            contacts=self.contacts,
            custom_properties=self.custom_properties,
            description=self.description,
            external_documentation=self.external_documentation,
            id=self.id,
            kind=self.kind,
            license=self.license,
            lifecycle_stage=self.lifecycle_stage,
            name=self.name,
            summary=self.summary,
            system_data=self.system_data,
            terms_of_service=self.terms_of_service,
            title=self.title,
            type=self.type)


def get_api(api_name: Optional[str] = None,
            resource_group_name: Optional[str] = None,
            service_name: Optional[str] = None,
            workspace_name: Optional[str] = None,
            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiResult:
    """
    Returns details of the API.
    Azure REST API version: 2024-03-01.

    Other available API versions: 2024-03-15-preview.


    :param str api_name: The name of the API.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of Azure API Center service.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['apiName'] = api_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apicenter:getApi', __args__, opts=opts, typ=GetApiResult).value

    return AwaitableGetApiResult(
        contacts=pulumi.get(__ret__, 'contacts'),
        custom_properties=pulumi.get(__ret__, 'custom_properties'),
        description=pulumi.get(__ret__, 'description'),
        external_documentation=pulumi.get(__ret__, 'external_documentation'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        license=pulumi.get(__ret__, 'license'),
        lifecycle_stage=pulumi.get(__ret__, 'lifecycle_stage'),
        name=pulumi.get(__ret__, 'name'),
        summary=pulumi.get(__ret__, 'summary'),
        system_data=pulumi.get(__ret__, 'system_data'),
        terms_of_service=pulumi.get(__ret__, 'terms_of_service'),
        title=pulumi.get(__ret__, 'title'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_api)
def get_api_output(api_name: Optional[pulumi.Input[str]] = None,
                   resource_group_name: Optional[pulumi.Input[str]] = None,
                   service_name: Optional[pulumi.Input[str]] = None,
                   workspace_name: Optional[pulumi.Input[str]] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiResult]:
    """
    Returns details of the API.
    Azure REST API version: 2024-03-01.

    Other available API versions: 2024-03-15-preview.


    :param str api_name: The name of the API.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of Azure API Center service.
    :param str workspace_name: The name of the workspace.
    """
    ...
