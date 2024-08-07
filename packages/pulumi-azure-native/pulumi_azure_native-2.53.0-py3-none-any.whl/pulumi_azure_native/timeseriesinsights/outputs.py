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
from ._enums import *

__all__ = [
    'EnvironmentStateDetailsResponse',
    'EnvironmentStatusResponse',
    'Gen2StorageConfigurationOutputResponse',
    'IngressEnvironmentStatusResponse',
    'LocalTimestampResponse',
    'LocalTimestampResponseTimeZoneOffset',
    'PrivateEndpointResponse',
    'PrivateLinkServiceConnectionStateResponse',
    'ReferenceDataSetKeyPropertyResponse',
    'SkuResponse',
    'TimeSeriesIdPropertyResponse',
    'WarmStorageEnvironmentStatusResponse',
    'WarmStoreConfigurationPropertiesResponse',
]

@pulumi.output_type
class EnvironmentStateDetailsResponse(dict):
    """
    An object that contains the details about an environment's state.
    """
    def __init__(__self__, *,
                 code: Optional[str] = None,
                 message: Optional[str] = None):
        """
        An object that contains the details about an environment's state.
        :param str code: Contains the code that represents the reason of an environment being in a particular state. Can be used to programmatically handle specific cases.
        :param str message: A message that describes the state in detail.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def code(self) -> Optional[str]:
        """
        Contains the code that represents the reason of an environment being in a particular state. Can be used to programmatically handle specific cases.
        """
        return pulumi.get(self, "code")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        A message that describes the state in detail.
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class EnvironmentStatusResponse(dict):
    """
    An object that represents the status of the environment, and its internal state in the Time Series Insights service.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "warmStorage":
            suggest = "warm_storage"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EnvironmentStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EnvironmentStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EnvironmentStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ingress: 'outputs.IngressEnvironmentStatusResponse',
                 warm_storage: 'outputs.WarmStorageEnvironmentStatusResponse'):
        """
        An object that represents the status of the environment, and its internal state in the Time Series Insights service.
        :param 'IngressEnvironmentStatusResponse' ingress: An object that represents the status of ingress on an environment.
        :param 'WarmStorageEnvironmentStatusResponse' warm_storage: An object that represents the status of warm storage on an environment.
        """
        pulumi.set(__self__, "ingress", ingress)
        pulumi.set(__self__, "warm_storage", warm_storage)

    @property
    @pulumi.getter
    def ingress(self) -> 'outputs.IngressEnvironmentStatusResponse':
        """
        An object that represents the status of ingress on an environment.
        """
        return pulumi.get(self, "ingress")

    @property
    @pulumi.getter(name="warmStorage")
    def warm_storage(self) -> 'outputs.WarmStorageEnvironmentStatusResponse':
        """
        An object that represents the status of warm storage on an environment.
        """
        return pulumi.get(self, "warm_storage")


