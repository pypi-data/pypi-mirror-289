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

__all__ = [
    'GetContentPackageResult',
    'AwaitableGetContentPackageResult',
    'get_content_package',
    'get_content_package_output',
]

@pulumi.output_type
class GetContentPackageResult:
    """
    Represents a Package in Azure Security Insights.
    """
    def __init__(__self__, author=None, categories=None, content_id=None, content_kind=None, content_product_id=None, content_schema_version=None, dependencies=None, description=None, display_name=None, etag=None, first_publish_date=None, icon=None, id=None, is_deprecated=None, is_featured=None, is_new=None, is_preview=None, last_publish_date=None, name=None, providers=None, publisher_display_name=None, source=None, support=None, system_data=None, threat_analysis_tactics=None, threat_analysis_techniques=None, type=None, version=None):
        if author and not isinstance(author, dict):
            raise TypeError("Expected argument 'author' to be a dict")
        pulumi.set(__self__, "author", author)
        if categories and not isinstance(categories, dict):
            raise TypeError("Expected argument 'categories' to be a dict")
        pulumi.set(__self__, "categories", categories)
        if content_id and not isinstance(content_id, str):
            raise TypeError("Expected argument 'content_id' to be a str")
        pulumi.set(__self__, "content_id", content_id)
        if content_kind and not isinstance(content_kind, str):
            raise TypeError("Expected argument 'content_kind' to be a str")
        pulumi.set(__self__, "content_kind", content_kind)
        if content_product_id and not isinstance(content_product_id, str):
            raise TypeError("Expected argument 'content_product_id' to be a str")
        pulumi.set(__self__, "content_product_id", content_product_id)
        if content_schema_version and not isinstance(content_schema_version, str):
            raise TypeError("Expected argument 'content_schema_version' to be a str")
        pulumi.set(__self__, "content_schema_version", content_schema_version)
        if dependencies and not isinstance(dependencies, dict):
            raise TypeError("Expected argument 'dependencies' to be a dict")
        pulumi.set(__self__, "dependencies", dependencies)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if first_publish_date and not isinstance(first_publish_date, str):
            raise TypeError("Expected argument 'first_publish_date' to be a str")
        pulumi.set(__self__, "first_publish_date", first_publish_date)
        if icon and not isinstance(icon, str):
            raise TypeError("Expected argument 'icon' to be a str")
        pulumi.set(__self__, "icon", icon)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_deprecated and not isinstance(is_deprecated, str):
            raise TypeError("Expected argument 'is_deprecated' to be a str")
        pulumi.set(__self__, "is_deprecated", is_deprecated)
        if is_featured and not isinstance(is_featured, str):
            raise TypeError("Expected argument 'is_featured' to be a str")
        pulumi.set(__self__, "is_featured", is_featured)
        if is_new and not isinstance(is_new, str):
            raise TypeError("Expected argument 'is_new' to be a str")
        pulumi.set(__self__, "is_new", is_new)
        if is_preview and not isinstance(is_preview, str):
            raise TypeError("Expected argument 'is_preview' to be a str")
        pulumi.set(__self__, "is_preview", is_preview)
        if last_publish_date and not isinstance(last_publish_date, str):
            raise TypeError("Expected argument 'last_publish_date' to be a str")
        pulumi.set(__self__, "last_publish_date", last_publish_date)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if providers and not isinstance(providers, list):
            raise TypeError("Expected argument 'providers' to be a list")
        pulumi.set(__self__, "providers", providers)
        if publisher_display_name and not isinstance(publisher_display_name, str):
            raise TypeError("Expected argument 'publisher_display_name' to be a str")
        pulumi.set(__self__, "publisher_display_name", publisher_display_name)
        if source and not isinstance(source, dict):
            raise TypeError("Expected argument 'source' to be a dict")
        pulumi.set(__self__, "source", source)
        if support and not isinstance(support, dict):
            raise TypeError("Expected argument 'support' to be a dict")
        pulumi.set(__self__, "support", support)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if threat_analysis_tactics and not isinstance(threat_analysis_tactics, list):
            raise TypeError("Expected argument 'threat_analysis_tactics' to be a list")
        pulumi.set(__self__, "threat_analysis_tactics", threat_analysis_tactics)
        if threat_analysis_techniques and not isinstance(threat_analysis_techniques, list):
            raise TypeError("Expected argument 'threat_analysis_techniques' to be a list")
        pulumi.set(__self__, "threat_analysis_techniques", threat_analysis_techniques)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def author(self) -> Optional['outputs.MetadataAuthorResponse']:
        """
        The author of the package
        """
        return pulumi.get(self, "author")

    @property
    @pulumi.getter
    def categories(self) -> Optional['outputs.MetadataCategoriesResponse']:
        """
        The categories of the package
        """
        return pulumi.get(self, "categories")

    @property
    @pulumi.getter(name="contentId")
    def content_id(self) -> str:
        """
        The content id of the package
        """
        return pulumi.get(self, "content_id")

    @property
    @pulumi.getter(name="contentKind")
    def content_kind(self) -> str:
        """
        The package kind
        """
        return pulumi.get(self, "content_kind")

    @property
    @pulumi.getter(name="contentProductId")
    def content_product_id(self) -> str:
        """
        Unique ID for the content. It should be generated based on the contentId, contentKind and the contentVersion of the package
        """
        return pulumi.get(self, "content_product_id")

    @property
    @pulumi.getter(name="contentSchemaVersion")
    def content_schema_version(self) -> Optional[str]:
        """
        The version of the content schema.
        """
        return pulumi.get(self, "content_schema_version")

    @property
    @pulumi.getter
    def dependencies(self) -> Optional['outputs.MetadataDependenciesResponse']:
        """
        The support tier of the package
        """
        return pulumi.get(self, "dependencies")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the package
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the package
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="firstPublishDate")
    def first_publish_date(self) -> Optional[str]:
        """
        first publish date package item
        """
        return pulumi.get(self, "first_publish_date")

    @property
    @pulumi.getter
    def icon(self) -> Optional[str]:
        """
        the icon identifier. this id can later be fetched from the content metadata
        """
        return pulumi.get(self, "icon")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDeprecated")
    def is_deprecated(self) -> Optional[str]:
        """
        Flag indicates if this template is deprecated
        """
        return pulumi.get(self, "is_deprecated")

    @property
    @pulumi.getter(name="isFeatured")
    def is_featured(self) -> Optional[str]:
        """
        Flag indicates if this package is among the featured list.
        """
        return pulumi.get(self, "is_featured")

    @property
    @pulumi.getter(name="isNew")
    def is_new(self) -> Optional[str]:
        """
        Flag indicates if this is a newly published package.
        """
        return pulumi.get(self, "is_new")

    @property
    @pulumi.getter(name="isPreview")
    def is_preview(self) -> Optional[str]:
        """
        Flag indicates if this package is in preview.
        """
        return pulumi.get(self, "is_preview")

    @property
    @pulumi.getter(name="lastPublishDate")
    def last_publish_date(self) -> Optional[str]:
        """
        last publish date for the package item
        """
        return pulumi.get(self, "last_publish_date")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def providers(self) -> Optional[Sequence[str]]:
        """
        Providers for the package item
        """
        return pulumi.get(self, "providers")

    @property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> Optional[str]:
        """
        The publisher display name of the package
        """
        return pulumi.get(self, "publisher_display_name")

    @property
    @pulumi.getter
    def source(self) -> Optional['outputs.MetadataSourceResponse']:
        """
        The source of the package
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def support(self) -> Optional['outputs.MetadataSupportResponse']:
        """
        The support tier of the package
        """
        return pulumi.get(self, "support")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="threatAnalysisTactics")
    def threat_analysis_tactics(self) -> Optional[Sequence[str]]:
        """
        the tactics the resource covers
        """
        return pulumi.get(self, "threat_analysis_tactics")

    @property
    @pulumi.getter(name="threatAnalysisTechniques")
    def threat_analysis_techniques(self) -> Optional[Sequence[str]]:
        """
        the techniques the resource covers, these have to be aligned with the tactics being used
        """
        return pulumi.get(self, "threat_analysis_techniques")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        the latest version number of the package
        """
        return pulumi.get(self, "version")


