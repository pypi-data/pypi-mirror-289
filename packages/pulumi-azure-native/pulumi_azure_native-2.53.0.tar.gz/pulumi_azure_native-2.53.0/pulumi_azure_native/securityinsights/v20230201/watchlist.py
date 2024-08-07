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

__all__ = ['WatchlistArgs', 'Watchlist']

@pulumi.input_type
class WatchlistArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 items_search_key: pulumi.Input[str],
                 provider: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 source: pulumi.Input[Union[str, 'Source']],
                 workspace_name: pulumi.Input[str],
                 content_type: Optional[pulumi.Input[str]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input['WatchlistUserInfoArgs']] = None,
                 default_duration: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 is_deleted: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 number_of_lines_to_skip: Optional[pulumi.Input[int]] = None,
                 raw_content: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 updated: Optional[pulumi.Input[str]] = None,
                 updated_by: Optional[pulumi.Input['WatchlistUserInfoArgs']] = None,
                 upload_status: Optional[pulumi.Input[str]] = None,
                 watchlist_alias: Optional[pulumi.Input[str]] = None,
                 watchlist_id: Optional[pulumi.Input[str]] = None,
                 watchlist_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Watchlist resource.
        :param pulumi.Input[str] display_name: The display name of the watchlist
        :param pulumi.Input[str] items_search_key: The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address.
        :param pulumi.Input[str] provider: The provider of the watchlist
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'Source']] source: The source of the watchlist
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input[str] content_type: The content type of the raw content. For now, only text/csv is valid
        :param pulumi.Input[str] created: The time the watchlist was created
        :param pulumi.Input['WatchlistUserInfoArgs'] created_by: Describes a user that created the watchlist
        :param pulumi.Input[str] default_duration: The default duration of a watchlist (in ISO 8601 duration format)
        :param pulumi.Input[str] description: A description of the watchlist
        :param pulumi.Input[bool] is_deleted: A flag that indicates if the watchlist is deleted or not
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of labels relevant to this watchlist
        :param pulumi.Input[int] number_of_lines_to_skip: The number of lines in a csv content to skip before the header
        :param pulumi.Input[str] raw_content: The raw content that represents to watchlist items to create. Example : This line will be skipped
               header1,header2
               value1,value2
        :param pulumi.Input[str] tenant_id: The tenantId where the watchlist belongs to
        :param pulumi.Input[str] updated: The last time the watchlist was updated
        :param pulumi.Input['WatchlistUserInfoArgs'] updated_by: Describes a user that updated the watchlist
        :param pulumi.Input[str] upload_status: The status of the Watchlist upload : New, InProgress or Complete. **Note** : When a Watchlist upload status is InProgress, the Watchlist cannot be deleted
        :param pulumi.Input[str] watchlist_alias: The alias of the watchlist
        :param pulumi.Input[str] watchlist_id: The id (a Guid) of the watchlist
        :param pulumi.Input[str] watchlist_type: The type of the watchlist
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "items_search_key", items_search_key)
        pulumi.set(__self__, "provider", provider)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if created is not None:
            pulumi.set(__self__, "created", created)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if default_duration is not None:
            pulumi.set(__self__, "default_duration", default_duration)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if is_deleted is not None:
            pulumi.set(__self__, "is_deleted", is_deleted)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if number_of_lines_to_skip is not None:
            pulumi.set(__self__, "number_of_lines_to_skip", number_of_lines_to_skip)
        if raw_content is not None:
            pulumi.set(__self__, "raw_content", raw_content)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)
        if updated is not None:
            pulumi.set(__self__, "updated", updated)
        if updated_by is not None:
            pulumi.set(__self__, "updated_by", updated_by)
        if upload_status is not None:
            pulumi.set(__self__, "upload_status", upload_status)
        if watchlist_alias is not None:
            pulumi.set(__self__, "watchlist_alias", watchlist_alias)
        if watchlist_id is not None:
            pulumi.set(__self__, "watchlist_id", watchlist_id)
        if watchlist_type is not None:
            pulumi.set(__self__, "watchlist_type", watchlist_type)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the watchlist
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="itemsSearchKey")
    def items_search_key(self) -> pulumi.Input[str]:
        """
        The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address.
        """
        return pulumi.get(self, "items_search_key")

    @items_search_key.setter
    def items_search_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "items_search_key", value)

    @property
    @pulumi.getter
    def provider(self) -> pulumi.Input[str]:
        """
        The provider of the watchlist
        """
        return pulumi.get(self, "provider")

    @provider.setter
    def provider(self, value: pulumi.Input[str]):
        pulumi.set(self, "provider", value)

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
    @pulumi.getter
    def source(self) -> pulumi.Input[Union[str, 'Source']]:
        """
        The source of the watchlist
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[Union[str, 'Source']]):
        pulumi.set(self, "source", value)

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
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        """
        The content type of the raw content. For now, only text/csv is valid
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter
    def created(self) -> Optional[pulumi.Input[str]]:
        """
        The time the watchlist was created
        """
        return pulumi.get(self, "created")

    @created.setter
    def created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created", value)

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[pulumi.Input['WatchlistUserInfoArgs']]:
        """
        Describes a user that created the watchlist
        """
        return pulumi.get(self, "created_by")

    @created_by.setter
    def created_by(self, value: Optional[pulumi.Input['WatchlistUserInfoArgs']]):
        pulumi.set(self, "created_by", value)

    @property
    @pulumi.getter(name="defaultDuration")
    def default_duration(self) -> Optional[pulumi.Input[str]]:
        """
        The default duration of a watchlist (in ISO 8601 duration format)
        """
        return pulumi.get(self, "default_duration")

    @default_duration.setter
    def default_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_duration", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the watchlist
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="isDeleted")
    def is_deleted(self) -> Optional[pulumi.Input[bool]]:
        """
        A flag that indicates if the watchlist is deleted or not
        """
        return pulumi.get(self, "is_deleted")

    @is_deleted.setter
    def is_deleted(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "is_deleted", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of labels relevant to this watchlist
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter(name="numberOfLinesToSkip")
    def number_of_lines_to_skip(self) -> Optional[pulumi.Input[int]]:
        """
        The number of lines in a csv content to skip before the header
        """
        return pulumi.get(self, "number_of_lines_to_skip")

    @number_of_lines_to_skip.setter
    def number_of_lines_to_skip(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "number_of_lines_to_skip", value)

    @property
    @pulumi.getter(name="rawContent")
    def raw_content(self) -> Optional[pulumi.Input[str]]:
        """
        The raw content that represents to watchlist items to create. Example : This line will be skipped
        header1,header2
        value1,value2
        """
        return pulumi.get(self, "raw_content")

    @raw_content.setter
    def raw_content(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "raw_content", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The tenantId where the watchlist belongs to
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)

    @property
    @pulumi.getter
    def updated(self) -> Optional[pulumi.Input[str]]:
        """
        The last time the watchlist was updated
        """
        return pulumi.get(self, "updated")

    @updated.setter
    def updated(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated", value)

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional[pulumi.Input['WatchlistUserInfoArgs']]:
        """
        Describes a user that updated the watchlist
        """
        return pulumi.get(self, "updated_by")

    @updated_by.setter
    def updated_by(self, value: Optional[pulumi.Input['WatchlistUserInfoArgs']]):
        pulumi.set(self, "updated_by", value)

    @property
    @pulumi.getter(name="uploadStatus")
    def upload_status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the Watchlist upload : New, InProgress or Complete. **Note** : When a Watchlist upload status is InProgress, the Watchlist cannot be deleted
        """
        return pulumi.get(self, "upload_status")

    @upload_status.setter
    def upload_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "upload_status", value)

    @property
    @pulumi.getter(name="watchlistAlias")
    def watchlist_alias(self) -> Optional[pulumi.Input[str]]:
        """
        The alias of the watchlist
        """
        return pulumi.get(self, "watchlist_alias")

    @watchlist_alias.setter
    def watchlist_alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "watchlist_alias", value)

    @property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> Optional[pulumi.Input[str]]:
        """
        The id (a Guid) of the watchlist
        """
        return pulumi.get(self, "watchlist_id")

    @watchlist_id.setter
    def watchlist_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "watchlist_id", value)

    @property
    @pulumi.getter(name="watchlistType")
    def watchlist_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the watchlist
        """
        return pulumi.get(self, "watchlist_type")

    @watchlist_type.setter
    def watchlist_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "watchlist_type", value)


class Watchlist(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[Union['WatchlistUserInfoArgs', 'WatchlistUserInfoArgsDict']]] = None,
                 default_duration: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_deleted: Optional[pulumi.Input[bool]] = None,
                 items_search_key: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 number_of_lines_to_skip: Optional[pulumi.Input[int]] = None,
                 provider: Optional[pulumi.Input[str]] = None,
                 raw_content: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union[str, 'Source']]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 updated: Optional[pulumi.Input[str]] = None,
                 updated_by: Optional[pulumi.Input[Union['WatchlistUserInfoArgs', 'WatchlistUserInfoArgsDict']]] = None,
                 upload_status: Optional[pulumi.Input[str]] = None,
                 watchlist_alias: Optional[pulumi.Input[str]] = None,
                 watchlist_id: Optional[pulumi.Input[str]] = None,
                 watchlist_type: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a Watchlist in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] content_type: The content type of the raw content. For now, only text/csv is valid
        :param pulumi.Input[str] created: The time the watchlist was created
        :param pulumi.Input[Union['WatchlistUserInfoArgs', 'WatchlistUserInfoArgsDict']] created_by: Describes a user that created the watchlist
        :param pulumi.Input[str] default_duration: The default duration of a watchlist (in ISO 8601 duration format)
        :param pulumi.Input[str] description: A description of the watchlist
        :param pulumi.Input[str] display_name: The display name of the watchlist
        :param pulumi.Input[bool] is_deleted: A flag that indicates if the watchlist is deleted or not
        :param pulumi.Input[str] items_search_key: The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] labels: List of labels relevant to this watchlist
        :param pulumi.Input[int] number_of_lines_to_skip: The number of lines in a csv content to skip before the header
        :param pulumi.Input[str] provider: The provider of the watchlist
        :param pulumi.Input[str] raw_content: The raw content that represents to watchlist items to create. Example : This line will be skipped
               header1,header2
               value1,value2
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union[str, 'Source']] source: The source of the watchlist
        :param pulumi.Input[str] tenant_id: The tenantId where the watchlist belongs to
        :param pulumi.Input[str] updated: The last time the watchlist was updated
        :param pulumi.Input[Union['WatchlistUserInfoArgs', 'WatchlistUserInfoArgsDict']] updated_by: Describes a user that updated the watchlist
        :param pulumi.Input[str] upload_status: The status of the Watchlist upload : New, InProgress or Complete. **Note** : When a Watchlist upload status is InProgress, the Watchlist cannot be deleted
        :param pulumi.Input[str] watchlist_alias: The alias of the watchlist
        :param pulumi.Input[str] watchlist_id: The id (a Guid) of the watchlist
        :param pulumi.Input[str] watchlist_type: The type of the watchlist
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WatchlistArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a Watchlist in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param WatchlistArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WatchlistArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 created: Optional[pulumi.Input[str]] = None,
                 created_by: Optional[pulumi.Input[Union['WatchlistUserInfoArgs', 'WatchlistUserInfoArgsDict']]] = None,
                 default_duration: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 is_deleted: Optional[pulumi.Input[bool]] = None,
                 items_search_key: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 number_of_lines_to_skip: Optional[pulumi.Input[int]] = None,
                 provider: Optional[pulumi.Input[str]] = None,
                 raw_content: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union[str, 'Source']]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 updated: Optional[pulumi.Input[str]] = None,
                 updated_by: Optional[pulumi.Input[Union['WatchlistUserInfoArgs', 'WatchlistUserInfoArgsDict']]] = None,
                 upload_status: Optional[pulumi.Input[str]] = None,
                 watchlist_alias: Optional[pulumi.Input[str]] = None,
                 watchlist_id: Optional[pulumi.Input[str]] = None,
                 watchlist_type: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WatchlistArgs.__new__(WatchlistArgs)

            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["created"] = created
            __props__.__dict__["created_by"] = created_by
            __props__.__dict__["default_duration"] = default_duration
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["is_deleted"] = is_deleted
            if items_search_key is None and not opts.urn:
                raise TypeError("Missing required property 'items_search_key'")
            __props__.__dict__["items_search_key"] = items_search_key
            __props__.__dict__["labels"] = labels
            __props__.__dict__["number_of_lines_to_skip"] = number_of_lines_to_skip
            if provider is None and not opts.urn:
                raise TypeError("Missing required property 'provider'")
            __props__.__dict__["provider"] = provider
            __props__.__dict__["raw_content"] = raw_content
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["updated"] = updated
            __props__.__dict__["updated_by"] = updated_by
            __props__.__dict__["upload_status"] = upload_status
            __props__.__dict__["watchlist_alias"] = watchlist_alias
            __props__.__dict__["watchlist_id"] = watchlist_id
            __props__.__dict__["watchlist_type"] = watchlist_type
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20190101preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20210301preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20210401:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20210901preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20211001:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20211001preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20220101preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20220401preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20220501preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20220601preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20220701preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20220801:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20220801preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20220901preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20221001preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20221101:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20221101preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20221201preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20230201preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20230301preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20230601preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20230901preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20231101:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20240101preview:Watchlist"), pulumi.Alias(type_="azure-native:securityinsights/v20240301:Watchlist")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Watchlist, __self__).__init__(
            'azure-native:securityinsights/v20230201:Watchlist',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Watchlist':
        """
        Get an existing Watchlist resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WatchlistArgs.__new__(WatchlistArgs)

        __props__.__dict__["content_type"] = None
        __props__.__dict__["created"] = None
        __props__.__dict__["created_by"] = None
        __props__.__dict__["default_duration"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["is_deleted"] = None
        __props__.__dict__["items_search_key"] = None
        __props__.__dict__["labels"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["number_of_lines_to_skip"] = None
        __props__.__dict__["provider"] = None
        __props__.__dict__["raw_content"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["updated"] = None
        __props__.__dict__["updated_by"] = None
        __props__.__dict__["upload_status"] = None
        __props__.__dict__["watchlist_alias"] = None
        __props__.__dict__["watchlist_id"] = None
        __props__.__dict__["watchlist_type"] = None
        return Watchlist(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[str]]:
        """
        The content type of the raw content. For now, only text/csv is valid
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[Optional[str]]:
        """
        The time the watchlist was created
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> pulumi.Output[Optional['outputs.WatchlistUserInfoResponse']]:
        """
        Describes a user that created the watchlist
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="defaultDuration")
    def default_duration(self) -> pulumi.Output[Optional[str]]:
        """
        The default duration of a watchlist (in ISO 8601 duration format)
        """
        return pulumi.get(self, "default_duration")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the watchlist
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the watchlist
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="isDeleted")
    def is_deleted(self) -> pulumi.Output[Optional[bool]]:
        """
        A flag that indicates if the watchlist is deleted or not
        """
        return pulumi.get(self, "is_deleted")

    @property
    @pulumi.getter(name="itemsSearchKey")
    def items_search_key(self) -> pulumi.Output[str]:
        """
        The search key is used to optimize query performance when using watchlists for joins with other data. For example, enable a column with IP addresses to be the designated SearchKey field, then use this field as the key field when joining to other event data by IP address.
        """
        return pulumi.get(self, "items_search_key")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of labels relevant to this watchlist
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
    @pulumi.getter(name="numberOfLinesToSkip")
    def number_of_lines_to_skip(self) -> pulumi.Output[Optional[int]]:
        """
        The number of lines in a csv content to skip before the header
        """
        return pulumi.get(self, "number_of_lines_to_skip")

    @property
    @pulumi.getter
    def provider(self) -> pulumi.Output[str]:
        """
        The provider of the watchlist
        """
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter(name="rawContent")
    def raw_content(self) -> pulumi.Output[Optional[str]]:
        """
        The raw content that represents to watchlist items to create. Example : This line will be skipped
        header1,header2
        value1,value2
        """
        return pulumi.get(self, "raw_content")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        """
        The source of the watchlist
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        The tenantId where the watchlist belongs to
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def updated(self) -> pulumi.Output[Optional[str]]:
        """
        The last time the watchlist was updated
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> pulumi.Output[Optional['outputs.WatchlistUserInfoResponse']]:
        """
        Describes a user that updated the watchlist
        """
        return pulumi.get(self, "updated_by")

    @property
    @pulumi.getter(name="uploadStatus")
    def upload_status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the Watchlist upload : New, InProgress or Complete. **Note** : When a Watchlist upload status is InProgress, the Watchlist cannot be deleted
        """
        return pulumi.get(self, "upload_status")

    @property
    @pulumi.getter(name="watchlistAlias")
    def watchlist_alias(self) -> pulumi.Output[Optional[str]]:
        """
        The alias of the watchlist
        """
        return pulumi.get(self, "watchlist_alias")

    @property
    @pulumi.getter(name="watchlistId")
    def watchlist_id(self) -> pulumi.Output[Optional[str]]:
        """
        The id (a Guid) of the watchlist
        """
        return pulumi.get(self, "watchlist_id")

    @property
    @pulumi.getter(name="watchlistType")
    def watchlist_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the watchlist
        """
        return pulumi.get(self, "watchlist_type")

