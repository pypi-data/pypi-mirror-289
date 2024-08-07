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
from ._enums import *

__all__ = [
    'DenySettingsArgs',
    'DenySettingsArgsDict',
    'DeploymentStackPropertiesActionOnUnmanageArgs',
    'DeploymentStackPropertiesActionOnUnmanageArgsDict',
    'DeploymentStacksDebugSettingArgs',
    'DeploymentStacksDebugSettingArgsDict',
    'DeploymentStacksParametersLinkArgs',
    'DeploymentStacksParametersLinkArgsDict',
    'DeploymentStacksTemplateLinkArgs',
    'DeploymentStacksTemplateLinkArgsDict',
]

MYPY = False

if not MYPY:
    class DenySettingsArgsDict(TypedDict):
        """
        Defines how resources deployed by the deployment stack are locked.
        """
        mode: pulumi.Input[Union[str, 'DenySettingsMode']]
        """
        denySettings Mode.
        """
        apply_to_child_scopes: NotRequired[pulumi.Input[bool]]
        """
        DenySettings will be applied to child scopes.
        """
        excluded_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        List of role-based management operations that are excluded from the denySettings. Up to 200 actions are permitted. If the denySetting mode is set to 'denyWriteAndDelete', then the following actions are automatically appended to 'excludedActions': '*\\/read' and 'Microsoft.Authorization/locks/delete'. If the denySetting mode is set to 'denyDelete', then the following actions are automatically appended to 'excludedActions': 'Microsoft.Authorization/locks/delete'. Duplicate actions will be removed.
        """
        excluded_principals: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        List of AAD principal IDs excluded from the lock. Up to 5 principals are permitted.
        """
