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
    'CreateManagementGroupDetailsArgs',
    'CreateManagementGroupDetailsArgsDict',
    'CreateParentGroupInfoArgs',
    'CreateParentGroupInfoArgsDict',
]

MYPY = False

if not MYPY:
    class CreateManagementGroupDetailsArgsDict(TypedDict):
        """
        The details of a management group used during creation.
        """
        parent: NotRequired[pulumi.Input['CreateParentGroupInfoArgsDict']]
        """
        (Optional) The ID of the parent management group used during creation.
        """
elif False:
    CreateManagementGroupDetailsArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CreateManagementGroupDetailsArgs:
    def __init__(__self__, *,
                 parent: Optional[pulumi.Input['CreateParentGroupInfoArgs']] = None):
        """
        The details of a management group used during creation.
        :param pulumi.Input['CreateParentGroupInfoArgs'] parent: (Optional) The ID of the parent management group used during creation.
        """
        if parent is not None:
            pulumi.set(__self__, "parent", parent)

    @property
    @pulumi.getter
    def parent(self) -> Optional[pulumi.Input['CreateParentGroupInfoArgs']]:
        """
        (Optional) The ID of the parent management group used during creation.
        """
        return pulumi.get(self, "parent")

    @parent.setter
    def parent(self, value: Optional[pulumi.Input['CreateParentGroupInfoArgs']]):
        pulumi.set(self, "parent", value)


if not MYPY:
    class CreateParentGroupInfoArgsDict(TypedDict):
        """
        (Optional) The ID of the parent management group used during creation.
        """
        id: NotRequired[pulumi.Input[str]]
        """
        The fully qualified ID for the parent management group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
        """
elif False:
    CreateParentGroupInfoArgsDict: TypeAlias = Mapping[str, Any]

@pulumi.input_type
class CreateParentGroupInfoArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        (Optional) The ID of the parent management group used during creation.
        :param pulumi.Input[str] id: The fully qualified ID for the parent management group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The fully qualified ID for the parent management group.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


