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
    'ConnectorCollectionErrorInfoResponse',
    'ConnectorCollectionInfoResponse',
]

@pulumi.output_type
class ConnectorCollectionErrorInfoResponse(dict):
    """
    Details of any error encountered on last collection attempt
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "errorCode":
            suggest = "error_code"
        elif key == "errorInnerMessage":
            suggest = "error_inner_message"
        elif key == "errorMessage":
            suggest = "error_message"
        elif key == "errorStartTime":
            suggest = "error_start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConnectorCollectionErrorInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConnectorCollectionErrorInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConnectorCollectionErrorInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 error_code: str,
                 error_inner_message: str,
                 error_message: str,
                 error_start_time: str):
        """
        Details of any error encountered on last collection attempt
        :param str error_code: Short error code
        :param str error_inner_message: External Provider error message
        :param str error_message: Detailed error message
        :param str error_start_time: Time the error started occurring (Last time error occurred in lastChecked)
        """
        pulumi.set(__self__, "error_code", error_code)
        pulumi.set(__self__, "error_inner_message", error_inner_message)
        pulumi.set(__self__, "error_message", error_message)
        pulumi.set(__self__, "error_start_time", error_start_time)

    @property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> str:
        """
        Short error code
        """
        return pulumi.get(self, "error_code")

    @property
    @pulumi.getter(name="errorInnerMessage")
    def error_inner_message(self) -> str:
        """
        External Provider error message
        """
        return pulumi.get(self, "error_inner_message")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        """
        Detailed error message
        """
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter(name="errorStartTime")
    def error_start_time(self) -> str:
        """
        Time the error started occurring (Last time error occurred in lastChecked)
        """
        return pulumi.get(self, "error_start_time")


@pulumi.output_type
class ConnectorCollectionInfoResponse(dict):
    """
    Collection and ingestion information
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "lastChecked":
            suggest = "last_checked"
        elif key == "lastUpdated":
            suggest = "last_updated"
        elif key == "sourceLastUpdated":
            suggest = "source_last_updated"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ConnectorCollectionInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ConnectorCollectionInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ConnectorCollectionInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 last_checked: str,
                 last_updated: str,
                 source_last_updated: str,
                 error: Optional['outputs.ConnectorCollectionErrorInfoResponse'] = None):
        """
        Collection and ingestion information
        :param str last_checked: Last time the data acquisition process initiated connecting to the external provider
        :param str last_updated: Last time the external data was updated into Azure
        :param str source_last_updated: Source timestamp of external data currently available in Azure (eg AWS last processed CUR file timestamp)
        :param 'ConnectorCollectionErrorInfoResponse' error: Error information of last collection
        """
        pulumi.set(__self__, "last_checked", last_checked)
        pulumi.set(__self__, "last_updated", last_updated)
        pulumi.set(__self__, "source_last_updated", source_last_updated)
        if error is not None:
            pulumi.set(__self__, "error", error)

    @property
    @pulumi.getter(name="lastChecked")
    def last_checked(self) -> str:
        """
        Last time the data acquisition process initiated connecting to the external provider
        """
        return pulumi.get(self, "last_checked")

    @property
    @pulumi.getter(name="lastUpdated")
    def last_updated(self) -> str:
        """
        Last time the external data was updated into Azure
        """
        return pulumi.get(self, "last_updated")

    @property
    @pulumi.getter(name="sourceLastUpdated")
    def source_last_updated(self) -> str:
        """
        Source timestamp of external data currently available in Azure (eg AWS last processed CUR file timestamp)
        """
        return pulumi.get(self, "source_last_updated")

    @property
    @pulumi.getter
    def error(self) -> Optional['outputs.ConnectorCollectionErrorInfoResponse']:
        """
        Error information of last collection
        """
        return pulumi.get(self, "error")


