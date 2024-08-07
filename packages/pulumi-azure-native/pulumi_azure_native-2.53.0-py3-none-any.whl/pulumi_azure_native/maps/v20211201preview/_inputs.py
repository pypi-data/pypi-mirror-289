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
    'CorsRulesArgs',
    'CorsRulesArgsDict',
    'CorsRuleArgs',
    'CorsRuleArgsDict',
    'CreatorPropertiesArgs',
    'CreatorPropertiesArgsDict',
    'LinkedResourceArgs',
    'LinkedResourceArgsDict',
    'ManagedServiceIdentityArgs',
    'ManagedServiceIdentityArgsDict',
    'MapsAccountPropertiesArgs',
    'MapsAccountPropertiesArgsDict',
    'SkuArgs',
    'SkuArgsDict',
]

MYPY = False

if not MYPY:
    class CorsRulesArgsDict(TypedDict):
        """
        Sets the CORS rules. You can include up to five CorsRule elements in the request. 
        """
        cors_rules: NotRequired[pulumi.Input[Sequence[pulumi.Input['CorsRuleArgsDict']]]]
        """
        The list of CORS rules. You can include up to five CorsRule elements in the request. 
        """
elif False:
    CorsRulesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CorsRulesArgs:
    def __init__(__self__, *,
                 cors_rules: Optional[pulumi.Input[Sequence[pulumi.Input['CorsRuleArgs']]]] = None):
        """
        Sets the CORS rules. You can include up to five CorsRule elements in the request. 
        :param pulumi.Input[Sequence[pulumi.Input['CorsRuleArgs']]] cors_rules: The list of CORS rules. You can include up to five CorsRule elements in the request. 
        """
        if cors_rules is not None:
            pulumi.set(__self__, "cors_rules", cors_rules)

    @property
    @pulumi.getter(name="corsRules")
    def cors_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CorsRuleArgs']]]]:
        """
        The list of CORS rules. You can include up to five CorsRule elements in the request. 
        """
        return pulumi.get(self, "cors_rules")

    @cors_rules.setter
    def cors_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CorsRuleArgs']]]]):
        pulumi.set(self, "cors_rules", value)


if not MYPY:
    class CorsRuleArgsDict(TypedDict):
        """
        Specifies a CORS rule for the Map Account.
        """
        allowed_origins: pulumi.Input[Sequence[pulumi.Input[str]]]
        """
        Required if CorsRule element is present. A list of origin domains that will be allowed via CORS, or "*" to allow all domains
        """
elif False:
    CorsRuleArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CorsRuleArgs:
    def __init__(__self__, *,
                 allowed_origins: pulumi.Input[Sequence[pulumi.Input[str]]]):
        """
        Specifies a CORS rule for the Map Account.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_origins: Required if CorsRule element is present. A list of origin domains that will be allowed via CORS, or "*" to allow all domains
        """
        pulumi.set(__self__, "allowed_origins", allowed_origins)

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Required if CorsRule element is present. A list of origin domains that will be allowed via CORS, or "*" to allow all domains
        """
        return pulumi.get(self, "allowed_origins")

    @allowed_origins.setter
    def allowed_origins(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "allowed_origins", value)


if not MYPY:
    class CreatorPropertiesArgsDict(TypedDict):
        """
        Creator resource properties
        """
        storage_units: pulumi.Input[int]
        """
        The storage units to be allocated. Integer values from 1 to 100, inclusive.
        """
elif False:
    CreatorPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CreatorPropertiesArgs:
    def __init__(__self__, *,
                 storage_units: pulumi.Input[int]):
        """
        Creator resource properties
        :param pulumi.Input[int] storage_units: The storage units to be allocated. Integer values from 1 to 100, inclusive.
        """
        pulumi.set(__self__, "storage_units", storage_units)

    @property
    @pulumi.getter(name="storageUnits")
    def storage_units(self) -> pulumi.Input[int]:
        """
        The storage units to be allocated. Integer values from 1 to 100, inclusive.
        """
        return pulumi.get(self, "storage_units")

    @storage_units.setter
    def storage_units(self, value: pulumi.Input[int]):
        pulumi.set(self, "storage_units", value)


if not MYPY:
    class LinkedResourceArgsDict(TypedDict):
        """
        Linked resource is reference to a resource deployed in an Azure subscription, add the linked resource `uniqueName` value as an optional parameter for operations on Azure Maps Geospatial REST APIs.
        """
        id: pulumi.Input[str]
        """
        ARM resource id in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/accounts/{storageName}'.
        """
        unique_name: pulumi.Input[str]
        """
        A provided name which uniquely identifies the linked resource.
        """
elif False:
    LinkedResourceArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class LinkedResourceArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 unique_name: pulumi.Input[str]):
        """
        Linked resource is reference to a resource deployed in an Azure subscription, add the linked resource `uniqueName` value as an optional parameter for operations on Azure Maps Geospatial REST APIs.
        :param pulumi.Input[str] id: ARM resource id in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/accounts/{storageName}'.
        :param pulumi.Input[str] unique_name: A provided name which uniquely identifies the linked resource.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "unique_name", unique_name)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        ARM resource id in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/accounts/{storageName}'.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="uniqueName")
    def unique_name(self) -> pulumi.Input[str]:
        """
        A provided name which uniquely identifies the linked resource.
        """
        return pulumi.get(self, "unique_name")

    @unique_name.setter
    def unique_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "unique_name", value)


