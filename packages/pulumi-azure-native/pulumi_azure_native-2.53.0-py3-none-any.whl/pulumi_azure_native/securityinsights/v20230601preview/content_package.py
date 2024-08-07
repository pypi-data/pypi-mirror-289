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

__all__ = ['ContentPackageArgs', 'ContentPackage']

@pulumi.input_type
class ContentPackageArgs:
    def __init__(__self__, *,
                 content_id: pulumi.Input[str],
                 content_kind: pulumi.Input[Union[str, 'PackageKind']],
                 display_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 version: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 author: Optional[pulumi.Input['MetadataAuthorArgs']] = None,
                 categories: Optional[pulumi.Input['MetadataCategoriesArgs']] = None,
                 content_schema_version: Optional[pulumi.Input[str]] = None,
                 dependencies: Optional[pulumi.Input['MetadataDependenciesArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 first_publish_date: Optional[pulumi.Input[str]] = None,
                 icon: Optional[pulumi.Input[str]] = None,
                 is_featured: Optional[pulumi.Input[Union[str, 'Flag']]] = None,
                 is_new: Optional[pulumi.Input[Union[str, 'Flag']]] = None,
                 is_preview: Optional[pulumi.Input[Union[str, 'Flag']]] = None,
                 last_publish_date: Optional[pulumi.Input[str]] = None,
                 package_id: Optional[pulumi.Input[str]] = None,
                 providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 publisher_display_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input['MetadataSourceArgs']] = None,
                 support: Optional[pulumi.Input['MetadataSupportArgs']] = None,
                 threat_analysis_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 threat_analysis_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ContentPackage resource.
        :param pulumi.Input[str] content_id: The package id
        :param pulumi.Input[Union[str, 'PackageKind']] content_kind: The package kind
        :param pulumi.Input[str] display_name: The display name of the package
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] version: the latest version number of the package
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        :param pulumi.Input['MetadataAuthorArgs'] author: The author of the package
        :param pulumi.Input['MetadataCategoriesArgs'] categories: The categories of the package
        :param pulumi.Input[str] content_schema_version: The version of the content schema.
        :param pulumi.Input['MetadataDependenciesArgs'] dependencies: The support tier of the package
        :param pulumi.Input[str] description: The description of the package
        :param pulumi.Input[str] first_publish_date: first publish date package item
        :param pulumi.Input[str] icon: the icon identifier. this id can later be fetched from the content metadata
        :param pulumi.Input[Union[str, 'Flag']] is_featured: Flag indicates if this package is among the featured list.
        :param pulumi.Input[Union[str, 'Flag']] is_new: Flag indicates if this is a newly published package.
        :param pulumi.Input[Union[str, 'Flag']] is_preview: Flag indicates if this package is in preview.
        :param pulumi.Input[str] last_publish_date: last publish date for the package item
        :param pulumi.Input[str] package_id: package Id
        :param pulumi.Input[Sequence[pulumi.Input[str]]] providers: Providers for the package item
        :param pulumi.Input[str] publisher_display_name: The publisher display name of the package
        :param pulumi.Input['MetadataSourceArgs'] source: The source of the package
        :param pulumi.Input['MetadataSupportArgs'] support: The support tier of the package
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_analysis_tactics: the tactics the resource covers
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_analysis_techniques: the techniques the resource covers, these have to be aligned with the tactics being used
        """
        pulumi.set(__self__, "content_id", content_id)
        pulumi.set(__self__, "content_kind", content_kind)
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "version", version)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if author is not None:
            pulumi.set(__self__, "author", author)
        if categories is not None:
            pulumi.set(__self__, "categories", categories)
        if content_schema_version is not None:
            pulumi.set(__self__, "content_schema_version", content_schema_version)
        if dependencies is not None:
            pulumi.set(__self__, "dependencies", dependencies)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if first_publish_date is not None:
            pulumi.set(__self__, "first_publish_date", first_publish_date)
        if icon is not None:
            pulumi.set(__self__, "icon", icon)
        if is_featured is not None:
            pulumi.set(__self__, "is_featured", is_featured)
        if is_new is not None:
            pulumi.set(__self__, "is_new", is_new)
        if is_preview is not None:
            pulumi.set(__self__, "is_preview", is_preview)
        if last_publish_date is not None:
            pulumi.set(__self__, "last_publish_date", last_publish_date)
        if package_id is not None:
            pulumi.set(__self__, "package_id", package_id)
        if providers is not None:
            pulumi.set(__self__, "providers", providers)
        if publisher_display_name is not None:
            pulumi.set(__self__, "publisher_display_name", publisher_display_name)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if support is not None:
            pulumi.set(__self__, "support", support)
        if threat_analysis_tactics is not None:
            pulumi.set(__self__, "threat_analysis_tactics", threat_analysis_tactics)
        if threat_analysis_techniques is not None:
            pulumi.set(__self__, "threat_analysis_techniques", threat_analysis_techniques)

    @property
    @pulumi.getter(name="contentId")
    def content_id(self) -> pulumi.Input[str]:
        """
        The package id
        """
        return pulumi.get(self, "content_id")

    @content_id.setter
    def content_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "content_id", value)

    @property
    @pulumi.getter(name="contentKind")
    def content_kind(self) -> pulumi.Input[Union[str, 'PackageKind']]:
        """
        The package kind
        """
        return pulumi.get(self, "content_kind")

    @content_kind.setter
    def content_kind(self, value: pulumi.Input[Union[str, 'PackageKind']]):
        pulumi.set(self, "content_kind", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The display name of the package
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

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
    def version(self) -> pulumi.Input[str]:
        """
        the latest version number of the package
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

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
    @pulumi.getter
    def author(self) -> Optional[pulumi.Input['MetadataAuthorArgs']]:
        """
        The author of the package
        """
        return pulumi.get(self, "author")

    @author.setter
    def author(self, value: Optional[pulumi.Input['MetadataAuthorArgs']]):
        pulumi.set(self, "author", value)

    @property
    @pulumi.getter
    def categories(self) -> Optional[pulumi.Input['MetadataCategoriesArgs']]:
        """
        The categories of the package
        """
        return pulumi.get(self, "categories")

    @categories.setter
    def categories(self, value: Optional[pulumi.Input['MetadataCategoriesArgs']]):
        pulumi.set(self, "categories", value)

    @property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of the content schema.
        """
        return pulumi.get(self, "content_schema_version")

    @content_schema_version.setter
    def content_schema_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_schema_version", value)

    @property
    @pulumi.getter
    def dependencies(self) -> Optional[pulumi.Input['MetadataDependenciesArgs']]:
        """
        The support tier of the package
        """
        return pulumi.get(self, "dependencies")

    @dependencies.setter
    def dependencies(self, value: Optional[pulumi.Input['MetadataDependenciesArgs']]):
        pulumi.set(self, "dependencies", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the package
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> Optional[pulumi.Input[str]]:
        """
        first publish date package item
        """
        return pulumi.get(self, "first_publish_date")

    @first_publish_date.setter
    def first_publish_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_publish_date", value)

    @property
    @pulumi.getter
    def icon(self) -> Optional[pulumi.Input[str]]:
        """
        the icon identifier. this id can later be fetched from the content metadata
        """
        return pulumi.get(self, "icon")

    @icon.setter
    def icon(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "icon", value)

    @property
    @pulumi.getter(name="isFeatured")
    def is_featured(self) -> Optional[pulumi.Input[Union[str, 'Flag']]]:
        """
        Flag indicates if this package is among the featured list.
        """
        return pulumi.get(self, "is_featured")

    @is_featured.setter
    def is_featured(self, value: Optional[pulumi.Input[Union[str, 'Flag']]]):
        pulumi.set(self, "is_featured", value)

    @property
    @pulumi.getter(name="isNew")
    def is_new(self) -> Optional[pulumi.Input[Union[str, 'Flag']]]:
        """
        Flag indicates if this is a newly published package.
        """
        return pulumi.get(self, "is_new")

    @is_new.setter
    def is_new(self, value: Optional[pulumi.Input[Union[str, 'Flag']]]):
        pulumi.set(self, "is_new", value)

    @property
    @pulumi.getter(name="isPreview")
    def is_preview(self) -> Optional[pulumi.Input[Union[str, 'Flag']]]:
        """
        Flag indicates if this package is in preview.
        """
        return pulumi.get(self, "is_preview")

    @is_preview.setter
    def is_preview(self, value: Optional[pulumi.Input[Union[str, 'Flag']]]):
        pulumi.set(self, "is_preview", value)

    @property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> Optional[pulumi.Input[str]]:
        """
        last publish date for the package item
        """
        return pulumi.get(self, "last_publish_date")

    @last_publish_date.setter
    def last_publish_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_publish_date", value)

    @property
    @pulumi.getter(name="packageId")
    def package_id(self) -> Optional[pulumi.Input[str]]:
        """
        package Id
        """
        return pulumi.get(self, "package_id")

    @package_id.setter
    def package_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "package_id", value)

    @property
    @pulumi.getter
    def providers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Providers for the package item
        """
        return pulumi.get(self, "providers")

    @providers.setter
    def providers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "providers", value)

    @property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The publisher display name of the package
        """
        return pulumi.get(self, "publisher_display_name")

    @publisher_display_name.setter
    def publisher_display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "publisher_display_name", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input['MetadataSourceArgs']]:
        """
        The source of the package
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input['MetadataSourceArgs']]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def support(self) -> Optional[pulumi.Input['MetadataSupportArgs']]:
        """
        The support tier of the package
        """
        return pulumi.get(self, "support")

    @support.setter
    def support(self, value: Optional[pulumi.Input['MetadataSupportArgs']]):
        pulumi.set(self, "support", value)

    @property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        the tactics the resource covers
        """
        return pulumi.get(self, "threat_analysis_tactics")

    @threat_analysis_tactics.setter
    def threat_analysis_tactics(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "threat_analysis_tactics", value)

    @property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        the techniques the resource covers, these have to be aligned with the tactics being used
        """
        return pulumi.get(self, "threat_analysis_techniques")

    @threat_analysis_techniques.setter
    def threat_analysis_techniques(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "threat_analysis_techniques", value)