@pulumi.output_type
class Gen2StorageConfigurationOutputResponse(dict):
    """
    The storage configuration provides the non-secret connection details about the customer storage account that is used to store the environment's data.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accountName":
            suggest = "account_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Gen2StorageConfigurationOutputResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Gen2StorageConfigurationOutputResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Gen2StorageConfigurationOutputResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 account_name: str):
        """
        The storage configuration provides the non-secret connection details about the customer storage account that is used to store the environment's data.
        :param str account_name: The name of the storage account that will hold the environment's Gen2 data.
        """
        pulumi.set(__self__, "account_name", account_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        """
        The name of the storage account that will hold the environment's Gen2 data.
        """
        return pulumi.get(self, "account_name")


@pulumi.output_type
class IngressEnvironmentStatusResponse(dict):
    """
    An object that represents the status of ingress on an environment.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "stateDetails":
            suggest = "state_details"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IngressEnvironmentStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IngressEnvironmentStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IngressEnvironmentStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 state_details: 'outputs.EnvironmentStateDetailsResponse',
                 state: Optional[str] = None):
        """
        An object that represents the status of ingress on an environment.
        :param 'EnvironmentStateDetailsResponse' state_details: An object that contains the details about an environment's state.
        :param str state: This string represents the state of ingress operations on an environment. It can be "Disabled", "Ready", "Running", "Paused" or "Unknown"
        """
        pulumi.set(__self__, "state_details", state_details)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="stateDetails")
    def state_details(self) -> 'outputs.EnvironmentStateDetailsResponse':
        """
        An object that contains the details about an environment's state.
        """
        return pulumi.get(self, "state_details")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        This string represents the state of ingress operations on an environment. It can be "Disabled", "Ready", "Running", "Paused" or "Unknown"
        """
        return pulumi.get(self, "state")


@pulumi.output_type
class LocalTimestampResponse(dict):
    """
    An object that represents the local timestamp property. It contains the format of local timestamp that needs to be used and the corresponding timezone offset information. If a value isn't specified for localTimestamp, or if null, then the local timestamp will not be ingressed with the events.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "timeZoneOffset":
            suggest = "time_zone_offset"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LocalTimestampResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LocalTimestampResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LocalTimestampResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 format: Optional[str] = None,
                 time_zone_offset: Optional['outputs.LocalTimestampResponseTimeZoneOffset'] = None):
        """
        An object that represents the local timestamp property. It contains the format of local timestamp that needs to be used and the corresponding timezone offset information. If a value isn't specified for localTimestamp, or if null, then the local timestamp will not be ingressed with the events.
        :param str format: An enum that represents the format of the local timestamp property that needs to be set.
        :param 'LocalTimestampResponseTimeZoneOffset' time_zone_offset: An object that represents the offset information for the local timestamp format specified. Should not be specified for LocalTimestampFormat - Embedded.
        """
        if format is not None:
            pulumi.set(__self__, "format", format)
        if time_zone_offset is not None:
            pulumi.set(__self__, "time_zone_offset", time_zone_offset)

    @property
    @pulumi.getter
    def format(self) -> Optional[str]:
        """
        An enum that represents the format of the local timestamp property that needs to be set.
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter(name="timeZoneOffset")
    def time_zone_offset(self) -> Optional['outputs.LocalTimestampResponseTimeZoneOffset']:
        """
        An object that represents the offset information for the local timestamp format specified. Should not be specified for LocalTimestampFormat - Embedded.
        """
        return pulumi.get(self, "time_zone_offset")


@pulumi.output_type
class LocalTimestampResponseTimeZoneOffset(dict):
    """
    An object that represents the offset information for the local timestamp format specified. Should not be specified for LocalTimestampFormat - Embedded.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "propertyName":
            suggest = "property_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in LocalTimestampResponseTimeZoneOffset. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        LocalTimestampResponseTimeZoneOffset.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        LocalTimestampResponseTimeZoneOffset.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 property_name: Optional[str] = None):
        """
        An object that represents the offset information for the local timestamp format specified. Should not be specified for LocalTimestampFormat - Embedded.
        :param str property_name: The event property that will be contain the offset information to calculate the local timestamp. When the LocalTimestampFormat is Iana, the property name will contain the name of the column which contains IANA Timezone Name (eg: Americas/Los Angeles). When LocalTimestampFormat is Timespan, it contains the name of property which contains values representing the offset (eg: P1D or 1.00:00:00)
        """
        if property_name is not None:
            pulumi.set(__self__, "property_name", property_name)

    @property
    @pulumi.getter(name="propertyName")
    def property_name(self) -> Optional[str]:
        """
        The event property that will be contain the offset information to calculate the local timestamp. When the LocalTimestampFormat is Iana, the property name will contain the name of the column which contains IANA Timezone Name (eg: Americas/Los Angeles). When LocalTimestampFormat is Timespan, it contains the name of property which contains values representing the offset (eg: P1D or 1.00:00:00)
        """
        return pulumi.get(self, "property_name")


