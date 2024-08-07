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

__all__ = ['IntegrationAccountSchemaArgs', 'IntegrationAccountSchema']

@pulumi.input_type
class IntegrationAccountSchemaArgs:
    def __init__(__self__, *,
                 integration_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 schema_type: pulumi.Input[Union[str, 'SchemaType']],
                 content: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 document_name: Optional[pulumi.Input[str]] = None,
                 file_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_namespace: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IntegrationAccountSchema resource.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[Union[str, 'SchemaType']] schema_type: The schema type.
        :param pulumi.Input[str] content: The content.
        :param pulumi.Input[str] content_type: The content type.
        :param pulumi.Input[str] document_name: The document name.
        :param pulumi.Input[str] file_name: The file name.
        :param pulumi.Input[str] location: The resource location.
        :param Any metadata: The metadata.
        :param pulumi.Input[str] schema_name: The integration account schema name.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        :param pulumi.Input[str] target_namespace: The target namespace of the schema.
        """
        pulumi.set(__self__, "integration_account_name", integration_account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "schema_type", schema_type)
        if content is not None:
            pulumi.set(__self__, "content", content)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if document_name is not None:
            pulumi.set(__self__, "document_name", document_name)
        if file_name is not None:
            pulumi.set(__self__, "file_name", file_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if schema_name is not None:
            pulumi.set(__self__, "schema_name", schema_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if target_namespace is not None:
            pulumi.set(__self__, "target_namespace", target_namespace)

    @property
    @pulumi.getter(name="integrationAccountName")
    def integration_account_name(self) -> pulumi.Input[str]:
        """
        The integration account name.
        """
        return pulumi.get(self, "integration_account_name")

    @integration_account_name.setter
    def integration_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "integration_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> pulumi.Input[Union[str, 'SchemaType']]:
        """
        The schema type.
        """
        return pulumi.get(self, "schema_type")

    @schema_type.setter
    def schema_type(self, value: pulumi.Input[Union[str, 'SchemaType']]):
        pulumi.set(self, "schema_type", value)

    @property
    @pulumi.getter
    def content(self) -> Optional[pulumi.Input[str]]:
        """
        The content.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        """
        The content type.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="documentName")
    def document_name(self) -> Optional[pulumi.Input[str]]:
        """
        The document name.
        """
        return pulumi.get(self, "document_name")

    @document_name.setter
    def document_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "document_name", value)

    @property
    @pulumi.getter(name="fileName")
    def file_name(self) -> Optional[pulumi.Input[str]]:
        """
        The file name.
        """
        return pulumi.get(self, "file_name")

    @file_name.setter
    def file_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "file_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Any]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[Any]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter(name="schemaName")
    def schema_name(self) -> Optional[pulumi.Input[str]]:
        """
        The integration account schema name.
        """
        return pulumi.get(self, "schema_name")

    @schema_name.setter
    def schema_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schema_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> Optional[pulumi.Input[str]]:
        """
        The target namespace of the schema.
        """
        return pulumi.get(self, "target_namespace")

    @target_namespace.setter
    def target_namespace(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_namespace", value)


class IntegrationAccountSchema(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 document_name: Optional[pulumi.Input[str]] = None,
                 file_name: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 schema_type: Optional[pulumi.Input[Union[str, 'SchemaType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The integration account schema.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content: The content.
        :param pulumi.Input[str] content_type: The content type.
        :param pulumi.Input[str] document_name: The document name.
        :param pulumi.Input[str] file_name: The file name.
        :param pulumi.Input[str] integration_account_name: The integration account name.
        :param pulumi.Input[str] location: The resource location.
        :param Any metadata: The metadata.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] schema_name: The integration account schema name.
        :param pulumi.Input[Union[str, 'SchemaType']] schema_type: The schema type.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The resource tags.
        :param pulumi.Input[str] target_namespace: The target namespace of the schema.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationAccountSchemaArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The integration account schema.

        :param str resource_name: The name of the resource.
        :param IntegrationAccountSchemaArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationAccountSchemaArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 document_name: Optional[pulumi.Input[str]] = None,
                 file_name: Optional[pulumi.Input[str]] = None,
                 integration_account_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[Any] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 schema_name: Optional[pulumi.Input[str]] = None,
                 schema_type: Optional[pulumi.Input[Union[str, 'SchemaType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_namespace: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationAccountSchemaArgs.__new__(IntegrationAccountSchemaArgs)

            __props__.__dict__["content"] = content
            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["document_name"] = document_name
            __props__.__dict__["file_name"] = file_name
            if integration_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'integration_account_name'")
            __props__.__dict__["integration_account_name"] = integration_account_name
            __props__.__dict__["location"] = location
            __props__.__dict__["metadata"] = metadata
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["schema_name"] = schema_name
            if schema_type is None and not opts.urn:
                raise TypeError("Missing required property 'schema_type'")
            __props__.__dict__["schema_type"] = schema_type
            __props__.__dict__["tags"] = tags
            __props__.__dict__["target_namespace"] = target_namespace
            __props__.__dict__["changed_time"] = None
            __props__.__dict__["content_link"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:logic:IntegrationAccountSchema"), pulumi.Alias(type_="azure-native:logic/v20150801preview:IntegrationAccountSchema"), pulumi.Alias(type_="azure-native:logic/v20160601:IntegrationAccountSchema"), pulumi.Alias(type_="azure-native:logic/v20180701preview:IntegrationAccountSchema")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IntegrationAccountSchema, __self__).__init__(
            'azure-native:logic/v20190501:IntegrationAccountSchema',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IntegrationAccountSchema':
        """
        Get an existing IntegrationAccountSchema resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IntegrationAccountSchemaArgs.__new__(IntegrationAccountSchemaArgs)

        __props__.__dict__["changed_time"] = None
        __props__.__dict__["content"] = None
        __props__.__dict__["content_link"] = None
        __props__.__dict__["content_type"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["document_name"] = None
        __props__.__dict__["file_name"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["schema_type"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_namespace"] = None
        __props__.__dict__["type"] = None
        return IntegrationAccountSchema(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> pulumi.Output[str]:
        """
        The changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter
    def content(self) -> pulumi.Output[Optional[str]]:
        """
        The content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> pulumi.Output['outputs.ContentLinkResponse']:
        """
        The content link.
        """
        return pulumi.get(self, "content_link")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[str]]:
        """
        The content type.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        The created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="documentName")
    def document_name(self) -> pulumi.Output[Optional[str]]:
        """
        The document name.
        """
        return pulumi.get(self, "document_name")

    @property
    @pulumi.getter(name="fileName")
    def file_name(self) -> pulumi.Output[Optional[str]]:
        """
        The file name.
        """
        return pulumi.get(self, "file_name")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Any]]:
        """
        The metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="schemaType")
    def schema_type(self) -> pulumi.Output[str]:
        """
        The schema type.
        """
        return pulumi.get(self, "schema_type")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetNamespace")
    def target_namespace(self) -> pulumi.Output[Optional[str]]:
        """
        The target namespace of the schema.
        """
        return pulumi.get(self, "target_namespace")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")

