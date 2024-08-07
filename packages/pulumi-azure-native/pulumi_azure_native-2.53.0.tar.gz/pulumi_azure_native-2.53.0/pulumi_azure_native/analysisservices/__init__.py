# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .get_server_details import *
from .list_server_gateway_status import *
from .server_details import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.analysisservices.v20170801 as __v20170801
    v20170801 = __v20170801
    import pulumi_azure_native.analysisservices.v20170801beta as __v20170801beta
    v20170801beta = __v20170801beta
else:
    v20170801 = _utilities.lazy_import('pulumi_azure_native.analysisservices.v20170801')
    v20170801beta = _utilities.lazy_import('pulumi_azure_native.analysisservices.v20170801beta')

