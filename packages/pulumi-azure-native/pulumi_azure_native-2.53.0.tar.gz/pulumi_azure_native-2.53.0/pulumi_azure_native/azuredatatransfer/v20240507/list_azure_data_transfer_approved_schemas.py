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
    'ListAzureDataTransferApprovedSchemasResult',
    'AwaitableListAzureDataTransferApprovedSchemasResult',
    'list_azure_data_transfer_approved_schemas',
    'list_azure_data_transfer_approved_schemas_output',
]

@pulumi.output_type
class ListAzureDataTransferApprovedSchemasResult:
    """
    The schemas list result.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.SchemaResponse']]:
        """
        Schemas array.
        """
        return pulumi.get(self, "value")


class AwaitableListAzureDataTransferApprovedSchemasResult(ListAzureDataTransferApprovedSchemasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAzureDataTransferApprovedSchemasResult(
            value=self.value)


def list_azure_data_transfer_approved_schemas(direction: Optional[Union[str, 'ListApprovedSchemasDirection']] = None,
                                              pipeline: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAzureDataTransferApprovedSchemasResult:
    """
    Lists approved schemas for Azure Data Transfer.


    :param Union[str, 'ListApprovedSchemasDirection'] direction: The direction pipeline to filter approved schemas.
    :param str pipeline: The name of the pipeline to filter approved schemas.
    """
    __args__ = dict()
    __args__['direction'] = direction
    __args__['pipeline'] = pipeline
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azuredatatransfer/v20240507:listAzureDataTransferApprovedSchemas', __args__, opts=opts, typ=ListAzureDataTransferApprovedSchemasResult).value

    return AwaitableListAzureDataTransferApprovedSchemasResult(
        value=pulumi.get(__ret__, 'value'))


@_utilities.lift_output_func(list_azure_data_transfer_approved_schemas)
def list_azure_data_transfer_approved_schemas_output(direction: Optional[pulumi.Input[Optional[Union[str, 'ListApprovedSchemasDirection']]]] = None,
                                                     pipeline: Optional[pulumi.Input[Optional[str]]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListAzureDataTransferApprovedSchemasResult]:
    """
    Lists approved schemas for Azure Data Transfer.


    :param Union[str, 'ListApprovedSchemasDirection'] direction: The direction pipeline to filter approved schemas.
    :param str pipeline: The name of the pipeline to filter approved schemas.
    """
    ...