@pulumi.output_type
class PrivateEndpointResponse(dict):
    """
    The Private Endpoint resource.
    """
    def __init__(__self__, *,
                 id: str):
        """
        The Private Endpoint resource.
        :param str id: The ARM identifier for Private Endpoint
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM identifier for Private Endpoint
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    """
    A collection of information about the state of the connection between service consumer and provider.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionsRequired":
            suggest = "actions_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateLinkServiceConnectionStateResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions_required: Optional[str] = None,
                 description: Optional[str] = None,
                 status: Optional[str] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param str actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param str description: The reason for approval/rejection of the connection.
        :param str status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[str]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class ReferenceDataSetKeyPropertyResponse(dict):
    """
    A key property for the reference data set. A reference data set can have multiple key properties.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 type: Optional[str] = None):
        """
        A key property for the reference data set. A reference data set can have multiple key properties.
        :param str name: The name of the key property.
        :param str type: The type of the key property.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the key property.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of the key property.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class SkuResponse(dict):
    """
    The sku determines the type of environment, either Gen1 (S1 or S2) or Gen2 (L1). For Gen1 environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
    """
    def __init__(__self__, *,
                 capacity: int,
                 name: str):
        """
        The sku determines the type of environment, either Gen1 (S1 or S2) or Gen2 (L1). For Gen1 environments the sku determines the capacity of the environment, the ingress rate, and the billing rate.
        :param int capacity: The capacity of the sku. For Gen1 environments, this value can be changed to support scale out of environments after they have been created.
        :param str name: The name of this SKU.
        """
        pulumi.set(__self__, "capacity", capacity)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> int:
        """
        The capacity of the sku. For Gen1 environments, this value can be changed to support scale out of environments after they have been created.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of this SKU.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class TimeSeriesIdPropertyResponse(dict):
    """
    The structure of the property that a time series id can have. An environment can have multiple such properties.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 type: Optional[str] = None):
        """
        The structure of the property that a time series id can have. An environment can have multiple such properties.
        :param str name: The name of the property.
        :param str type: The type of the property.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the property.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of the property.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class WarmStorageEnvironmentStatusResponse(dict):
    """
    An object that represents the status of warm storage on an environment.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "currentCount":
            suggest = "current_count"
        elif key == "maxCount":
            suggest = "max_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WarmStorageEnvironmentStatusResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WarmStorageEnvironmentStatusResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WarmStorageEnvironmentStatusResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 current_count: Optional[int] = None,
                 max_count: Optional[int] = None,
                 state: Optional[str] = None):
        """
        An object that represents the status of warm storage on an environment.
        :param int current_count: A value that represents the number of properties used by the environment for S1/S2 SKU and number of properties used by Warm Store for PAYG SKU
        :param int max_count: A value that represents the maximum number of properties used allowed by the environment for S1/S2 SKU and maximum number of properties allowed by Warm Store for PAYG SKU.
        :param str state: This string represents the state of warm storage properties usage. It can be "Ok", "Error", "Unknown".
        """
        if current_count is not None:
            pulumi.set(__self__, "current_count", current_count)
        if max_count is not None:
            pulumi.set(__self__, "max_count", max_count)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="currentCount")
    def current_count(self) -> Optional[int]:
        """
        A value that represents the number of properties used by the environment for S1/S2 SKU and number of properties used by Warm Store for PAYG SKU
        """
        return pulumi.get(self, "current_count")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[int]:
        """
        A value that represents the maximum number of properties used allowed by the environment for S1/S2 SKU and maximum number of properties allowed by Warm Store for PAYG SKU.
        """
        return pulumi.get(self, "max_count")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        This string represents the state of warm storage properties usage. It can be "Ok", "Error", "Unknown".
        """
        return pulumi.get(self, "state")


@pulumi.output_type
class WarmStoreConfigurationPropertiesResponse(dict):
    """
    The warm store configuration provides the details to create a warm store cache that will retain a copy of the environment's data available for faster query.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dataRetention":
            suggest = "data_retention"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WarmStoreConfigurationPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WarmStoreConfigurationPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WarmStoreConfigurationPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 data_retention: str):
        """
        The warm store configuration provides the details to create a warm store cache that will retain a copy of the environment's data available for faster query.
        :param str data_retention: ISO8601 timespan specifying the number of days the environment's events will be available for query from the warm store.
        """
        pulumi.set(__self__, "data_retention", data_retention)

    @property
    @pulumi.getter(name="dataRetention")
    def data_retention(self) -> str:
        """
        ISO8601 timespan specifying the number of days the environment's events will be available for query from the warm store.
        """
        return pulumi.get(self, "data_retention")


