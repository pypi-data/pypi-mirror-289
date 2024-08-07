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

__all__ = [
    'GetFavoriteResult',
    'AwaitableGetFavoriteResult',
    'get_favorite',
    'get_favorite_output',
]

@pulumi.output_type
class GetFavoriteResult:
    """
    Properties that define a favorite that is associated to an Application Insights component.
    """
    def __init__(__self__, category=None, config=None, favorite_id=None, favorite_type=None, is_generated_from_template=None, name=None, source_type=None, tags=None, time_modified=None, user_id=None, version=None):
        if category and not isinstance(category, str):
            raise TypeError("Expected argument 'category' to be a str")
        pulumi.set(__self__, "category", category)
        if config and not isinstance(config, str):
            raise TypeError("Expected argument 'config' to be a str")
        pulumi.set(__self__, "config", config)
        if favorite_id and not isinstance(favorite_id, str):
            raise TypeError("Expected argument 'favorite_id' to be a str")
        pulumi.set(__self__, "favorite_id", favorite_id)
        if favorite_type and not isinstance(favorite_type, str):
            raise TypeError("Expected argument 'favorite_type' to be a str")
        pulumi.set(__self__, "favorite_type", favorite_type)
        if is_generated_from_template and not isinstance(is_generated_from_template, bool):
            raise TypeError("Expected argument 'is_generated_from_template' to be a bool")
        pulumi.set(__self__, "is_generated_from_template", is_generated_from_template)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if source_type and not isinstance(source_type, str):
            raise TypeError("Expected argument 'source_type' to be a str")
        pulumi.set(__self__, "source_type", source_type)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if time_modified and not isinstance(time_modified, str):
            raise TypeError("Expected argument 'time_modified' to be a str")
        pulumi.set(__self__, "time_modified", time_modified)
        if user_id and not isinstance(user_id, str):
            raise TypeError("Expected argument 'user_id' to be a str")
        pulumi.set(__self__, "user_id", user_id)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def category(self) -> Optional[str]:
        """
        Favorite category, as defined by the user at creation time.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def config(self) -> Optional[str]:
        """
        Configuration of this particular favorite, which are driven by the Azure portal UX. Configuration data is a string containing valid JSON
        """
        return pulumi.get(self, "config")

    @property
    @pulumi.getter(name="favoriteId")
    def favorite_id(self) -> str:
        """
        Internally assigned unique id of the favorite definition.
        """
        return pulumi.get(self, "favorite_id")

    @property
    @pulumi.getter(name="favoriteType")
    def favorite_type(self) -> Optional[str]:
        """
        Enum indicating if this favorite definition is owned by a specific user or is shared between all users with access to the Application Insights component.
        """
        return pulumi.get(self, "favorite_type")

    @property
    @pulumi.getter(name="isGeneratedFromTemplate")
    def is_generated_from_template(self) -> Optional[bool]:
        """
        Flag denoting wether or not this favorite was generated from a template.
        """
        return pulumi.get(self, "is_generated_from_template")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The user-defined name of the favorite.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[str]:
        """
        The source of the favorite definition.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[str]]:
        """
        A list of 0 or more tags that are associated with this favorite definition
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeModified")
    def time_modified(self) -> str:
        """
        Date and time in UTC of the last modification that was made to this favorite definition.
        """
        return pulumi.get(self, "time_modified")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> str:
        """
        Unique user id of the specific user that owns this favorite.
        """
        return pulumi.get(self, "user_id")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        This instance's version of the data model. This can change as new features are added that can be marked favorite. Current examples include MetricsExplorer (ME) and Search.
        """
        return pulumi.get(self, "version")


class AwaitableGetFavoriteResult(GetFavoriteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFavoriteResult(
            category=self.category,
            config=self.config,
            favorite_id=self.favorite_id,
            favorite_type=self.favorite_type,
            is_generated_from_template=self.is_generated_from_template,
            name=self.name,
            source_type=self.source_type,
            tags=self.tags,
            time_modified=self.time_modified,
            user_id=self.user_id,
            version=self.version)


def get_favorite(favorite_id: Optional[str] = None,
                 resource_group_name: Optional[str] = None,
                 resource_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFavoriteResult:
    """
    Get a single favorite by its FavoriteId, defined within an Application Insights component.
    Azure REST API version: 2015-05-01.


    :param str favorite_id: The Id of a specific favorite defined in the Application Insights component
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    """
    __args__ = dict()
    __args__['favoriteId'] = favorite_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:insights:getFavorite', __args__, opts=opts, typ=GetFavoriteResult).value

    return AwaitableGetFavoriteResult(
        category=pulumi.get(__ret__, 'category'),
        config=pulumi.get(__ret__, 'config'),
        favorite_id=pulumi.get(__ret__, 'favorite_id'),
        favorite_type=pulumi.get(__ret__, 'favorite_type'),
        is_generated_from_template=pulumi.get(__ret__, 'is_generated_from_template'),
        name=pulumi.get(__ret__, 'name'),
        source_type=pulumi.get(__ret__, 'source_type'),
        tags=pulumi.get(__ret__, 'tags'),
        time_modified=pulumi.get(__ret__, 'time_modified'),
        user_id=pulumi.get(__ret__, 'user_id'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_favorite)
def get_favorite_output(favorite_id: Optional[pulumi.Input[str]] = None,
                        resource_group_name: Optional[pulumi.Input[str]] = None,
                        resource_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFavoriteResult]:
    """
    Get a single favorite by its FavoriteId, defined within an Application Insights component.
    Azure REST API version: 2015-05-01.


    :param str favorite_id: The Id of a specific favorite defined in the Application Insights component
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the Application Insights component resource.
    """
    ...