class ContentPackage(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 author: Optional[pulumi.Input[Union['MetadataAuthorArgs', 'MetadataAuthorArgsDict']]] = None,
                 categories: Optional[pulumi.Input[Union['MetadataCategoriesArgs', 'MetadataCategoriesArgsDict']]] = None,
                 content_id: Optional[pulumi.Input[str]] = None,
                 content_kind: Optional[pulumi.Input[Union[str, 'PackageKind']]] = None,
                 content_schema_version: Optional[pulumi.Input[str]] = None,
                 dependencies: Optional[pulumi.Input[Union['MetadataDependenciesArgs', 'MetadataDependenciesArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 first_publish_date: Optional[pulumi.Input[str]] = None,
                 icon: Optional[pulumi.Input[str]] = None,
                 is_featured: Optional[pulumi.Input[Union[str, 'Flag']]] = None,
                 is_new: Optional[pulumi.Input[Union[str, 'Flag']]] = None,
                 is_preview: Optional[pulumi.Input[Union[str, 'Flag']]] = None,
                 last_publish_date: Optional[pulumi.Input[str]] = None,
                 package_id: Optional[pulumi.Input[str]] = None,
                 providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 publisher_display_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union['MetadataSourceArgs', 'MetadataSourceArgsDict']]] = None,
                 support: Optional[pulumi.Input[Union['MetadataSupportArgs', 'MetadataSupportArgsDict']]] = None,
                 threat_analysis_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 threat_analysis_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a Package in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union['MetadataAuthorArgs', 'MetadataAuthorArgsDict']] author: The author of the package
        :param pulumi.Input[Union['MetadataCategoriesArgs', 'MetadataCategoriesArgsDict']] categories: The categories of the package
        :param pulumi.Input[str] content_id: The package id
        :param pulumi.Input[Union[str, 'PackageKind']] content_kind: The package kind
        :param pulumi.Input[str] content_schema_version: The version of the content schema.
        :param pulumi.Input[Union['MetadataDependenciesArgs', 'MetadataDependenciesArgsDict']] dependencies: The support tier of the package
        :param pulumi.Input[str] description: The description of the package
        :param pulumi.Input[str] display_name: The display name of the package
        :param pulumi.Input[str] first_publish_date: first publish date package item
        :param pulumi.Input[str] icon: the icon identifier. this id can later be fetched from the content metadata
        :param pulumi.Input[Union[str, 'Flag']] is_featured: Flag indicates if this package is among the featured list.
        :param pulumi.Input[Union[str, 'Flag']] is_new: Flag indicates if this is a newly published package.
        :param pulumi.Input[Union[str, 'Flag']] is_preview: Flag indicates if this package is in preview.
        :param pulumi.Input[str] last_publish_date: last publish date for the package item
        :param pulumi.Input[str] package_id: package Id
        :param pulumi.Input[Sequence[pulumi.Input[str]]] providers: Providers for the package item
        :param pulumi.Input[str] publisher_display_name: The publisher display name of the package
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Union['MetadataSourceArgs', 'MetadataSourceArgsDict']] source: The source of the package
        :param pulumi.Input[Union['MetadataSupportArgs', 'MetadataSupportArgsDict']] support: The support tier of the package
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_analysis_tactics: the tactics the resource covers
        :param pulumi.Input[Sequence[pulumi.Input[str]]] threat_analysis_techniques: the techniques the resource covers, these have to be aligned with the tactics being used
        :param pulumi.Input[str] version: the latest version number of the package
        :param pulumi.Input[str] workspace_name: The name of the workspace.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContentPackageArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a Package in Azure Security Insights.

        :param str resource_name: The name of the resource.
        :param ContentPackageArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContentPackageArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 author: Optional[pulumi.Input[Union['MetadataAuthorArgs', 'MetadataAuthorArgsDict']]] = None,
                 categories: Optional[pulumi.Input[Union['MetadataCategoriesArgs', 'MetadataCategoriesArgsDict']]] = None,
                 content_id: Optional[pulumi.Input[str]] = None,
                 content_kind: Optional[pulumi.Input[Union[str, 'PackageKind']]] = None,
                 content_schema_version: Optional[pulumi.Input[str]] = None,
                 dependencies: Optional[pulumi.Input[Union['MetadataDependenciesArgs', 'MetadataDependenciesArgsDict']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 first_publish_date: Optional[pulumi.Input[str]] = None,
                 icon: Optional[pulumi.Input[str]] = None,
                 is_featured: Optional[pulumi.Input[Union[str, 'Flag']]] = None,
                 is_new: Optional[pulumi.Input[Union[str, 'Flag']]] = None,
                 is_preview: Optional[pulumi.Input[Union[str, 'Flag']]] = None,
                 last_publish_date: Optional[pulumi.Input[str]] = None,
                 package_id: Optional[pulumi.Input[str]] = None,
                 providers: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 publisher_display_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union['MetadataSourceArgs', 'MetadataSourceArgsDict']]] = None,
                 support: Optional[pulumi.Input[Union['MetadataSupportArgs', 'MetadataSupportArgsDict']]] = None,
                 threat_analysis_tactics: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 threat_analysis_techniques: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 version: Optional[pulumi.Input[str]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContentPackageArgs.__new__(ContentPackageArgs)

            __props__.__dict__["author"] = author
            __props__.__dict__["categories"] = categories
            if content_id is None and not opts.urn:
                raise TypeError("Missing required property 'content_id'")
            __props__.__dict__["content_id"] = content_id
            if content_kind is None and not opts.urn:
                raise TypeError("Missing required property 'content_kind'")
            __props__.__dict__["content_kind"] = content_kind
            __props__.__dict__["content_schema_version"] = content_schema_version
            __props__.__dict__["dependencies"] = dependencies
            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["first_publish_date"] = first_publish_date
            __props__.__dict__["icon"] = icon
            __props__.__dict__["is_featured"] = is_featured
            __props__.__dict__["is_new"] = is_new
            __props__.__dict__["is_preview"] = is_preview
            __props__.__dict__["last_publish_date"] = last_publish_date
            __props__.__dict__["package_id"] = package_id
            __props__.__dict__["providers"] = providers
            __props__.__dict__["publisher_display_name"] = publisher_display_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["source"] = source
            __props__.__dict__["support"] = support
            __props__.__dict__["threat_analysis_tactics"] = threat_analysis_tactics
            __props__.__dict__["threat_analysis_techniques"] = threat_analysis_techniques
            if version is None and not opts.urn:
                raise TypeError("Missing required property 'version'")
            __props__.__dict__["version"] = version
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:securityinsights:ContentPackage"), pulumi.Alias(type_="azure-native:securityinsights/v20230401preview:ContentPackage"), pulumi.Alias(type_="azure-native:securityinsights/v20230501preview:ContentPackage"), pulumi.Alias(type_="azure-native:securityinsights/v20230701preview:ContentPackage"), pulumi.Alias(type_="azure-native:securityinsights/v20230801preview:ContentPackage"), pulumi.Alias(type_="azure-native:securityinsights/v20230901preview:ContentPackage"), pulumi.Alias(type_="azure-native:securityinsights/v20231001preview:ContentPackage"), pulumi.Alias(type_="azure-native:securityinsights/v20231101:ContentPackage"), pulumi.Alias(type_="azure-native:securityinsights/v20231201preview:ContentPackage"), pulumi.Alias(type_="azure-native:securityinsights/v20240101preview:ContentPackage"), pulumi.Alias(type_="azure-native:securityinsights/v20240301:ContentPackage")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ContentPackage, __self__).__init__(
            'azure-native:securityinsights/v20230601preview:ContentPackage',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ContentPackage':
        """
        Get an existing ContentPackage resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContentPackageArgs.__new__(ContentPackageArgs)

        __props__.__dict__["author"] = None
        __props__.__dict__["categories"] = None
        __props__.__dict__["content_id"] = None
        __props__.__dict__["content_kind"] = None
        __props__.__dict__["content_schema_version"] = None
        __props__.__dict__["dependencies"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["first_publish_date"] = None
        __props__.__dict__["icon"] = None
        __props__.__dict__["is_featured"] = None
        __props__.__dict__["is_new"] = None
        __props__.__dict__["is_preview"] = None
        __props__.__dict__["last_publish_date"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["providers"] = None
        __props__.__dict__["publisher_display_name"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["support"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["threat_analysis_tactics"] = None
        __props__.__dict__["threat_analysis_techniques"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return ContentPackage(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def author(self) -> pulumi.Output[Optional['outputs.MetadataAuthorResponse']]:
        """
        The author of the package
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter
    def categories(self) -> pulumi.Output[Optional['outputs.MetadataCategoriesResponse']]:
        """
        The categories of the package
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter(name="contentId")
    def content_id(self) -> pulumi.Output[str]:
        """
        The package id
        """
        return pulumi.get(self, "content_id")

    @property
    @pulumi.getter(name="contentKind")
    def content_kind(self) -> pulumi.Output[str]:
        """
        The package kind
        """
        return pulumi.get(self, "content_kind")

    @property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> pulumi.Output[Optional[str]]:
        """
        The version of the content schema.
        """
        return pulumi.get(self, "content_schema_version")

    @property
    @pulumi.getter
    def dependencies(self) -> pulumi.Output[Optional['outputs.MetadataDependenciesResponse']]:
        """
        The support tier of the package
        """
        return pulumi.get(self, "dependencies")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the package
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The display name of the package
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
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> pulumi.Output[Optional[str]]:
        """
        first publish date package item
        """
        return pulumi.get(self, "first_publish_date")

    @property
    @pulumi.getter
    def icon(self) -> pulumi.Output[Optional[str]]:
        """
        the icon identifier. this id can later be fetched from the content metadata
        """
        return pulumi.get(self, "icon")

    @property
    @pulumi.getter(name="isFeatured")
    def is_featured(self) -> pulumi.Output[Optional[str]]:
        """
        Flag indicates if this package is among the featured list.
        """
        return pulumi.get(self, "is_featured")

    @property
    @pulumi.getter(name="isNew")
    def is_new(self) -> pulumi.Output[Optional[str]]:
        """
        Flag indicates if this is a newly published package.
        """
        return pulumi.get(self, "is_new")

    @property
    @pulumi.getter(name="isPreview")
    def is_preview(self) -> pulumi.Output[Optional[str]]:
        """
        Flag indicates if this package is in preview.
        """
        return pulumi.get(self, "is_preview")

    @property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> pulumi.Output[Optional[str]]:
        """
        last publish date for the package item
        """
        return pulumi.get(self, "last_publish_date")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def providers(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Providers for the package item
        """
        return pulumi.get(self, "providers")

    @property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The publisher display name of the package
        """
        return pulumi.get(self, "publisher_display_name")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional['outputs.MetadataSourceResponse']]:
        """
        The source of the package
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def support(self) -> pulumi.Output[Optional['outputs.MetadataSupportResponse']]:
        """
        The support tier of the package
        """
        return pulumi.get(self, "support")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        the tactics the resource covers
        """
        return pulumi.get(self, "threat_analysis_tactics")

    @property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        the techniques the resource covers, these have to be aligned with the tactics being used
        """
        return pulumi.get(self, "threat_analysis_techniques")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        the latest version number of the package
        """
        return pulumi.get(self, "version")

