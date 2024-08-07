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

__all__ = ['LinkArgs', 'Link']

@pulumi.input_type
class LinkArgs:
    def __init__(__self__, *,
                 hub_name: pulumi.Input[str],
                 participant_property_references: pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]],
                 resource_group_name: pulumi.Input[str],
                 source_entity_type: pulumi.Input['EntityType'],
                 source_entity_type_name: pulumi.Input[str],
                 target_entity_type: pulumi.Input['EntityType'],
                 target_entity_type_name: pulumi.Input[str],
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 link_name: Optional[pulumi.Input[str]] = None,
                 mappings: Optional[pulumi.Input[Sequence[pulumi.Input['TypePropertiesMappingArgs']]]] = None,
                 operation_type: Optional[pulumi.Input['InstanceOperationType']] = None,
                 reference_only: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Link resource.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]] participant_property_references: The properties that represent the participating profile.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['EntityType'] source_entity_type: Type of source entity.
        :param pulumi.Input[str] source_entity_type_name: Name of the source Entity Type.
        :param pulumi.Input['EntityType'] target_entity_type: Type of target entity.
        :param pulumi.Input[str] target_entity_type_name: Name of the target Entity Type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Localized descriptions for the Link.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Localized display name for the Link.
        :param pulumi.Input[str] link_name: The name of the link.
        :param pulumi.Input[Sequence[pulumi.Input['TypePropertiesMappingArgs']]] mappings: The set of properties mappings between the source and target Types.
        :param pulumi.Input['InstanceOperationType'] operation_type: Determines whether this link is supposed to create or delete instances if Link is NOT Reference Only.
        :param pulumi.Input[bool] reference_only: Indicating whether the link is reference only link. This flag is ignored if the Mappings are defined. If the mappings are not defined and it is set to true, links processing will not create or update profiles.
        """
        pulumi.set(__self__, "hub_name", hub_name)
        pulumi.set(__self__, "participant_property_references", participant_property_references)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source_entity_type", source_entity_type)
        pulumi.set(__self__, "source_entity_type_name", source_entity_type_name)
        pulumi.set(__self__, "target_entity_type", target_entity_type)
        pulumi.set(__self__, "target_entity_type_name", target_entity_type_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if link_name is not None:
            pulumi.set(__self__, "link_name", link_name)
        if mappings is not None:
            pulumi.set(__self__, "mappings", mappings)
        if operation_type is not None:
            pulumi.set(__self__, "operation_type", operation_type)
        if reference_only is not None:
            pulumi.set(__self__, "reference_only", reference_only)

    @property
    @pulumi.getter(name="hubName")
    def hub_name(self) -> pulumi.Input[str]:
        """
        The name of the hub.
        """
        return pulumi.get(self, "hub_name")

    @hub_name.setter
    def hub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "hub_name", value)

    @property
    @pulumi.getter(name="participantPropertyReferences")
    def participant_property_references(self) -> pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]]:
        """
        The properties that represent the participating profile.
        """
        return pulumi.get(self, "participant_property_references")

    @participant_property_references.setter
    def participant_property_references(self, value: pulumi.Input[Sequence[pulumi.Input['ParticipantPropertyReferenceArgs']]]):
        pulumi.set(self, "participant_property_references", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="sourceEntityType")
    def source_entity_type(self) -> pulumi.Input['EntityType']:
        """
        Type of source entity.
        """
        return pulumi.get(self, "source_entity_type")

    @source_entity_type.setter
    def source_entity_type(self, value: pulumi.Input['EntityType']):
        pulumi.set(self, "source_entity_type", value)

    @property
    @pulumi.getter(name="sourceEntityTypeName")
    def source_entity_type_name(self) -> pulumi.Input[str]:
        """
        Name of the source Entity Type.
        """
        return pulumi.get(self, "source_entity_type_name")

    @source_entity_type_name.setter
    def source_entity_type_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "source_entity_type_name", value)

    @property
    @pulumi.getter(name="targetEntityType")
    def target_entity_type(self) -> pulumi.Input['EntityType']:
        """
        Type of target entity.
        """
        return pulumi.get(self, "target_entity_type")

    @target_entity_type.setter
    def target_entity_type(self, value: pulumi.Input['EntityType']):
        pulumi.set(self, "target_entity_type", value)

    @property
    @pulumi.getter(name="targetEntityTypeName")
    def target_entity_type_name(self) -> pulumi.Input[str]:
        """
        Name of the target Entity Type.
        """
        return pulumi.get(self, "target_entity_type_name")

    @target_entity_type_name.setter
    def target_entity_type_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_entity_type_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Localized descriptions for the Link.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Localized display name for the Link.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="linkName")
    def link_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the link.
        """
        return pulumi.get(self, "link_name")

    @link_name.setter
    def link_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "link_name", value)

    @property
    @pulumi.getter
    def mappings(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TypePropertiesMappingArgs']]]]:
        """
        The set of properties mappings between the source and target Types.
        """
        return pulumi.get(self, "mappings")

    @mappings.setter
    def mappings(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TypePropertiesMappingArgs']]]]):
        pulumi.set(self, "mappings", value)

    @property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> Optional[pulumi.Input['InstanceOperationType']]:
        """
        Determines whether this link is supposed to create or delete instances if Link is NOT Reference Only.
        """
        return pulumi.get(self, "operation_type")

    @operation_type.setter
    def operation_type(self, value: Optional[pulumi.Input['InstanceOperationType']]):
        pulumi.set(self, "operation_type", value)

    @property
    @pulumi.getter(name="referenceOnly")
    def reference_only(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicating whether the link is reference only link. This flag is ignored if the Mappings are defined. If the mappings are not defined and it is set to true, links processing will not create or update profiles.
        """
        return pulumi.get(self, "reference_only")

    @reference_only.setter
    def reference_only(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "reference_only", value)


class Link(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 link_name: Optional[pulumi.Input[str]] = None,
                 mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TypePropertiesMappingArgs', 'TypePropertiesMappingArgsDict']]]]] = None,
                 operation_type: Optional[pulumi.Input['InstanceOperationType']] = None,
                 participant_property_references: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ParticipantPropertyReferenceArgs', 'ParticipantPropertyReferenceArgsDict']]]]] = None,
                 reference_only: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_entity_type: Optional[pulumi.Input['EntityType']] = None,
                 source_entity_type_name: Optional[pulumi.Input[str]] = None,
                 target_entity_type: Optional[pulumi.Input['EntityType']] = None,
                 target_entity_type_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The link resource format.
        Azure REST API version: 2017-04-26. Prior API version in Azure Native 1.x: 2017-04-26.

        Other available API versions: 2017-01-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] description: Localized descriptions for the Link.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] display_name: Localized display name for the Link.
        :param pulumi.Input[str] hub_name: The name of the hub.
        :param pulumi.Input[str] link_name: The name of the link.
        :param pulumi.Input[Sequence[pulumi.Input[Union['TypePropertiesMappingArgs', 'TypePropertiesMappingArgsDict']]]] mappings: The set of properties mappings between the source and target Types.
        :param pulumi.Input['InstanceOperationType'] operation_type: Determines whether this link is supposed to create or delete instances if Link is NOT Reference Only.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ParticipantPropertyReferenceArgs', 'ParticipantPropertyReferenceArgsDict']]]] participant_property_references: The properties that represent the participating profile.
        :param pulumi.Input[bool] reference_only: Indicating whether the link is reference only link. This flag is ignored if the Mappings are defined. If the mappings are not defined and it is set to true, links processing will not create or update profiles.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['EntityType'] source_entity_type: Type of source entity.
        :param pulumi.Input[str] source_entity_type_name: Name of the source Entity Type.
        :param pulumi.Input['EntityType'] target_entity_type: Type of target entity.
        :param pulumi.Input[str] target_entity_type_name: Name of the target Entity Type.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LinkArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The link resource format.
        Azure REST API version: 2017-04-26. Prior API version in Azure Native 1.x: 2017-04-26.

        Other available API versions: 2017-01-01.

        :param str resource_name: The name of the resource.
        :param LinkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LinkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 display_name: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 hub_name: Optional[pulumi.Input[str]] = None,
                 link_name: Optional[pulumi.Input[str]] = None,
                 mappings: Optional[pulumi.Input[Sequence[pulumi.Input[Union['TypePropertiesMappingArgs', 'TypePropertiesMappingArgsDict']]]]] = None,
                 operation_type: Optional[pulumi.Input['InstanceOperationType']] = None,
                 participant_property_references: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ParticipantPropertyReferenceArgs', 'ParticipantPropertyReferenceArgsDict']]]]] = None,
                 reference_only: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source_entity_type: Optional[pulumi.Input['EntityType']] = None,
                 source_entity_type_name: Optional[pulumi.Input[str]] = None,
                 target_entity_type: Optional[pulumi.Input['EntityType']] = None,
                 target_entity_type_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LinkArgs.__new__(LinkArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'hub_name'")
            __props__.__dict__["hub_name"] = hub_name
            __props__.__dict__["link_name"] = link_name
            __props__.__dict__["mappings"] = mappings
            __props__.__dict__["operation_type"] = operation_type
            if participant_property_references is None and not opts.urn:
                raise TypeError("Missing required property 'participant_property_references'")
            __props__.__dict__["participant_property_references"] = participant_property_references
            __props__.__dict__["reference_only"] = reference_only
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source_entity_type is None and not opts.urn:
                raise TypeError("Missing required property 'source_entity_type'")
            __props__.__dict__["source_entity_type"] = source_entity_type
            if source_entity_type_name is None and not opts.urn:
                raise TypeError("Missing required property 'source_entity_type_name'")
            __props__.__dict__["source_entity_type_name"] = source_entity_type_name
            if target_entity_type is None and not opts.urn:
                raise TypeError("Missing required property 'target_entity_type'")
            __props__.__dict__["target_entity_type"] = target_entity_type
            if target_entity_type_name is None and not opts.urn:
                raise TypeError("Missing required property 'target_entity_type_name'")
            __props__.__dict__["target_entity_type_name"] = target_entity_type_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:customerinsights/v20170101:Link"), pulumi.Alias(type_="azure-native:customerinsights/v20170426:Link")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Link, __self__).__init__(
            'azure-native:customerinsights:Link',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Link':
        """
        Get an existing Link resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LinkArgs.__new__(LinkArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["link_name"] = None
        __props__.__dict__["mappings"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operation_type"] = None
        __props__.__dict__["participant_property_references"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["reference_only"] = None
        __props__.__dict__["source_entity_type"] = None
        __props__.__dict__["source_entity_type_name"] = None
        __props__.__dict__["target_entity_type"] = None
        __props__.__dict__["target_entity_type_name"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return Link(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Localized descriptions for the Link.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Localized display name for the Link.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="linkName")
    def link_name(self) -> pulumi.Output[str]:
        """
        The link name.
        """
        return pulumi.get(self, "link_name")

    @property
    @pulumi.getter
    def mappings(self) -> pulumi.Output[Optional[Sequence['outputs.TypePropertiesMappingResponse']]]:
        """
        The set of properties mappings between the source and target Types.
        """
        return pulumi.get(self, "mappings")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationType")
    def operation_type(self) -> pulumi.Output[Optional[str]]:
        """
        Determines whether this link is supposed to create or delete instances if Link is NOT Reference Only.
        """
        return pulumi.get(self, "operation_type")

    @property
    @pulumi.getter(name="participantPropertyReferences")
    def participant_property_references(self) -> pulumi.Output[Sequence['outputs.ParticipantPropertyReferenceResponse']]:
        """
        The properties that represent the participating profile.
        """
        return pulumi.get(self, "participant_property_references")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="referenceOnly")
    def reference_only(self) -> pulumi.Output[Optional[bool]]:
        """
        Indicating whether the link is reference only link. This flag is ignored if the Mappings are defined. If the mappings are not defined and it is set to true, links processing will not create or update profiles.
        """
        return pulumi.get(self, "reference_only")

    @property
    @pulumi.getter(name="sourceEntityType")
    def source_entity_type(self) -> pulumi.Output[str]:
        """
        Type of source entity.
        """
        return pulumi.get(self, "source_entity_type")

    @property
    @pulumi.getter(name="sourceEntityTypeName")
    def source_entity_type_name(self) -> pulumi.Output[str]:
        """
        Name of the source Entity Type.
        """
        return pulumi.get(self, "source_entity_type_name")

    @property
    @pulumi.getter(name="targetEntityType")
    def target_entity_type(self) -> pulumi.Output[str]:
        """
        Type of target entity.
        """
        return pulumi.get(self, "target_entity_type")

    @property
    @pulumi.getter(name="targetEntityTypeName")
    def target_entity_type_name(self) -> pulumi.Output[str]:
        """
        Name of the target Entity Type.
        """
        return pulumi.get(self, "target_entity_type_name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

