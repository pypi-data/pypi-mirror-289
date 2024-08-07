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

__all__ = ['HuntRelationArgs', 'HuntRelation']

@pulumi.input_type
class HuntRelationArgs:
    def __init__(__self__, *,
                 hunt_id: pulumi.Input[str],
                 related_resource_id: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 hunt_relation_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a HuntRelation resource.
        :param pulumi.Input[str] hunt_id: The hunt id (GUID)
        :param pulumi.Input[str] related_resource_id: The id of the related resource
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] hunt_relation_id: The hunt relation id (GUID)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of labels relevant to this hunt
        """
        pulumi.set(__self__, "hunt_id", hunt_id)
        pulumi.set(__self__, "related_resource_id", related_resource_id)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if hunt_relation_id is not None:
            pulumi.set(__self__, "hunt_relation_id", hunt_relation_id)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)

    @property
    @pulumi.getter(name="huntId")
    def hunt_id(self) -> pulumi.Input[str]:
        """
        The hunt id (GUID)
        """
        return pulumi.get(self, "hunt_id")

    @hunt_id.setter
    def hunt_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hunt_id", value)

    @property
    @pulumi.getter(name="relatedResourceId")
    def related_resource_id(self) -> pulumi.Input[str]:
        """
        The id of the related resource
        """
        return pulumi.get(self, "related_resource_id")

    @related_resource_id.setter
    def related_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "related_resource_id", value)

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
        The name of the workspace.
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter(name="huntRelationId")
    def hunt_relation_id(self) -> Optional[pulumi.Input[str]]:
        """
        The hunt relation id (GUID)
        """
        return pulumi.get(self, "hunt_relation_id")

    @hunt_relation_id.setter
    def hunt_relation_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hunt_relation_id", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of labels relevant to this hunt
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)


class HuntRelation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hunt_id: Optional[pulumi.Input[str]] = None,
                 hunt_relation_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 related_resource_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a Hunt Relation in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hunt_id: The hunt id (GUID)
        :param pulumi.Input[str] hunt_relation_id: The hunt relation id (GUID)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of labels relevant to this hunt
        :param pulumi.Input[str] related_resource_id: The id of the related resource
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HuntRelationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a Hunt Relation in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param HuntRelationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HuntRelationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hunt_id: Optional[pulumi.Input[str]] = None,
                 hunt_relation_id: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 related_resource_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HuntRelationArgs.__new__(HuntRelationArgs)

            if hunt_id is None and not opts.urn:
                raise TypeError("Missing required property 'hunt_id'")
            __props__.__dict__["hunt_id"] = hunt_id
            __props__.__dict__["hunt_relation_id"] = hunt_relation_id
            __props__.__dict__["labels"] = labels
            if related_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'related_resource_id'")
            __props__.__dict__["related_resource_id"] = related_resource_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["related_resource_kind"] = None
            __props__.__dict__["related_resource_name"] = None
            __props__.__dict__["relation_type"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:HuntRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:HuntRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:HuntRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20230601preview:HuntRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:HuntRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:HuntRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20230901preview:HuntRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:HuntRelation"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:HuntRelation")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(HuntRelation, __self__).__init__(
            'azure-native:securityinsights/v20240101preview:HuntRelation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HuntRelation':
        """
        Get an existing HuntRelation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HuntRelationArgs.__new__(HuntRelationArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["related_resource_id"] = None
        __props__.__dict__["related_resource_kind"] = None
        __props__.__dict__["related_resource_name"] = None
        __props__.__dict__["relation_type"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return HuntRelation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of labels relevant to this hunt
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="relatedResourceId")
    def related_resource_id(self) -> pulumi.Output[str]:
        """
        The id of the related resource
        """
        return pulumi.get(self, "related_resource_id")

    @property
    @pulumi.getter(name="relatedResourceKind")
    def related_resource_kind(self) -> pulumi.Output[str]:
        """
        The resource that the relation is related to
        """
        return pulumi.get(self, "related_resource_kind")

    @property
    @pulumi.getter(name="relatedResourceName")
    def related_resource_name(self) -> pulumi.Output[str]:
        """
        The name of the related resource
        """
        return pulumi.get(self, "related_resource_name")

    @property
    @pulumi.getter(name="relationType")
    def relation_type(self) -> pulumi.Output[str]:
        """
        The type of the hunt relation
        """
        return pulumi.get(self, "relation_type")

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

