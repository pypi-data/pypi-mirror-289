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

__all__ = ['DataTypeArgs', 'DataType']

@pulumi.input_type
class DataTypeArgs:
    def __init__(__self__, *,
                 data_product_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 data_type_name: Optional[pulumi.Input[str]] = None,
                 database_cache_retention: Optional[pulumi.Input[int]] = None,
                 database_retention: Optional[pulumi.Input[int]] = None,
                 state: Optional[pulumi.Input[Union[str, 'DataTypeState']]] = None,
                 storage_output_retention: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a DataType resource.
        :param pulumi.Input[str] data_product_name: The data product resource name
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] data_type_name: The data type name.
        :param pulumi.Input[int] database_cache_retention: Field for database cache retention in days.
        :param pulumi.Input[int] database_retention: Field for database data retention in days.
        :param pulumi.Input[Union[str, 'DataTypeState']] state: State of data type.
        :param pulumi.Input[int] storage_output_retention: Field for storage output retention in days.
        """
        pulumi.set(__self__, "data_product_name", data_product_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if data_type_name is not None:
            pulumi.set(__self__, "data_type_name", data_type_name)
        if database_cache_retention is not None:
            pulumi.set(__self__, "database_cache_retention", database_cache_retention)
        if database_retention is not None:
            pulumi.set(__self__, "database_retention", database_retention)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if storage_output_retention is not None:
            pulumi.set(__self__, "storage_output_retention", storage_output_retention)

    @property
    @pulumi.getter(name="dataProductName")
    def data_product_name(self) -> pulumi.Input[str]:
        """
        The data product resource name
        """
        return pulumi.get(self, "data_product_name")

    @data_product_name.setter
    def data_product_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_product_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dataTypeName")
    def data_type_name(self) -> Optional[pulumi.Input[str]]:
        """
        The data type name.
        """
        return pulumi.get(self, "data_type_name")

    @data_type_name.setter
    def data_type_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data_type_name", value)

    @property
    @pulumi.getter(name="databaseCacheRetention")
    def database_cache_retention(self) -> Optional[pulumi.Input[int]]:
        """
        Field for database cache retention in days.
        """
        return pulumi.get(self, "database_cache_retention")

    @database_cache_retention.setter
    def database_cache_retention(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "database_cache_retention", value)

    @property
    @pulumi.getter(name="databaseRetention")
    def database_retention(self) -> Optional[pulumi.Input[int]]:
        """
        Field for database data retention in days.
        """
        return pulumi.get(self, "database_retention")

    @database_retention.setter
    def database_retention(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "database_retention", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'DataTypeState']]]:
        """
        State of data type.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'DataTypeState']]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="storageOutputRetention")
    def storage_output_retention(self) -> Optional[pulumi.Input[int]]:
        """
        Field for storage output retention in days.
        """
        return pulumi.get(self, "storage_output_retention")

    @storage_output_retention.setter
    def storage_output_retention(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "storage_output_retention", value)


class DataType(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_product_name: Optional[pulumi.Input[str]] = None,
                 data_type_name: Optional[pulumi.Input[str]] = None,
                 database_cache_retention: Optional[pulumi.Input[int]] = None,
                 database_retention: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'DataTypeState']]] = None,
                 storage_output_retention: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        The data type resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] data_product_name: The data product resource name
        :param pulumi.Input[str] data_type_name: The data type name.
        :param pulumi.Input[int] database_cache_retention: Field for database cache retention in days.
        :param pulumi.Input[int] database_retention: Field for database data retention in days.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'DataTypeState']] state: State of data type.
        :param pulumi.Input[int] storage_output_retention: Field for storage output retention in days.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DataTypeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The data type resource.

        :param str resource_name: The name of the resource.
        :param DataTypeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DataTypeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_product_name: Optional[pulumi.Input[str]] = None,
                 data_type_name: Optional[pulumi.Input[str]] = None,
                 database_cache_retention: Optional[pulumi.Input[int]] = None,
                 database_retention: Optional[pulumi.Input[int]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'DataTypeState']]] = None,
                 storage_output_retention: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DataTypeArgs.__new__(DataTypeArgs)

            if data_product_name is None and not opts.urn:
                raise TypeError("Missing required property 'data_product_name'")
            __props__.__dict__["data_product_name"] = data_product_name
            __props__.__dict__["data_type_name"] = data_type_name
            __props__.__dict__["database_cache_retention"] = database_cache_retention
            __props__.__dict__["database_retention"] = database_retention
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["state"] = state
            __props__.__dict__["storage_output_retention"] = storage_output_retention
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["state_reason"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["visualization_url"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkanalytics:DataType")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DataType, __self__).__init__(
            'azure-native:networkanalytics/v20231115:DataType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DataType':
        """
        Get an existing DataType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DataTypeArgs.__new__(DataTypeArgs)

        __props__.__dict__["database_cache_retention"] = None
        __props__.__dict__["database_retention"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["state_reason"] = None
        __props__.__dict__["storage_output_retention"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["visualization_url"] = None
        return DataType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="databaseCacheRetention")
    def database_cache_retention(self) -> pulumi.Output[Optional[int]]:
        """
        Field for database cache retention in days.
        """
        return pulumi.get(self, "database_cache_retention")

    @property
    @pulumi.getter(name="databaseRetention")
    def database_retention(self) -> pulumi.Output[Optional[int]]:
        """
        Field for database data retention in days.
        """
        return pulumi.get(self, "database_retention")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Latest provisioning state  of data product.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        State of data type.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="stateReason")
    def state_reason(self) -> pulumi.Output[str]:
        """
        Reason for the state of data type.
        """
        return pulumi.get(self, "state_reason")

    @property
    @pulumi.getter(name="storageOutputRetention")
    def storage_output_retention(self) -> pulumi.Output[Optional[int]]:
        """
        Field for storage output retention in days.
        """
        return pulumi.get(self, "storage_output_retention")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="visualizationUrl")
    def visualization_url(self) -> pulumi.Output[str]:
        """
        Url for data visualization.
        """
        return pulumi.get(self, "visualization_url")

