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
    'GetPython3PackageResult',
    'AwaitableGetPython3PackageResult',
    'get_python3_package',
    'get_python3_package_output',
]

@pulumi.output_type
class GetPython3PackageResult:
    """
    Definition of the module type.
    """
    def __init__(__self__, activity_count=None, content_link=None, creation_time=None, description=None, error=None, etag=None, id=None, is_composite=None, is_global=None, last_modified_time=None, location=None, name=None, provisioning_state=None, size_in_bytes=None, system_data=None, tags=None, type=None, version=None):
        if activity_count and not isinstance(activity_count, int):
            raise TypeError("Expected argument 'activity_count' to be a int")
        pulumi.set(__self__, "activity_count", activity_count)
        if content_link and not isinstance(content_link, dict):
            raise TypeError("Expected argument 'content_link' to be a dict")
        pulumi.set(__self__, "content_link", content_link)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_composite and not isinstance(is_composite, bool):
            raise TypeError("Expected argument 'is_composite' to be a bool")
        pulumi.set(__self__, "is_composite", is_composite)
        if is_global and not isinstance(is_global, bool):
            raise TypeError("Expected argument 'is_global' to be a bool")
        pulumi.set(__self__, "is_global", is_global)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if size_in_bytes and not isinstance(size_in_bytes, float):
            raise TypeError("Expected argument 'size_in_bytes' to be a float")
        pulumi.set(__self__, "size_in_bytes", size_in_bytes)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="activityCount")
    def activity_count(self) -> Optional[int]:
        """
        Gets or sets the activity count of the module.
        """
        return pulumi.get(self, "activity_count")

    @property
    @pulumi.getter(name="contentLink")
    def content_link(self) -> Optional['outputs.ContentLinkResponse']:
        """
        Gets or sets the contentLink of the module.
        """
        return pulumi.get(self, "content_link")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[str]:
        """
        Gets or sets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def error(self) -> Optional['outputs.ModuleErrorInfoResponse']:
        """
        Gets or sets the error info of the module.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Gets or sets the etag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}"
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isComposite")
    def is_composite(self) -> Optional[bool]:
        """
        Gets or sets type of module, if its composite or not.
        """
        return pulumi.get(self, "is_composite")

    @property
    @pulumi.getter(name="isGlobal")
    def is_global(self) -> Optional[bool]:
        """
        Gets or sets the isGlobal flag of the module.
        """
        return pulumi.get(self, "is_global")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> Optional[str]:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        Gets or sets the provisioning state of the module.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sizeInBytes")
    def size_in_bytes(self) -> Optional[float]:
        """
        Gets or sets the size in bytes of the module.
        """
        return pulumi.get(self, "size_in_bytes")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        Gets or sets the version of the module.
        """
        return pulumi.get(self, "version")


class AwaitableGetPython3PackageResult(GetPython3PackageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPython3PackageResult(
            activity_count=self.activity_count,
            content_link=self.content_link,
            creation_time=self.creation_time,
            description=self.description,
            error=self.error,
            etag=self.etag,
            id=self.id,
            is_composite=self.is_composite,
            is_global=self.is_global,
            last_modified_time=self.last_modified_time,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            size_in_bytes=self.size_in_bytes,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            version=self.version)


def get_python3_package(automation_account_name: Optional[str] = None,
                        package_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPython3PackageResult:
    """
    Retrieve the python 3 package identified by package name.


    :param str automation_account_name: The name of the automation account.
    :param str package_name: The python package name.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    __args__ = dict()
    __args__['automationAccountName'] = automation_account_name
    __args__['packageName'] = package_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:automation/v20230515preview:getPython3Package', __args__, opts=opts, typ=GetPython3PackageResult).value

    return AwaitableGetPython3PackageResult(
        activity_count=pulumi.get(__ret__, 'activity_count'),
        content_link=pulumi.get(__ret__, 'content_link'),
        creation_time=pulumi.get(__ret__, 'creation_time'),
        description=pulumi.get(__ret__, 'description'),
        error=pulumi.get(__ret__, 'error'),
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        is_composite=pulumi.get(__ret__, 'is_composite'),
        is_global=pulumi.get(__ret__, 'is_global'),
        last_modified_time=pulumi.get(__ret__, 'last_modified_time'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        size_in_bytes=pulumi.get(__ret__, 'size_in_bytes'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'),
        version=pulumi.get(__ret__, 'version'))


@_utilities.lift_output_func(get_python3_package)
def get_python3_package_output(automation_account_name: Optional[pulumi.Input[str]] = None,
                               package_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPython3PackageResult]:
    """
    Retrieve the python 3 package identified by package name.


    :param str automation_account_name: The name of the automation account.
    :param str package_name: The python package name.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    ...
