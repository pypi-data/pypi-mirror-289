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

__all__ = [
    'GetGeoBackupPolicyResult',
    'AwaitableGetGeoBackupPolicyResult',
    'get_geo_backup_policy',
    'get_geo_backup_policy_output',
]

@pulumi.output_type
class GetGeoBackupPolicyResult:
    """
    A Geo backup policy.
    """
    def __init__(__self__, id=None, kind=None, location=None, name=None, state=None, storage_type=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of geo backup policy.  This is metadata used for the Azure portal experience.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Backup policy location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the geo backup policy.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> str:
        """
        The storage type of the geo backup policy.
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetGeoBackupPolicyResult(GetGeoBackupPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGeoBackupPolicyResult(
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            state=self.state,
            storage_type=self.storage_type,
            type=self.type)


def get_geo_backup_policy(database_name: Optional[str] = None,
                          geo_backup_policy_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          server_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGeoBackupPolicyResult:
    """
    Gets a Geo backup policy for the given database resource.


    :param str database_name: The name of the database.
    :param str geo_backup_policy_name: The name of the Geo backup policy. This should always be 'Default'.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['geoBackupPolicyName'] = geo_backup_policy_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20230201preview:getGeoBackupPolicy', __args__, opts=opts, typ=GetGeoBackupPolicyResult).value

    return AwaitableGetGeoBackupPolicyResult(
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        location=pulumi.get(__ret__, 'location'),
        name=pulumi.get(__ret__, 'name'),
        state=pulumi.get(__ret__, 'state'),
        storage_type=pulumi.get(__ret__, 'storage_type'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_geo_backup_policy)
def get_geo_backup_policy_output(database_name: Optional[pulumi.Input[str]] = None,
                                 geo_backup_policy_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 server_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGeoBackupPolicyResult]:
    """
    Gets a Geo backup policy for the given database resource.


    :param str database_name: The name of the database.
    :param str geo_backup_policy_name: The name of the Geo backup policy. This should always be 'Default'.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
