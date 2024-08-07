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
from ._inputs import *

__all__ = ['InferenceEndpointInitArgs', 'InferenceEndpoint']

@pulumi.input_type
class InferenceEndpointInitArgs:
    def __init__(__self__, *,
                 inference_endpoint_properties: pulumi.Input['InferenceEndpointArgs'],
                 pool_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a InferenceEndpoint resource.
        :param pulumi.Input['InferenceEndpointArgs'] inference_endpoint_properties: [Required] Additional attributes of the entity.
        :param pulumi.Input[str] pool_name: InferencePool name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        :param pulumi.Input[str] endpoint_name: InferenceEndpoint name.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: Managed service identity (system assigned and/or user assigned identities)
        :param pulumi.Input[str] kind: Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['SkuArgs'] sku: Sku details required for ARM contract for Autoscaling.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "inference_endpoint_properties", inference_endpoint_properties)
        pulumi.set(__self__, "pool_name", pool_name)
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
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="inferenceEndpointProperties")
    def inference_endpoint_properties(self) -> pulumi.Input['InferenceEndpointArgs']:
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "inference_endpoint_properties")

    @inference_endpoint_properties.setter
    def inference_endpoint_properties(self, value: pulumi.Input['InferenceEndpointArgs']):
        pulumi.set(self, "inference_endpoint_properties", value)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Input[str]:
        """
        InferencePool name.
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool_name", value)

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
        InferenceEndpoint name.
        """
        return pulumi.get(self, "endpoint_name")

    @endpoint_name.setter
    def endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        Managed service identity (system assigned and/or user assigned identities)
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
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
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        Sku details required for ARM contract for Autoscaling.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

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


class InferenceEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 inference_endpoint_properties: Optional[pulumi.Input[Union['InferenceEndpointArgs', 'InferenceEndpointArgsDict']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['SkuArgs', 'SkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Azure REST API version: 2023-08-01-preview.

        Other available API versions: 2024-01-01-preview, 2024-04-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] endpoint_name: InferenceEndpoint name.
        :param pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']] identity: Managed service identity (system assigned and/or user assigned identities)
        :param pulumi.Input[Union['InferenceEndpointArgs', 'InferenceEndpointArgsDict']] inference_endpoint_properties: [Required] Additional attributes of the entity.
        :param pulumi.Input[str] kind: Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] pool_name: InferencePool name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['SkuArgs', 'SkuArgsDict']] sku: Sku details required for ARM contract for Autoscaling.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_name: Name of Azure Machine Learning workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InferenceEndpointInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure REST API version: 2023-08-01-preview.

        Other available API versions: 2024-01-01-preview, 2024-04-01-preview.

        :param str resource_name: The name of the resource.
        :param InferenceEndpointInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InferenceEndpointInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[Union['ManagedServiceIdentityArgs', 'ManagedServiceIdentityArgsDict']]] = None,
                 inference_endpoint_properties: Optional[pulumi.Input[Union['InferenceEndpointArgs', 'InferenceEndpointArgsDict']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[Union['SkuArgs', 'SkuArgsDict']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InferenceEndpointInitArgs.__new__(InferenceEndpointInitArgs)

            __props__.__dict__["endpoint_name"] = endpoint_name
            __props__.__dict__["identity"] = identity
            if inference_endpoint_properties is None and not opts.urn:
                raise TypeError("Missing required property 'inference_endpoint_properties'")
            __props__.__dict__["inference_endpoint_properties"] = inference_endpoint_properties
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'pool_name'")
            __props__.__dict__["pool_name"] = pool_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:machinelearningservices/v20230801preview:InferenceEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240101preview:InferenceEndpoint"), pulumi.Alias(type_="azure-native:machinelearningservices/v20240401preview:InferenceEndpoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(InferenceEndpoint, __self__).__init__(
            'azure-native:machinelearningservices:InferenceEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InferenceEndpoint':
        """
        Get an existing InferenceEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InferenceEndpointInitArgs.__new__(InferenceEndpointInitArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["inference_endpoint_properties"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return InferenceEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        Managed service identity (system assigned and/or user assigned identities)
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="inferenceEndpointProperties")
    def inference_endpoint_properties(self) -> pulumi.Output['outputs.InferenceEndpointResponse']:
        """
        [Required] Additional attributes of the entity.
        """
        return pulumi.get(self, "inference_endpoint_properties")

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
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        Sku details required for ARM contract for Autoscaling.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
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

