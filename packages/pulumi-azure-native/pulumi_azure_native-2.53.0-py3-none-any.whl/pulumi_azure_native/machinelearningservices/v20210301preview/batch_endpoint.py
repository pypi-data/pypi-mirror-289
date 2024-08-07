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
from ._inputs import *

__all__ = ['BatchEndpointInitArgs', 'BatchEndpoint']

@pulumi.input_type
class BatchEndpointInitArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input['BatchEndpointArgs'],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ResourceIdentityArgs']] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a BatchEndpoint resource.
        :param pulumi.Input['BatchEndpointArgs'] properties: [Required] Additional attributes of the entity.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[str] endpoint_name: Name for the Batch inference endpoint.
        :param pulumi.Input['ResourceIdentityArgs'] identity: Service identity associated with a resource.
        :param pulumi.Input[str] kind: Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if endpoint_name is not None:
            pulumi.set(__self__, "endpoint_name", endpoint_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['BatchEndpointArgs']:
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['BatchEndpointArgs']):
        pulumi.set(self, "properties", value)

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
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        Name of Azure Machine Learning workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="endpointName")
    def endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for the Batch inference endpoint.
        """
        return pulumi.get(self, "endpoint_name")

    @endpoint_name.setter
    def endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ResourceIdentityArgs']]:
        """
        Service identity associated with a resource.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ResourceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class BatchEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['ResourceIdentityArgs', 'ResourceIdentityArgsDict']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['BatchEndpointArgs', 'BatchEndpointArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a BatchEndpoint resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint_name: Name for the Batch inference endpoint.
        :param pulumi.Input[Union['ResourceIdentityArgs', 'ResourceIdentityArgsDict']] identity: Service identity associated with a resource.
        :param pulumi.Input[str] kind: Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Union['BatchEndpointArgs', 'BatchEndpointArgsDict']] properties: [Required] Additional attributes of the entity.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BatchEndpointInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a BatchEndpoint resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param BatchEndpointInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BatchEndpointInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['ResourceIdentityArgs', 'ResourceIdentityArgsDict']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[Union['BatchEndpointArgs', 'BatchEndpointArgsDict']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BatchEndpointInitArgs.__new__(BatchEndpointInitArgs)

            __props__.__dict__["endpoint_name"] = endpoint_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:machinelearningservices:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20220201preview:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20220501:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20220601preview:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221001:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221001preview:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20221201preview:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230201preview:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230401:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230401preview:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230601preview:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20230801preview:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20231001:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240101preview:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240401:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240401preview:BatchEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240701preview:BatchEndpoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(BatchEndpoint, __self__).__init__(
            'azure-native:machinelearningservices/v20210301preview:BatchEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'BatchEndpoint':
        """
        Get an existing BatchEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BatchEndpointInitArgs.__new__(BatchEndpointInitArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return BatchEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ResourceIdentityResponse']]:
        """
        Service identity associated with a resource.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.BatchEndpointResponse']:
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        System data associated with resource provider
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