class AwaitableGetContentPackageResult(GetContentPackageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContentPackageResult(
            author=self.author,
            categories=self.categories,
            content_id=self.content_id,
            content_kind=self.content_kind,
            content_product_id=self.content_product_id,
            content_schema_version=self.content_schema_version,
            dependencies=self.dependencies,
            description=self.description,
            display_name=self.display_name,
            etag=self.etag,
            first_publish_date=self.first_publish_date,
            icon=self.icon,
            id=self.id,
            is_deprecated=self.is_deprecated,
            is_featured=self.is_featured,
            is_new=self.is_new,
            is_preview=self.is_preview,
            last_publish_date=self.last_publish_date,
            name=self.name,
            providers=self.providers,
            publisher_display_name=self.publisher_display_name,
            source=self.source,
            support=self.support,
            system_data=self.system_data,
            threat_analysis_tactics=self.threat_analysis_tactics,
            threat_analysis_techniques=self.threat_analysis_techniques,
            type=self.type,
            version=self.version)


def get_content_package(package_id: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        workspace_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContentPackageResult:
    """
    Gets an installed packages by its id.


    :param str package_id: package Id
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['packageId'] = package_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20240301:getContentPackage', __args__, opts=opts, typ=GetContentPackageResult).value

    return AwaitableGetContentPackageResult(
        author=pulumi.get(__ret__, 'author'),
        categories=pulumi.get(__ret__, 'categories'),
        content_id=pulumi.get(__ret__, 'content_id'),
        content_kind=pulumi.get(__ret__, 'content_kind'),
        content_product_id=pulumi.get(__ret__, 'content_product_id'),
        content_schema_version=pulumi.get(__ret__, 'content_schema_version'),
        dependencies=pulumi.get(__ret__, 'dependencies'),
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        etag=pulumi.get(__ret__, 'etag'),
        first_publish_date=pulumi.get(__ret__, 'first_publish_date'),
        icon=pulumi.get(__ret__, 'icon'),
        id=pulumi.get(__ret__, 'id'),
        is_deprecated=pulumi.get(__ret__, 'is_deprecated'),
        is_featured=pulumi.get(__ret__, 'is_featured'),
        is_new=pulumi.get(__ret__, 'is_new'),
        is_preview=pulumi.get(__ret__, 'is_preview'),
        last_publish_date=pulumi.get(__ret__, 'last_publish_date'),
        name=pulumi.get(__ret__, 'name'),
        providers=pulumi.get(__ret__, 'providers'),
        publisher_display_name=pulumi.get(__ret__, 'publisher_display_name'),
        source=pulumi.get(__ret__, 'source'),
        support=pulumi.get(__ret__, 'support'),
        system_data=pulumi.get(__ret__, 'system_data'),
        threat_analysis_tactics=pulumi.get(__ret__, 'threat_analysis_tactics'),
        threat_analysis_techniques=pulumi.get(__ret__, 'threat_analysis_techniques'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_content_package)
def get_content_package_output(package_id: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               workspace_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContentPackageResult]:
    """
    Gets an installed packages by its id.


    :param str package_id: package Id
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