if not MYPY:
    class ManagedServiceIdentityArgsDict(TypedDict):
        """
        Identity for the resource.
        """
        type: NotRequired[pulumi.Input['ResourceIdentityType']]
        """
        The identity type.
        """
        user_assigned_identities: NotRequired[pulumi.Input[Sequence[pulumi.Input[str]]]]
        """
        The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
elif False:
    ManagedServiceIdentityArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class ManagedServiceIdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input['ResourceIdentityType']] = None,
                 user_assigned_identities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Identity for the resource.
        :param pulumi.Input['ResourceIdentityType'] type: The identity type.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] user_assigned_identities: The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        if type is not None:
            pulumi.set(__self__, "type", type)
        if user_assigned_identities is not None:
            pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['ResourceIdentityType']]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['ResourceIdentityType']]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The list of user identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}'.
        """
        return pulumi.get(self, "user_assigned_identities")

    @user_assigned_identities.setter
    def user_assigned_identities(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "user_assigned_identities", value)


if not MYPY:
    class MapsAccountPropertiesArgsDict(TypedDict):
        """
        Additional Map account properties
        """
        cors: NotRequired[pulumi.Input['CorsRulesArgsDict']]
        """
        Specifies CORS rules for the Blob service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Blob service.
        """
        disable_local_auth: NotRequired[pulumi.Input[bool]]
        """
        Allows toggle functionality on Azure Policy to disable Azure Maps local authentication support. This will disable Shared Keys authentication from any usage.
        """
        linked_resources: NotRequired[pulumi.Input[Sequence[pulumi.Input['LinkedResourceArgsDict']]]]
        """
        Sets the resources to be used for Managed Identities based operations for the Map account resource.
        """
elif False:
    MapsAccountPropertiesArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class MapsAccountPropertiesArgs:
    def __init__(__self__, *,
                 cors: Optional[pulumi.Input['CorsRulesArgs']] = None,
                 disable_local_auth: Optional[pulumi.Input[bool]] = None,
                 linked_resources: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedResourceArgs']]]] = None):
        """
        Additional Map account properties
        :param pulumi.Input['CorsRulesArgs'] cors: Specifies CORS rules for the Blob service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Blob service.
        :param pulumi.Input[bool] disable_local_auth: Allows toggle functionality on Azure Policy to disable Azure Maps local authentication support. This will disable Shared Keys authentication from any usage.
        :param pulumi.Input[Sequence[pulumi.Input['LinkedResourceArgs']]] linked_resources: Sets the resources to be used for Managed Identities based operations for the Map account resource.
        """
        if cors is not None:
            pulumi.set(__self__, "cors", cors)
        if disable_local_auth is None:
            disable_local_auth = False
        if disable_local_auth is not None:
            pulumi.set(__self__, "disable_local_auth", disable_local_auth)
        if linked_resources is not None:
            pulumi.set(__self__, "linked_resources", linked_resources)

    @property
    @pulumi.getter
    def cors(self) -> Optional[pulumi.Input['CorsRulesArgs']]:
        """
        Specifies CORS rules for the Blob service. You can include up to five CorsRule elements in the request. If no CorsRule elements are included in the request body, all CORS rules will be deleted, and CORS will be disabled for the Blob service.
        """
        return pulumi.get(self, "cors")

    @cors.setter
    def cors(self, value: Optional[pulumi.Input['CorsRulesArgs']]):
        pulumi.set(self, "cors", value)

    @property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[bool]]:
        """
        Allows toggle functionality on Azure Policy to disable Azure Maps local authentication support. This will disable Shared Keys authentication from any usage.
        """
        return pulumi.get(self, "disable_local_auth")

    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_local_auth", value)

    @property
    @pulumi.getter(name="linkedResources")
    def linked_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LinkedResourceArgs']]]]:
        """
        Sets the resources to be used for Managed Identities based operations for the Map account resource.
        """
        return pulumi.get(self, "linked_resources")

    @linked_resources.setter
    def linked_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LinkedResourceArgs']]]]):
        pulumi.set(self, "linked_resources", value)


if not MYPY:
    class SkuArgsDict(TypedDict):
        """
        The SKU of the Maps Account.
        """
        name: pulumi.Input[Union[str, 'Name']]
        """
        The name of the SKU, in standard format (such as S0).
        """
elif False:
    SkuArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class SkuArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[Union[str, 'Name']]):
        """
        The SKU of the Maps Account.
        :param pulumi.Input[Union[str, 'Name']] name: The name of the SKU, in standard format (such as S0).
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[str, 'Name']]:
        """
        The name of the SKU, in standard format (such as S0).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[Union[str, 'Name']]):
        pulumi.set(self, "name", value)


