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
from ._enums import *

__all__ = [
    'BranchResponse',
    'CapabilityPropertiesResponse',
    'ContinuousActionResponse',
    'DelayActionResponse',
    'DiscreteActionResponse',
    'ExperimentPropertiesResponse',
    'KeyValuePairResponse',
    'ListSelectorResponse',
    'QuerySelectorResponse',
    'ResourceIdentityResponse',
    'SimpleFilterParametersResponse',
    'SimpleFilterResponse',
    'StepResponse',
    'SystemDataResponse',
    'TargetReferenceResponse',
    'UserAssignedIdentityResponse',
]

@pulumi.output_type
class BranchResponse(dict):
    """
    Model that represents a branch in the step.
    """
    def __init__(__self__, *,
                 actions: Sequence[Any],
                 name: str):
        """
        Model that represents a branch in the step.
        :param Sequence[Union['ContinuousActionResponse', 'DelayActionResponse', 'DiscreteActionResponse']] actions: List of actions.
        :param str name: String of the branch name.
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def actions(self) -> Sequence[Any]:
        """
        List of actions.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        String of the branch name.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class CapabilityPropertiesResponse(dict):
    """
    Model that represents the Capability properties model.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "parametersSchema":
            suggest = "parameters_schema"
        elif key == "targetType":
            suggest = "target_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CapabilityPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CapabilityPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CapabilityPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 description: str,
                 parameters_schema: str,
                 publisher: str,
                 target_type: str,
                 urn: str):
        """
        Model that represents the Capability properties model.
        :param str description: Localized string of the description.
        :param str parameters_schema: URL to retrieve JSON schema of the Capability parameters.
        :param str publisher: String of the Publisher that this Capability extends.
        :param str target_type: String of the Target Type that this Capability extends.
        :param str urn: String of the URN for this Capability Type.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "parameters_schema", parameters_schema)
        pulumi.set(__self__, "publisher", publisher)
        pulumi.set(__self__, "target_type", target_type)
        pulumi.set(__self__, "urn", urn)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Localized string of the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="parametersSchema")
    def parameters_schema(self) -> str:
        """
        URL to retrieve JSON schema of the Capability parameters.
        """
        return pulumi.get(self, "parameters_schema")

    @property
    @pulumi.getter
    def publisher(self) -> str:
        """
        String of the Publisher that this Capability extends.
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> str:
        """
        String of the Target Type that this Capability extends.
        """
        return pulumi.get(self, "target_type")

    @property
    @pulumi.getter
    def urn(self) -> str:
        """
        String of the URN for this Capability Type.
        """
        return pulumi.get(self, "urn")


@pulumi.output_type
class ContinuousActionResponse(dict):
    """
    Model that represents a continuous action.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "selectorId":
            suggest = "selector_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContinuousActionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContinuousActionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContinuousActionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 duration: str,
                 name: str,
                 parameters: Sequence['outputs.KeyValuePairResponse'],
                 selector_id: str,
                 type: str):
        """
        Model that represents a continuous action.
        :param str duration: ISO8601 formatted string that represents a duration.
        :param str name: String that represents a Capability URN.
        :param Sequence['KeyValuePairResponse'] parameters: List of key value pairs.
        :param str selector_id: String that represents a selector.
        :param str type: Enum that discriminates between action models.
               Expected value is 'continuous'.
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "parameters", parameters)
        pulumi.set(__self__, "selector_id", selector_id)
        pulumi.set(__self__, "type", 'continuous')

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        ISO8601 formatted string that represents a duration.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        String that represents a Capability URN.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Sequence['outputs.KeyValuePairResponse']:
        """
        List of key value pairs.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="selectorId")
    def selector_id(self) -> str:
        """
        String that represents a selector.
        """
        return pulumi.get(self, "selector_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Enum that discriminates between action models.
        Expected value is 'continuous'.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class DelayActionResponse(dict):
    """
    Model that represents a delay action.
    """
    def __init__(__self__, *,
                 duration: str,
                 name: str,
                 type: str):
        """
        Model that represents a delay action.
        :param str duration: ISO8601 formatted string that represents a duration.
        :param str name: String that represents a Capability URN.
        :param str type: Enum that discriminates between action models.
               Expected value is 'delay'.
        """
        pulumi.set(__self__, "duration", duration)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", 'delay')

    @property
    @pulumi.getter
    def duration(self) -> str:
        """
        ISO8601 formatted string that represents a duration.
        """
        return pulumi.get(self, "duration")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        String that represents a Capability URN.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Enum that discriminates between action models.
        Expected value is 'delay'.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class DiscreteActionResponse(dict):
    """
    Model that represents a discrete action.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "selectorId":
            suggest = "selector_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DiscreteActionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DiscreteActionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DiscreteActionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 parameters: Sequence['outputs.KeyValuePairResponse'],
                 selector_id: str,
                 type: str):
        """
        Model that represents a discrete action.
        :param str name: String that represents a Capability URN.
        :param Sequence['KeyValuePairResponse'] parameters: List of key value pairs.
        :param str selector_id: String that represents a selector.
        :param str type: Enum that discriminates between action models.
               Expected value is 'discrete'.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "parameters", parameters)
        pulumi.set(__self__, "selector_id", selector_id)
        pulumi.set(__self__, "type", 'discrete')

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        String that represents a Capability URN.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> Sequence['outputs.KeyValuePairResponse']:
        """
        List of key value pairs.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="selectorId")
    def selector_id(self) -> str:
        """
        String that represents a selector.
        """
        return pulumi.get(self, "selector_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Enum that discriminates between action models.
        Expected value is 'discrete'.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ExperimentPropertiesResponse(dict):
    """
    Model that represents the Experiment properties model.
    """
    def __init__(__self__, *,
                 selectors: Sequence[Any],
                 steps: Sequence['outputs.StepResponse']):
        """
        Model that represents the Experiment properties model.
        :param Sequence[Union['ListSelectorResponse', 'QuerySelectorResponse']] selectors: List of selectors.
        :param Sequence['StepResponse'] steps: List of steps.
        """
        pulumi.set(__self__, "selectors", selectors)
        pulumi.set(__self__, "steps", steps)

    @property
    @pulumi.getter
    def selectors(self) -> Sequence[Any]:
        """
        List of selectors.
        """
        return pulumi.get(self, "selectors")

    @property
    @pulumi.getter
    def steps(self) -> Sequence['outputs.StepResponse']:
        """
        List of steps.
        """
        return pulumi.get(self, "steps")


@pulumi.output_type
class KeyValuePairResponse(dict):
    """
    A map to describe the settings of an action.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A map to describe the settings of an action.
        :param str key: The name of the setting for the action.
        :param str value: The value of the setting for the action.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The name of the setting for the action.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value of the setting for the action.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ListSelectorResponse(dict):
    """
    Model that represents a list selector.
    """
    def __init__(__self__, *,
                 id: str,
                 targets: Sequence['outputs.TargetReferenceResponse'],
                 type: str,
                 filter: Optional['outputs.SimpleFilterResponse'] = None):
        """
        Model that represents a list selector.
        :param str id: String of the selector ID.
        :param Sequence['TargetReferenceResponse'] targets: List of Target references.
        :param str type: Enum of the selector type.
               Expected value is 'List'.
        :param 'SimpleFilterResponse' filter: Model that represents available filter types that can be applied to a targets list.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "targets", targets)
        pulumi.set(__self__, "type", 'List')
        if filter is not None:
            pulumi.set(__self__, "filter", filter)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        String of the selector ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def targets(self) -> Sequence['outputs.TargetReferenceResponse']:
        """
        List of Target references.
        """
        return pulumi.get(self, "targets")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Enum of the selector type.
        Expected value is 'List'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.SimpleFilterResponse']:
        """
        Model that represents available filter types that can be applied to a targets list.
        """
        return pulumi.get(self, "filter")


@pulumi.output_type
class QuerySelectorResponse(dict):
    """
    Model that represents a query selector.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "queryString":
            suggest = "query_string"
        elif key == "subscriptionIds":
            suggest = "subscription_ids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in QuerySelectorResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        QuerySelectorResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        QuerySelectorResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 query_string: str,
                 subscription_ids: Sequence[str],
                 type: str,
                 filter: Optional['outputs.SimpleFilterResponse'] = None):
        """
        Model that represents a query selector.
        :param str id: String of the selector ID.
        :param str query_string: Azure Resource Graph (ARG) Query Language query for target resources.
        :param Sequence[str] subscription_ids: Subscription id list to scope resource query.
        :param str type: Enum of the selector type.
               Expected value is 'Query'.
        :param 'SimpleFilterResponse' filter: Model that represents available filter types that can be applied to a targets list.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "query_string", query_string)
        pulumi.set(__self__, "subscription_ids", subscription_ids)
        pulumi.set(__self__, "type", 'Query')
        if filter is not None:
            pulumi.set(__self__, "filter", filter)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        String of the selector ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="queryString")
    def query_string(self) -> str:
        """
        Azure Resource Graph (ARG) Query Language query for target resources.
        """
        return pulumi.get(self, "query_string")

    @property
    @pulumi.getter(name="subscriptionIds")
    def subscription_ids(self) -> Sequence[str]:
        """
        Subscription id list to scope resource query.
        """
        return pulumi.get(self, "subscription_ids")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Enum of the selector type.
        Expected value is 'Query'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.SimpleFilterResponse']:
        """
        Model that represents available filter types that can be applied to a targets list.
        """
        return pulumi.get(self, "filter")


@pulumi.output_type
class ResourceIdentityResponse(dict):
    """
    The identity of a resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "userAssignedIdentities":
            suggest = "user_assigned_identities"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResourceIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResourceIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResourceIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: str,
                 user_assigned_identities: Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']] = None):
        """
        The identity of a resource.
        :param str principal_id: GUID that represents the principal ID of this resource identity.
        :param str tenant_id: GUID that represents the tenant ID of this resource identity.
        :param str type: String of the resource identity type.
        :param Mapping[str, 'UserAssignedIdentityResponse'] user_assigned_identities: The list of user identities associated with the Experiment. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        GUID that represents the principal ID of this resource identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        GUID that represents the tenant ID of this resource identity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        String of the resource identity type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']]:
        """
        The list of user identities associated with the Experiment. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        return pulumi.get(self, "user_assigned_identities")


