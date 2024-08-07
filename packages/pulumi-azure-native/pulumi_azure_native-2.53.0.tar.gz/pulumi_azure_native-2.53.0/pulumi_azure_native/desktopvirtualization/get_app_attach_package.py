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

__all__ = [
    'GetAppAttachPackageResult',
    'AwaitableGetAppAttachPackageResult',
    'get_app_attach_package',
    'get_app_attach_package_output',
]

@pulumi.output_type
class GetAppAttachPackageResult:
    """
    Schema for App Attach Package properties.
    """
    def __init__(__self__, etag=None, id=None, identity=None, kind=None, location=None, managed_by=None, name=None, plan=None, properties=None, sku=None, system_data=None, tags=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_by and not isinstance(managed_by, str):
            raise TypeError("Expected argument 'managed_by' to be a str")
        pulumi.set(__self__, "managed_by", managed_by)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if plan and not isinstance(plan, dict):
            raise TypeError("Expected argument 'plan' to be a dict")
        pulumi.set(__self__, "plan", plan)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. 
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ResourceModelWithAllowedPropertySetResponseIdentity']:
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Metadata used by portal/tooling/etc to render different UX experiences for resources of the same type; e.g. ApiApps are a kind of Microsoft.Web/sites type.  If supported, the resource provider must validate and persist this value.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> Optional[str]:
        """
        The fully qualified resource ID of the resource that manages this resource. Indicates if this resource is managed by another Azure resource. If this is present, complete mode deployment will not delete the resource if it is removed from the template since it is managed by another resource.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plan(self) -> Optional['outputs.ResourceModelWithAllowedPropertySetResponsePlan']:
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.AppAttachPackagePropertiesResponse':
        """
        Detailed properties for App Attach Package
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.ResourceModelWithAllowedPropertySetResponseSku']:
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
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


class AwaitableGetAppAttachPackageResult(GetAppAttachPackageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAppAttachPackageResult(
            etag=self.etag,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            location=self.location,
            managed_by=self.managed_by,
            name=self.name,
            plan=self.plan,
            properties=self.properties,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_app_attach_package(app_attach_package_name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAppAttachPackageResult:
    """
    Get an app attach package.
    Azure REST API version: 2023-10-04-preview.

    Other available API versions: 2023-11-01-preview, 2024-01-16-preview, 2024-03-06-preview, 2024-04-03, 2024-04-08-preview.


    :param str app_attach_package_name: The name of the App Attach package arm object
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['appAttachPackageName'] = app_attach_package_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:desktopvirtualization:getAppAttachPackage', __args__, opts=opts, typ=GetAppAttachPackageResult).value

    return AwaitableGetAppAttachPackageResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        managed_by=pulumi.get(__ret__, 'managed_by'),
        name=pulumi.get(__ret__, 'name'),
        plan=pulumi.get(__ret__, 'plan'),
        properties=pulumi.get(__ret__, 'properties'),
        sku=pulumi.get(__ret__, 'sku'),
        system_data=pulumi.get(__ret__, 'system_data'),
        tags=pulumi.get(__ret__, 'tags'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_app_attach_package)
def get_app_attach_package_output(app_attach_package_name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAppAttachPackageResult]:
    """
    Get an app attach package.
    Azure REST API version: 2023-10-04-preview.

    Other available API versions: 2023-11-01-preview, 2024-01-16-preview, 2024-03-06-preview, 2024-04-03, 2024-04-08-preview.


    :param str app_attach_package_name: The name of the App Attach package arm object
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
