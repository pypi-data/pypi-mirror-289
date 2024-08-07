# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .auto_scale_v_core import *
from .capacity_details import *
from .get_auto_scale_v_core import *
from .get_capacity_details import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.powerbidedicated.v20210101 as __v20210101
    v20210101 = __v20210101
else:
    v20210101 = _utilities.lazy_import('pulumi_azure_native.powerbidedicated.v20210101')

