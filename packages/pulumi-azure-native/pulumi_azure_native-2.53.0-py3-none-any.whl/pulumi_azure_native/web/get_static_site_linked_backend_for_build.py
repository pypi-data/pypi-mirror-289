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
    'GetStaticSiteLinkedBackendForBuildResult',
    'AwaitableGetStaticSiteLinkedBackendForBuildResult',
    'get_static_site_linked_backend_for_build',
    'get_static_site_linked_backend_for_build_output',
]

@pulumi.output_type
class GetStaticSiteLinkedBackendForBuildResult:
    """
    Static Site Linked Backend ARM resource.
    """
    def __init__(__self__, backend_resource_id=None, created_on=None, id=None, kind=None, name=None, provisioning_state=None, region=None, type=None):
        if backend_resource_id and not isinstance(backend_resource_id, str):
            raise TypeError("Expected argument 'backend_resource_id' to be a str")
        pulumi.set(__self__, "backend_resource_id", backend_resource_id)
        if created_on and not isinstance(created_on, str):
            raise TypeError("Expected argument 'created_on' to be a str")
        pulumi.set(__self__, "created_on", created_on)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="backendResourceId")
    def backend_resource_id(self) -> Optional[str]:
        """
        The resource id of the backend linked to the static site
        """
        return pulumi.get(self, "backend_resource_id")

    @property
    @pulumi.getter(name="createdOn")
    def created_on(self) -> str:
        """
        The date and time on which the backend was linked to the static site.
        """
        return pulumi.get(self, "created_on")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        Kind of resource.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the linking process.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region of the backend linked to the static site
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetStaticSiteLinkedBackendForBuildResult(GetStaticSiteLinkedBackendForBuildResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStaticSiteLinkedBackendForBuildResult(
            backend_resource_id=self.backend_resource_id,
            created_on=self.created_on,
            id=self.id,
            kind=self.kind,
            name=self.name,
            provisioning_state=self.provisioning_state,
            region=self.region,
            type=self.type)


def get_static_site_linked_backend_for_build(environment_name: Optional[str] = None,
                                             linked_backend_name: Optional[str] = None,
                                             name: Optional[str] = None,
                                             resource_group_name: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStaticSiteLinkedBackendForBuildResult:
    """
    Static Site Linked Backend ARM resource.
    Azure REST API version: 2022-09-01.

    Other available API versions: 2023-01-01, 2023-12-01.


    :param str environment_name: The stage site identifier
    :param str linked_backend_name: Name of the linked backend that should be retrieved
    :param str name: Name of the static site
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['linkedBackendName'] = linked_backend_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web:getStaticSiteLinkedBackendForBuild', __args__, opts=opts, typ=GetStaticSiteLinkedBackendForBuildResult).value

    return AwaitableGetStaticSiteLinkedBackendForBuildResult(
        backend_resource_id=pulumi.get(__ret__, 'backend_resource_id'),
        created_on=pulumi.get(__ret__, 'created_on'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        region=pulumi.get(__ret__, 'region'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_static_site_linked_backend_for_build)
def get_static_site_linked_backend_for_build_output(environment_name: Optional[pulumi.Input[str]] = None,
                                                    linked_backend_name: Optional[pulumi.Input[str]] = None,
                                                    name: Optional[pulumi.Input[str]] = None,
                                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStaticSiteLinkedBackendForBuildResult]:
    """
    Static Site Linked Backend ARM resource.
    Azure REST API version: 2022-09-01.

    Other available API versions: 2023-01-01, 2023-12-01.


    :param str environment_name: The stage site identifier
    :param str linked_backend_name: Name of the linked backend that should be retrieved
    :param str name: Name of the static site
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    """
    ...