@pulumi.output_type
class SimpleFilterParametersResponse(dict):
    """
    Model that represents the Simple filter parameters.
    """
    def __init__(__self__, *,
                 zones: Optional[Sequence[str]] = None):
        """
        Model that represents the Simple filter parameters.
        :param Sequence[str] zones: List of Azure availability zones to filter targets by.
        """
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        List of Azure availability zones to filter targets by.
        """
        return pulumi.get(self, "zones")


@pulumi.output_type
class SimpleFilterResponse(dict):
    """
    Model that represents a simple target filter.
    """
    def __init__(__self__, *,
                 type: str,
                 parameters: Optional['outputs.SimpleFilterParametersResponse'] = None):
        """
        Model that represents a simple target filter.
        :param str type: Enum that discriminates between filter types. Currently only `Simple` type is supported.
               Expected value is 'Simple'.
        :param 'SimpleFilterParametersResponse' parameters: Model that represents the Simple filter parameters.
        """
        pulumi.set(__self__, "type", 'Simple')
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Enum that discriminates between filter types. Currently only `Simple` type is supported.
        Expected value is 'Simple'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def parameters(self) -> Optional['outputs.SimpleFilterParametersResponse']:
        """
        Model that represents the Simple filter parameters.
        """
        return pulumi.get(self, "parameters")


@pulumi.output_type
class StepResponse(dict):
    """
    Model that represents a step in the Experiment resource.
    """
    def __init__(__self__, *,
                 branches: Sequence['outputs.BranchResponse'],
                 name: str):
        """
        Model that represents a step in the Experiment resource.
        :param Sequence['BranchResponse'] branches: List of branches.
        :param str name: String of the step name.
        """
        pulumi.set(__self__, "branches", branches)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def branches(self) -> Sequence['outputs.BranchResponse']:
        """
        List of branches.
        """
        return pulumi.get(self, "branches")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        String of the step name.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


@pulumi.output_type
class TargetReferenceResponse(dict):
    """
    Model that represents a reference to a Target in the selector.
    """
    def __init__(__self__, *,
                 id: str,
                 type: str):
        """
        Model that represents a reference to a Target in the selector.
        :param str id: String of the resource ID of a Target resource.
        :param str type: Enum of the Target reference type.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        String of the resource ID of a Target resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Enum of the Target reference type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class UserAssignedIdentityResponse(dict):
    """
    User assigned identity properties
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"
        elif key == "principalId":
            suggest = "principal_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in UserAssignedIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        UserAssignedIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        UserAssignedIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: str,
                 principal_id: str):
        """
        User assigned identity properties
        :param str client_id: The client ID of the assigned identity.
        :param str principal_id: The principal ID of the assigned identity.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "principal_id", principal_id)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The client ID of the assigned identity.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of the assigned identity.
        """
        return pulumi.get(self, "principal_id")