elif False:
    DenySettingsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DenySettingsArgs:
    def __init__(__self__, *,
                 mode: pulumi.Input[Union[str, 'DenySettingsMode']],
                 apply_to_child_scopes: Optional[pulumi.Input[bool]] = None,
                 excluded_actions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 excluded_principals: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Defines how resources deployed by the deployment stack are locked.
        :param pulumi.Input[Union[str, 'DenySettingsMode']] mode: denySettings Mode.
        :param pulumi.Input[bool] apply_to_child_scopes: DenySettings will be applied to child scopes.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_actions: List of role-based management operations that are excluded from the denySettings. Up to 200 actions are permitted. If the denySetting mode is set to 'denyWriteAndDelete', then the following actions are automatically appended to 'excludedActions': '*\\/read' and 'Microsoft.Authorization/locks/delete'. If the denySetting mode is set to 'denyDelete', then the following actions are automatically appended to 'excludedActions': 'Microsoft.Authorization/locks/delete'. Duplicate actions will be removed.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_principals: List of AAD principal IDs excluded from the lock. Up to 5 principals are permitted.
        """
        pulumi.set(__self__, "mode", mode)
        if apply_to_child_scopes is not None:
            pulumi.set(__self__, "apply_to_child_scopes", apply_to_child_scopes)
        if excluded_actions is not None:
            pulumi.set(__self__, "excluded_actions", excluded_actions)
        if excluded_principals is not None:
            pulumi.set(__self__, "excluded_principals", excluded_principals)

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Input[Union[str, 'DenySettingsMode']]:
        """
        denySettings Mode.
        """
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: pulumi.Input[Union[str, 'DenySettingsMode']]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="applyToChildScopes")
    def apply_to_child_scopes(self) -> Optional[pulumi.Input[bool]]:
        """
        DenySettings will be applied to child scopes.
        """
        return pulumi.get(self, "apply_to_child_scopes")

    @apply_to_child_scopes.setter
    def apply_to_child_scopes(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "apply_to_child_scopes", value)

    @property
    @pulumi.getter(name="excludedActions")
    def excluded_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of role-based management operations that are excluded from the denySettings. Up to 200 actions are permitted. If the denySetting mode is set to 'denyWriteAndDelete', then the following actions are automatically appended to 'excludedActions': '*\\/read' and 'Microsoft.Authorization/locks/delete'. If the denySetting mode is set to 'denyDelete', then the following actions are automatically appended to 'excludedActions': 'Microsoft.Authorization/locks/delete'. Duplicate actions will be removed.
        """
        return pulumi.get(self, "excluded_actions")

    @excluded_actions.setter
    def excluded_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_actions", value)

    @property
    @pulumi.getter(name="excludedPrincipals")
    def excluded_principals(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of AAD principal IDs excluded from the lock. Up to 5 principals are permitted.
        """
        return pulumi.get(self, "excluded_principals")

    @excluded_principals.setter
    def excluded_principals(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_principals", value)


if not MYPY:
    class DeploymentStackPropertiesActionOnUnmanageArgsDict(TypedDict):
        """
        Defines the behavior of resources that are not managed immediately after the stack is updated.
        """
        resources: pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]
        """
        Specifies the action that should be taken on the resource when the deployment stack is deleted. Delete will attempt to delete the resource from Azure. Detach will leave the resource in it's current state.
        """
        management_groups: NotRequired[pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]]
        """
        Specifies the action that should be taken on the resource when the deployment stack is deleted. Delete will attempt to delete the resource from Azure. Detach will leave the resource in it's current state.
        """
        resource_groups: NotRequired[pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]]
        """
        Specifies the action that should be taken on the resource when the deployment stack is deleted. Delete will attempt to delete the resource from Azure. Detach will leave the resource in it's current state.
        """
elif False:
    DeploymentStackPropertiesActionOnUnmanageArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DeploymentStackPropertiesActionOnUnmanageArgs:
    def __init__(__self__, *,
                 resources: pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']],
                 management_groups: Optional[pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]] = None,
                 resource_groups: Optional[pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]] = None):
        """
        Defines the behavior of resources that are not managed immediately after the stack is updated.
        :param pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']] resources: Specifies the action that should be taken on the resource when the deployment stack is deleted. Delete will attempt to delete the resource from Azure. Detach will leave the resource in it's current state.
        :param pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']] management_groups: Specifies the action that should be taken on the resource when the deployment stack is deleted. Delete will attempt to delete the resource from Azure. Detach will leave the resource in it's current state.
        :param pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']] resource_groups: Specifies the action that should be taken on the resource when the deployment stack is deleted. Delete will attempt to delete the resource from Azure. Detach will leave the resource in it's current state.
        """
        pulumi.set(__self__, "resources", resources)
        if management_groups is not None:
            pulumi.set(__self__, "management_groups", management_groups)
        if resource_groups is not None:
            pulumi.set(__self__, "resource_groups", resource_groups)

    @property
    @pulumi.getter
    def resources(self) -> pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]:
        """
        Specifies the action that should be taken on the resource when the deployment stack is deleted. Delete will attempt to delete the resource from Azure. Detach will leave the resource in it's current state.
        """
        return pulumi.get(self, "resources")

    @resources.setter
    def resources(self, value: pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]):
        pulumi.set(self, "resources", value)

    @property
    @pulumi.getter(name="managementGroups")
    def management_groups(self) -> Optional[pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]]:
        """
        Specifies the action that should be taken on the resource when the deployment stack is deleted. Delete will attempt to delete the resource from Azure. Detach will leave the resource in it's current state.
        """
        return pulumi.get(self, "management_groups")

    @management_groups.setter
    def management_groups(self, value: Optional[pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]]):
        pulumi.set(self, "management_groups", value)

    @property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> Optional[pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]]:
        """
        Specifies the action that should be taken on the resource when the deployment stack is deleted. Delete will attempt to delete the resource from Azure. Detach will leave the resource in it's current state.
        """
        return pulumi.get(self, "resource_groups")

    @resource_groups.setter
    def resource_groups(self, value: Optional[pulumi.Input[Union[str, 'DeploymentStacksDeleteDetachEnum']]]):
        pulumi.set(self, "resource_groups", value)


if not MYPY:
    class DeploymentStacksDebugSettingArgsDict(TypedDict):
        """
        The debug setting.
        """
        detail_level: NotRequired[pulumi.Input[str]]
        """
        Specifies the type of information to log for debugging. The permitted values are none, requestContent, responseContent, or both requestContent and responseContent separated by a comma. The default is none. When setting this value, carefully consider the type of information that is being passed in during deployment. By logging information about the request or response, sensitive data that is retrieved through the deployment operations could potentially be exposed.
        """
elif False:
    DeploymentStacksDebugSettingArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DeploymentStacksDebugSettingArgs:
    def __init__(__self__, *,
                 detail_level: Optional[pulumi.Input[str]] = None):
        """
        The debug setting.
        :param pulumi.Input[str] detail_level: Specifies the type of information to log for debugging. The permitted values are none, requestContent, responseContent, or both requestContent and responseContent separated by a comma. The default is none. When setting this value, carefully consider the type of information that is being passed in during deployment. By logging information about the request or response, sensitive data that is retrieved through the deployment operations could potentially be exposed.
        """
        if detail_level is not None:
            pulumi.set(__self__, "detail_level", detail_level)

    @property
    @pulumi.getter(name="detailLevel")
    def detail_level(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the type of information to log for debugging. The permitted values are none, requestContent, responseContent, or both requestContent and responseContent separated by a comma. The default is none. When setting this value, carefully consider the type of information that is being passed in during deployment. By logging information about the request or response, sensitive data that is retrieved through the deployment operations could potentially be exposed.
        """
        return pulumi.get(self, "detail_level")

    @detail_level.setter
    def detail_level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "detail_level", value)


if not MYPY:
    class DeploymentStacksParametersLinkArgsDict(TypedDict):
        """
        Entity representing the reference to the deployment parameters.
        """
        uri: pulumi.Input[str]
        """
        The URI of the parameters file.
        """
        content_version: NotRequired[pulumi.Input[str]]
        """
        If included, must match the ContentVersion in the template.
        """
elif False:
    DeploymentStacksParametersLinkArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DeploymentStacksParametersLinkArgs:
    def __init__(__self__, *,
                 uri: pulumi.Input[str],
                 content_version: Optional[pulumi.Input[str]] = None):
        """
        Entity representing the reference to the deployment parameters.
        :param pulumi.Input[str] uri: The URI of the parameters file.
        :param pulumi.Input[str] content_version: If included, must match the ContentVersion in the template.
        """
        pulumi.set(__self__, "uri", uri)
        if content_version is not None:
            pulumi.set(__self__, "content_version", content_version)

    @property
    @pulumi.getter
    def uri(self) -> pulumi.Input[str]:
        """
        The URI of the parameters file.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "uri", value)

    @property
    @pulumi.getter(name="contentVersion")
    def content_version(self) -> Optional[pulumi.Input[str]]:
        """
        If included, must match the ContentVersion in the template.
        """
        return pulumi.get(self, "content_version")

    @content_version.setter
    def content_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_version", value)


if not MYPY:
    class DeploymentStacksTemplateLinkArgsDict(TypedDict):
        """
        Entity representing the reference to the template.
        """
        content_version: NotRequired[pulumi.Input[str]]
        """
        If included, must match the ContentVersion in the template.
        """
        id: NotRequired[pulumi.Input[str]]
        """
        The resource id of a Template Spec. Use either the id or uri property, but not both.
        """
        query_string: NotRequired[pulumi.Input[str]]
        """
        The query string (for example, a SAS token) to be used with the templateLink URI.
        """
        relative_path: NotRequired[pulumi.Input[str]]
        """
        The relativePath property can be used to deploy a linked template at a location relative to the parent. If the parent template was linked with a TemplateSpec, this will reference an artifact in the TemplateSpec.  If the parent was linked with a URI, the child deployment will be a combination of the parent and relativePath URIs
        """
        uri: NotRequired[pulumi.Input[str]]
        """
        The URI of the template to deploy. Use either the uri or id property, but not both.
        """
elif False:
    DeploymentStacksTemplateLinkArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class DeploymentStacksTemplateLinkArgs:
    def __init__(__self__, *,
                 content_version: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 query_string: Optional[pulumi.Input[str]] = None,
                 relative_path: Optional[pulumi.Input[str]] = None,
                 uri: Optional[pulumi.Input[str]] = None):
        """
        Entity representing the reference to the template.
        :param pulumi.Input[str] content_version: If included, must match the ContentVersion in the template.
        :param pulumi.Input[str] id: The resource id of a Template Spec. Use either the id or uri property, but not both.
        :param pulumi.Input[str] query_string: The query string (for example, a SAS token) to be used with the templateLink URI.
        :param pulumi.Input[str] relative_path: The relativePath property can be used to deploy a linked template at a location relative to the parent. If the parent template was linked with a TemplateSpec, this will reference an artifact in the TemplateSpec.  If the parent was linked with a URI, the child deployment will be a combination of the parent and relativePath URIs
        :param pulumi.Input[str] uri: The URI of the template to deploy. Use either the uri or id property, but not both.
        """
        if content_version is not None:
            pulumi.set(__self__, "content_version", content_version)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if query_string is not None:
            pulumi.set(__self__, "query_string", query_string)
        if relative_path is not None:
            pulumi.set(__self__, "relative_path", relative_path)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="contentVersion")
    def content_version(self) -> Optional[pulumi.Input[str]]:
        """
        If included, must match the ContentVersion in the template.
        """
        return pulumi.get(self, "content_version")

    @content_version.setter
    def content_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_version", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of a Template Spec. Use either the id or uri property, but not both.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[pulumi.Input[str]]:
        """
        The query string (for example, a SAS token) to be used with the templateLink URI.
        """
        return pulumi.get(self, "query_string")

    @query_string.setter
    def query_string(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query_string", value)

    @property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[pulumi.Input[str]]:
        """
        The relativePath property can be used to deploy a linked template at a location relative to the parent. If the parent template was linked with a TemplateSpec, this will reference an artifact in the TemplateSpec.  If the parent was linked with a URI, the child deployment will be a combination of the parent and relativePath URIs
        """
        return pulumi.get(self, "relative_path")

    @relative_path.setter
    def relative_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "relative_path", value)

    @property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[str]]:
        """
        The URI of the template to deploy. Use either the uri or id property, but not both.
        """
        return pulumi.get(self, "uri")

    @uri.setter
    def uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "uri", value)


