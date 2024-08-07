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
    'GetApiDefinitionResult',
    'AwaitableGetApiDefinitionResult',
    'get_api_definition',
    'get_api_definition_output',
]

@pulumi.output_type
class GetApiDefinitionResult:
    """
    API definition entity.
    """
    def __init__(__self__, description=None, id=None, name=None, specification=None, system_data=None, title=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if specification and not isinstance(specification, dict):
            raise TypeError("Expected argument 'specification' to be a dict")
        pulumi.set(__self__, "specification", specification)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if title and not isinstance(title, str):
            raise TypeError("Expected argument 'title' to be a str")
        pulumi.set(__self__, "title", title)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        API definition description.
        """
        return pulumi.get(self, "description")

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
    @pulumi.getter
    def specification(self) -> 'outputs.ApiDefinitionPropertiesSpecificationResponse':
        """
        API specification details.
        """
        return pulumi.get(self, "specification")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def title(self) -> str:
        """
        API definition title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetApiDefinitionResult(GetApiDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiDefinitionResult(
            description=self.description,
            id=self.id,
            name=self.name,
            specification=self.specification,
            system_data=self.system_data,
            title=self.title,
            type=self.type)


def get_api_definition(api_name: Optional[str] = None,
                       definition_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       service_name: Optional[str] = None,
                       version_name: Optional[str] = None,
                       workspace_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiDefinitionResult:
    """
    Returns details of the API definition.


    :param str api_name: The name of the API.
    :param str definition_name: The name of the API definition.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of Azure API Center service.
    :param str version_name: The name of the API version.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['apiName'] = api_name
    __args__['definitionName'] = definition_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['versionName'] = version_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apicenter/v20240301:getApiDefinition', __args__, opts=opts, typ=GetApiDefinitionResult).value

    return AwaitableGetApiDefinitionResult(
        description=pulumi.get(__ret__, 'description'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        specification=pulumi.get(__ret__, 'specification'),
        system_data=pulumi.get(__ret__, 'system_data'),
        title=pulumi.get(__ret__, 'title'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_api_definition)
def get_api_definition_output(api_name: Optional[pulumi.Input[str]] = None,
                              definition_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              service_name: Optional[pulumi.Input[str]] = None,
                              version_name: Optional[pulumi.Input[str]] = None,
                              workspace_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiDefinitionResult]:
    """
    Returns details of the API definition.


    :param str api_name: The name of the API.
    :param str definition_name: The name of the API definition.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of Azure API Center service.
    :param str version_name: The name of the API version.
    :param str workspace_name: The name of the workspace.
    """
    ...
