# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Workload',
]


class Workload(str, Enum):
    """
    The workload type of the subscription. It can be either Production or DevTest.
    """
    PRODUCTION = "Production"
    DEV_TEST = "DevTest"
