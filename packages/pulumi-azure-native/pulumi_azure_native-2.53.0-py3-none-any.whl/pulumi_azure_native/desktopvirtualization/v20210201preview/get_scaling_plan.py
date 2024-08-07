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
    'GetScalingPlanResult',
    'AwaitableGetScalingPlanResult',
    'get_scaling_plan',
    'get_scaling_plan_output',
]

@pulumi.output_type
class GetScalingPlanResult:
    """
    Represents a scaling plan definition.
    """
    def __init__(__self__, description=None, etag=None, exclusion_tag=None, friendly_name=None, host_pool_references=None, host_pool_type=None, id=None, identity=None, kind=None, location=None, managed_by=None, name=None, object_id=None, plan=None, ring=None, schedules=None, sku=None, tags=None, time_zone=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if exclusion_tag and not isinstance(exclusion_tag, str):
            raise TypeError("Expected argument 'exclusion_tag' to be a str")
        pulumi.set(__self__, "exclusion_tag", exclusion_tag)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if host_pool_references and not isinstance(host_pool_references, list):
            raise TypeError("Expected argument 'host_pool_references' to be a list")
        pulumi.set(__self__, "host_pool_references", host_pool_references)
        if host_pool_type and not isinstance(host_pool_type, str):
            raise TypeError("Expected argument 'host_pool_type' to be a str")
        pulumi.set(__self__, "host_pool_type", host_pool_type)
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
        if object_id and not isinstance(object_id, str):
            raise TypeError("Expected argument 'object_id' to be a str")
        pulumi.set(__self__, "object_id", object_id)
        if plan and not isinstance(plan, dict):
            raise TypeError("Expected argument 'plan' to be a dict")
        pulumi.set(__self__, "plan", plan)
        if ring and not isinstance(ring, int):
            raise TypeError("Expected argument 'ring' to be a int")
        pulumi.set(__self__, "ring", ring)
        if schedules and not isinstance(schedules, list):
            raise TypeError("Expected argument 'schedules' to be a list")
        pulumi.set(__self__, "schedules", schedules)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of scaling plan.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. 
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="exclusionTag")
    def exclusion_tag(self) -> Optional[str]:
        """
        Exclusion tag for scaling plan.
        """
        return pulumi.get(self, "exclusion_tag")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        User friendly name of scaling plan.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hostPoolReferences")
    def host_pool_references(self) -> Optional[Sequence['outputs.ScalingHostPoolReferenceResponse']]:
        """
        List of ScalingHostPoolReference definitions.
        """
        return pulumi.get(self, "host_pool_references")

    @property
    @pulumi.getter(name="hostPoolType")
    def host_pool_type(self) -> Optional[str]:
        """
        HostPool type for desktop.
        """
        return pulumi.get(self, "host_pool_type")

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
    @pulumi.getter(name="objectId")
    def object_id(self) -> str:
        """
        ObjectId of scaling plan. (internal use)
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter
    def plan(self) -> Optional['outputs.ResourceModelWithAllowedPropertySetResponsePlan']:
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def ring(self) -> Optional[int]:
        """
        The ring number of scaling plan.
        """
        return pulumi.get(self, "ring")

    @property
    @pulumi.getter
    def schedules(self) -> Optional[Sequence['outputs.ScalingScheduleResponse']]:
        """
        List of ScalingSchedule definitions.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.ResourceModelWithAllowedPropertySetResponseSku']:
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[str]:
        """
        Timezone of the scaling plan.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetScalingPlanResult(GetScalingPlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScalingPlanResult(
            description=self.description,
            etag=self.etag,
            exclusion_tag=self.exclusion_tag,
            friendly_name=self.friendly_name,
            host_pool_references=self.host_pool_references,
            host_pool_type=self.host_pool_type,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            location=self.location,
            managed_by=self.managed_by,
            name=self.name,
            object_id=self.object_id,
            plan=self.plan,
            ring=self.ring,
            schedules=self.schedules,
            sku=self.sku,
            tags=self.tags,
            time_zone=self.time_zone,
            type=self.type)


def get_scaling_plan(resource_group_name: Optional[str] = None,
                     scaling_plan_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScalingPlanResult:
    """
    Get a scaling plan.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str scaling_plan_name: The name of the scaling plan.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['scalingPlanName'] = scaling_plan_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:desktopvirtualization/v20210201preview:getScalingPlan', __args__, opts=opts, typ=GetScalingPlanResult).value

    return AwaitableGetScalingPlanResult(
        description=pulumi.get(__ret__, 'description'),
        etag=pulumi.get(__ret__, 'etag'),
        exclusion_tag=pulumi.get(__ret__, 'exclusion_tag'),
        friendly_name=pulumi.get(__ret__, 'friendly_name'),
        host_pool_references=pulumi.get(__ret__, 'host_pool_references'),
        host_pool_type=pulumi.get(__ret__, 'host_pool_type'),
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        managed_by=pulumi.get(__ret__, 'managed_by'),
        name=pulumi.get(__ret__, 'name'),
        object_id=pulumi.get(__ret__, 'object_id'),
        plan=pulumi.get(__ret__, 'plan'),
        ring=pulumi.get(__ret__, 'ring'),
        schedules=pulumi.get(__ret__, 'schedules'),
        sku=pulumi.get(__ret__, 'sku'),
        tags=pulumi.get(__ret__, 'tags'),
        time_zone=pulumi.get(__ret__, 'time_zone'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_scaling_plan)
def get_scaling_plan_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                            scaling_plan_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScalingPlanResult]:
    """
    Get a scaling plan.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str scaling_plan_name: The name of the scaling plan.
    """
    ...
