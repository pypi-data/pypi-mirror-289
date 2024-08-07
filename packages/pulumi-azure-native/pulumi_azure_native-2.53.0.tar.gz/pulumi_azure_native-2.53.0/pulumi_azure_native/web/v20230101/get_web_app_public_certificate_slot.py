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
    'GetWebAppPublicCertificateSlotResult',
    'AwaitableGetWebAppPublicCertificateSlotResult',
    'get_web_app_public_certificate_slot',
    'get_web_app_public_certificate_slot_output',
]

@pulumi.output_type
class GetWebAppPublicCertificateSlotResult:
    """
    Public certificate object
    """
    def __init__(__self__, blob=None, id=None, kind=None, name=None, public_certificate_location=None, thumbprint=None, type=None):
        if blob and not isinstance(blob, str):
            raise TypeError("Expected argument 'blob' to be a str")
        pulumi.set(__self__, "blob", blob)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if public_certificate_location and not isinstance(public_certificate_location, str):
            raise TypeError("Expected argument 'public_certificate_location' to be a str")
        pulumi.set(__self__, "public_certificate_location", public_certificate_location)
        if thumbprint and not isinstance(thumbprint, str):
            raise TypeError("Expected argument 'thumbprint' to be a str")
        pulumi.set(__self__, "thumbprint", thumbprint)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def blob(self) -> Optional[str]:
        """
        Public Certificate byte array
        """
        return pulumi.get(self, "blob")

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
    @pulumi.getter(name="publicCertificateLocation")
    def public_certificate_location(self) -> Optional[str]:
        """
        Public Certificate Location
        """
        return pulumi.get(self, "public_certificate_location")

    @property
    @pulumi.getter
    def thumbprint(self) -> str:
        """
        Certificate Thumbprint
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetWebAppPublicCertificateSlotResult(GetWebAppPublicCertificateSlotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWebAppPublicCertificateSlotResult(
            blob=self.blob,
            id=self.id,
            kind=self.kind,
            name=self.name,
            public_certificate_location=self.public_certificate_location,
            thumbprint=self.thumbprint,
            type=self.type)


def get_web_app_public_certificate_slot(name: Optional[str] = None,
                                        public_certificate_name: Optional[str] = None,
                                        resource_group_name: Optional[str] = None,
                                        slot: Optional[str] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWebAppPublicCertificateSlotResult:
    """
    Description for Get the named public certificate for an app (or deployment slot, if specified).


    :param str name: Name of the app.
    :param str public_certificate_name: Public certificate name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str slot: Name of the deployment slot. If a slot is not specified, the API the named binding for the production slot.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['publicCertificateName'] = public_certificate_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['slot'] = slot
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:web/v20230101:getWebAppPublicCertificateSlot', __args__, opts=opts, typ=GetWebAppPublicCertificateSlotResult).value

    return AwaitableGetWebAppPublicCertificateSlotResult(
        blob=pulumi.get(__ret__, 'blob'),
        id=pulumi.get(__ret__, 'id'),
        kind=pulumi.get(__ret__, 'kind'),
        name=pulumi.get(__ret__, 'name'),
        public_certificate_location=pulumi.get(__ret__, 'public_certificate_location'),
        thumbprint=pulumi.get(__ret__, 'thumbprint'),
        type=pulumi.get(__ret__, 'type'))


@_utilities.lift_output_func(get_web_app_public_certificate_slot)
def get_web_app_public_certificate_slot_output(name: Optional[pulumi.Input[str]] = None,
                                               public_certificate_name: Optional[pulumi.Input[str]] = None,
                                               resource_group_name: Optional[pulumi.Input[str]] = None,
                                               slot: Optional[pulumi.Input[str]] = None,
                                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWebAppPublicCertificateSlotResult]:
    """
    Description for Get the named public certificate for an app (or deployment slot, if specified).


    :param str name: Name of the app.
    :param str public_certificate_name: Public certificate name.
    :param str resource_group_name: Name of the resource group to which the resource belongs.
    :param str slot: Name of the deployment slot. If a slot is not specified, the API the named binding for the production slot.
    """
    ...
