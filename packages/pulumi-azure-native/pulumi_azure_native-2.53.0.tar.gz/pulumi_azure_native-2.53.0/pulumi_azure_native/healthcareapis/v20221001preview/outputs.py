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
    'AnalyticsConnectorDataLakeDataDestinationResponse',
    'AnalyticsConnectorFhirServiceDataSourceResponse',
    'AnalyticsConnectorFhirToParquetMappingResponse',
    'ServiceManagedIdentityResponseIdentity',
    'SystemDataResponse',
    'UserAssignedIdentityResponse',
]

@pulumi.output_type
class AnalyticsConnectorDataLakeDataDestinationResponse(dict):
    """
    The Data Lake data destination for Analytics Connector.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataLakeName":
            suggest = "data_lake_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AnalyticsConnectorDataLakeDataDestinationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AnalyticsConnectorDataLakeDataDestinationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AnalyticsConnectorDataLakeDataDestinationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 data_lake_name: str,
                 type: str,
                 name: Optional[str] = None):
        """
        The Data Lake data destination for Analytics Connector.
        :param str data_lake_name: The name for the Data Lake.
        :param str type: Type of data destination.
               Expected value is 'datalake'.
        :param str name: Name of data destination.
        """
        pulumi.set(__self__, "data_lake_name", data_lake_name)
        pulumi.set(__self__, "type", 'datalake')
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="dataLakeName")
    def data_lake_name(self) -> str:
        """
        The name for the Data Lake.
        """
        return pulumi.get(self, "data_lake_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of data destination.
        Expected value is 'datalake'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of data destination.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class AnalyticsConnectorFhirServiceDataSourceResponse(dict):
    """
    The FHIR service data source for Analytics Connector.
    """
    def __init__(__self__, *,
                 kind: str,
                 type: str,
                 url: str):
        """
        The FHIR service data source for Analytics Connector.
        :param str kind: The kind of FHIR Service.
        :param str type: Type of data source.
               Expected value is 'fhirservice'.
        :param str url: The URL of FHIR service.
        """
        pulumi.set(__self__, "kind", kind)
        pulumi.set(__self__, "type", 'fhirservice')
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of FHIR Service.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of data source.
        Expected value is 'fhirservice'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def url(self) -> str:
        """
        The URL of FHIR service.
        """
        return pulumi.get(self, "url")


@pulumi.output_type
class AnalyticsConnectorFhirToParquetMappingResponse(dict):
    """
    FHIR Service data mapping configuration for Analytics Connector.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "extensionSchemaReference":
            suggest = "extension_schema_reference"
        elif key == "filterConfigurationReference":
            suggest = "filter_configuration_reference"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AnalyticsConnectorFhirToParquetMappingResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AnalyticsConnectorFhirToParquetMappingResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AnalyticsConnectorFhirToParquetMappingResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: str,
                 extension_schema_reference: Optional[str] = None,
                 filter_configuration_reference: Optional[str] = None):
        """
        FHIR Service data mapping configuration for Analytics Connector.
        :param str type: Type of data mapping.
               Expected value is 'fhirToParquet'.
        :param str extension_schema_reference: Artifact reference for extension schema.
        :param str filter_configuration_reference: Artifact reference for filter configurations.
        """
        pulumi.set(__self__, "type", 'fhirToParquet')
        if extension_schema_reference is not None:
            pulumi.set(__self__, "extension_schema_reference", extension_schema_reference)
        if filter_configuration_reference is not None:
            pulumi.set(__self__, "filter_configuration_reference", filter_configuration_reference)

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of data mapping.
        Expected value is 'fhirToParquet'.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="extensionSchemaReference")
    def extension_schema_reference(self) -> Optional[str]:
        """
        Artifact reference for extension schema.
        """
        return pulumi.get(self, "extension_schema_reference")

    @property
    @pulumi.getter(name="filterConfigurationReference")
    def filter_configuration_reference(self) -> Optional[str]:
        """
        Artifact reference for filter configurations.
        """
        return pulumi.get(self, "filter_configuration_reference")


@pulumi.output_type
class ServiceManagedIdentityResponseIdentity(dict):
    """
    Setting indicating whether the service has a managed identity associated with it.
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
            pulumi.log.warn(f"Key '{key}' not found in ServiceManagedIdentityResponseIdentity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceManagedIdentityResponseIdentity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceManagedIdentityResponseIdentity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: str,
                 user_assigned_identities: Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']] = None):
        """
        Setting indicating whether the service has a managed identity associated with it.
        :param str principal_id: The service principal ID of the system assigned identity. This property will only be provided for a system assigned identity.
        :param str tenant_id: The tenant ID of the system assigned identity. This property will only be provided for a system assigned identity.
        :param str type: Type of identity being specified, currently SystemAssigned and None are allowed.
        :param Mapping[str, 'UserAssignedIdentityResponse'] user_assigned_identities: The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
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
        The service principal ID of the system assigned identity. This property will only be provided for a system assigned identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of the system assigned identity. This property will only be provided for a system assigned identity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of identity being specified, currently SystemAssigned and None are allowed.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")


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


