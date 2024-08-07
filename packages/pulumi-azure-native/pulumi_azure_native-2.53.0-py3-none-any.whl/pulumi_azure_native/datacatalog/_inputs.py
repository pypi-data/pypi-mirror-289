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
from ._enums import *

__all__ = [
    'PrincipalsArgs',
    'PrincipalsArgsDict',
]

MYPY = False

if not MYPY:
    class PrincipalsArgsDict(TypedDict):
        """
        User principals.
        """
        object_id: NotRequired[pulumi.Input[str]]
        """
        Object Id for the user
        """
        upn: NotRequired[pulumi.Input[str]]
        """
        UPN of the user.
        """
elif False:
    PrincipalsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class PrincipalsArgs:
    def __init__(__self__, *,
                 object_id: Optional[pulumi.Input[str]] = None,
                 upn: Optional[pulumi.Input[str]] = None):
        """
        User principals.
        :param pulumi.Input[str] object_id: Object Id for the user
        :param pulumi.Input[str] upn: UPN of the user.
        """
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)
        if upn is not None:
            pulumi.set(__self__, "upn", upn)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[str]]:
        """
        Object Id for the user
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter
    def upn(self) -> Optional[pulumi.Input[str]]:
        """
        UPN of the user.
        """
        return pulumi.get(self, "upn")

    @upn.setter
    def upn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "upn", value)


