# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AdvancedFilterOperatorType',
    'PartnerDestinationActivationState',
    'PartnerDestinationProvisioningState',
    'PartnerRegistrationVisibilityState',
]


class AdvancedFilterOperatorType(str, Enum):
    """
    The operator type used for filtering, e.g., NumberIn, StringContains, BoolEquals and others.
    """
    NUMBER_IN = "NumberIn"
    NUMBER_NOT_IN = "NumberNotIn"
    NUMBER_LESS_THAN = "NumberLessThan"
    NUMBER_GREATER_THAN = "NumberGreaterThan"
    NUMBER_LESS_THAN_OR_EQUALS = "NumberLessThanOrEquals"
    NUMBER_GREATER_THAN_OR_EQUALS = "NumberGreaterThanOrEquals"
    BOOL_EQUALS = "BoolEquals"
    STRING_IN = "StringIn"
    STRING_NOT_IN = "StringNotIn"
    STRING_BEGINS_WITH = "StringBeginsWith"
    STRING_ENDS_WITH = "StringEndsWith"
    STRING_CONTAINS = "StringContains"
    NUMBER_IN_RANGE = "NumberInRange"
    NUMBER_NOT_IN_RANGE = "NumberNotInRange"
    STRING_NOT_BEGINS_WITH = "StringNotBeginsWith"
    STRING_NOT_ENDS_WITH = "StringNotEndsWith"
    STRING_NOT_CONTAINS = "StringNotContains"
    IS_NULL_OR_UNDEFINED = "IsNullOrUndefined"
    IS_NOT_NULL = "IsNotNull"


class PartnerDestinationActivationState(str, Enum):
    """
    Activation state of the partner destination.
    """
    NEVER_ACTIVATED = "NeverActivated"
    ACTIVATED = "Activated"


class PartnerDestinationProvisioningState(str, Enum):
    """
    Provisioning state of the partner destination.
    """
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"


class PartnerRegistrationVisibilityState(str, Enum):
    """
    Visibility state of the partner registration.
    """
    HIDDEN = "Hidden"
    PUBLIC_PREVIEW = "PublicPreview"
    GENERALLY_AVAILABLE = "GenerallyAvailable"
