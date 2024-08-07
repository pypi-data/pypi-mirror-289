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
    'GetHybridIdentityMetadatumResult',
    'AwaitableGetHybridIdentityMetadatumResult',
    'get_hybrid_identity_metadatum',
    'get_hybrid_identity_metadatum_output',
]

@pulumi.output_type
class GetHybridIdentityMetadatumResult:
    """
    Defines the hybridIdentityMetadata.
    """
    def __init__(__self__, id=None, identity=None, name=None, provisioning_state=None, public_key=None, resource_uid=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if resource_uid and not isinstance(resource_uid, str):
            raise TypeError("Expected argument 'resource_uid' to be a str")
        pulumi.set(__self__, "resource_uid", resource_uid)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ProvisionedClusterIdentityResponse']:
        """
        The identity of the provisioned cluster.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        provisioning state of the hybridIdentityMetadata resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[str]:
        """
        Onboarding public key for provisioning the Managed identity for the HybridAKS cluster.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> Optional[str]:
        """
        Unique id of the parent provisioned cluster resource.
        """
        return pulumi.get(self, "resource_uid")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetHybridIdentityMetadatumResult(GetHybridIdentityMetadatumResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHybridIdentityMetadatumResult(
            id=self.id,
            identity=self.identity,
            name=self.name,
            provisioning_state=self.provisioning_state,
            public_key=self.public_key,
            resource_uid=self.resource_uid,
            system_data=self.system_data,
            type=self.type)


def get_hybrid_identity_metadatum(hybrid_identity_metadata_resource_name: Optional[str] = None,
                                  provisioned_clusters_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHybridIdentityMetadatumResult:
    """
    Get the hybrid identity metadata proxy resource.


    :param str hybrid_identity_metadata_resource_name: Parameter for the name of the hybrid identity metadata resource.
    :param str provisioned_clusters_name: Parameter for the name of the provisioned cluster
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['hybridIdentityMetadataResourceName'] = hybrid_identity_metadata_resource_name
    __args__['provisionedClustersName'] = provisioned_clusters_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:hybridcontainerservice/v20220501preview:getHybridIdentityMetadatum', __args__, opts=opts, typ=GetHybridIdentityMetadatumResult).value

    return AwaitableGetHybridIdentityMetadatumResult(
        id=pulumi.get(__ret__, 'id'),
        identity=pulumi.get(__ret__, 'identity'),
        name=pulumi.get(__ret__, 'name'),
        provisioning_state=pulumi.get(__ret__, 'provisioning_state'),
        public_key=pulumi.get(__ret__, 'public_key'),
        resource_uid=pulumi.get(__ret__, 'resource_uid'),
        system_data=pulumi.get(__ret__, 'system_data'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_hybrid_identity_metadatum)
def get_hybrid_identity_metadatum_output(hybrid_identity_metadata_resource_name: Optional[pulumi.Input[str]] = None,
                                         provisioned_clusters_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHybridIdentityMetadatumResult]:
    """
    Get the hybrid identity metadata proxy resource.


    :param str hybrid_identity_metadata_resource_name: Parameter for the name of the hybrid identity metadata resource.
    :param str provisioned_clusters_name: Parameter for the name of the provisioned cluster
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
