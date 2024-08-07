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
    'GetHuntRelationResult',
    'AwaitableGetHuntRelationResult',
    'get_hunt_relation',
    'get_hunt_relation_output',
]

@pulumi.output_type
class GetHuntRelationResult:
    """
    Represents a Hunt Relation in Azure Security Insights.
    """
    def __init__(__self__, etag=None, id=None, labels=None, name=None, related_resource_id=None, related_resource_kind=None, related_resource_name=None, relation_type=None, system_data=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, list):
            raise TypeError("Expected argument 'labels' to be a list")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if related_resource_id and not isinstance(related_resource_id, str):
            raise TypeError("Expected argument 'related_resource_id' to be a str")
        pulumi.set(__self__, "related_resource_id", related_resource_id)
        if related_resource_kind and not isinstance(related_resource_kind, str):
            raise TypeError("Expected argument 'related_resource_kind' to be a str")
        pulumi.set(__self__, "related_resource_kind", related_resource_kind)
        if related_resource_name and not isinstance(related_resource_name, str):
            raise TypeError("Expected argument 'related_resource_name' to be a str")
        pulumi.set(__self__, "related_resource_name", related_resource_name)
        if relation_type and not isinstance(relation_type, str):
            raise TypeError("Expected argument 'relation_type' to be a str")
        pulumi.set(__self__, "relation_type", relation_type)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
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
    def labels(self) -> Optional[Sequence[str]]:
        """
        List of labels relevant to this hunt
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="relatedResourceId")
    def related_resource_id(self) -> str:
        """
        The id of the related resource
        """
        return pulumi.get(self, "related_resource_id")

    @property
    @pulumi.getter(name="relatedResourceKind")
    def related_resource_kind(self) -> str:
        """
        The resource that the relation is related to
        """
        return pulumi.get(self, "related_resource_kind")

    @property
    @pulumi.getter(name="relatedResourceName")
    def related_resource_name(self) -> str:
        """
        The name of the related resource
        """
        return pulumi.get(self, "related_resource_name")

    @property
    @pulumi.getter(name="relationType")
    def relation_type(self) -> str:
        """
        The type of the hunt relation
        """
        return pulumi.get(self, "relation_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetHuntRelationResult(GetHuntRelationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHuntRelationResult(
            etag=self.etag,
            id=self.id,
            labels=self.labels,
            name=self.name,
            related_resource_id=self.related_resource_id,
            related_resource_kind=self.related_resource_kind,
            related_resource_name=self.related_resource_name,
            relation_type=self.relation_type,
            system_data=self.system_data,
            type=self.type)


def get_hunt_relation(hunt_id: Optional[str] = None,
                      hunt_relation_id: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      workspace_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHuntRelationResult:
    """
    Gets a hunt relation


    :param str hunt_id: The hunt id (GUID)
    :param str hunt_relation_id: The hunt relation id (GUID)
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['huntId'] = hunt_id
    __args__['huntRelationId'] = hunt_relation_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20230701preview:getHuntRelation', __args__, opts=opts, typ=GetHuntRelationResult).value

    return AwaitableGetHuntRelationResult(
        etag=pulumi.get(__ret__, 'etag'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        related_resource_id=pulumi.get(__ret__, 'related_resource_id'),
        related_resource_kind=pulumi.get(__ret__, 'related_resource_kind'),
        related_resource_name=pulumi.get(__ret__, 'related_resource_name'),
        relation_type=pulumi.get(__ret__, 'relation_type'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_hunt_relation)
def get_hunt_relation_output(hunt_id: Optional[pulumi.Input[str]] = None,
                             hunt_relation_id: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             workspace_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHuntRelationResult]:
    """
    Gets a hunt relation


    :param str hunt_id: The hunt id (GUID)
    :param str hunt_relation_id: The hunt relation id (GUID)
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
