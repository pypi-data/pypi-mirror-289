# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .get_multiple_activation_key import *
from .multiple_activation_key import *

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.windowsesu.v20190916preview as __v20190916preview
    v20190916preview = __v20190916preview
else:
    v20190916preview = _utilities.lazy_import('pulumi_azure_native.windowsesu.v20190916preview')

