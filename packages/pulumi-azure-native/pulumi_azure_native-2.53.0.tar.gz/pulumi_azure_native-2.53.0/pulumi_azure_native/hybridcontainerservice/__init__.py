# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .agent_pool import *
from .get_agent_pool import *
from .get_hybrid_identity_metadatum import *
from .get_provisioned_cluster import *
from .get_storage_space_retrieve import *
from .get_virtual_network_retrieve import *
from .hybrid_identity_metadatum import *
from .provisioned_cluster import *
from .storage_space_retrieve import *
from .virtual_network_retrieve import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.hybridcontainerservice.v20220501preview as __v20220501preview
    v20220501preview = __v20220501preview
    import pulumi_azure_native.hybridcontainerservice.v20220901preview as __v20220901preview
    v20220901preview = __v20220901preview
    import pulumi_azure_native.hybridcontainerservice.v20231115preview as __v20231115preview
    v20231115preview = __v20231115preview
    import pulumi_azure_native.hybridcontainerservice.v20240101 as __v20240101
    v20240101 = __v20240101
else:
    v20220501preview = _utilities.lazy_import('pulumi_azure_native.hybridcontainerservice.v20220501preview')
    v20220901preview = _utilities.lazy_import('pulumi_azure_native.hybridcontainerservice.v20220901preview')
    v20231115preview = _utilities.lazy_import('pulumi_azure_native.hybridcontainerservice.v20231115preview')
    v20240101 = _utilities.lazy_import('pulumi_azure_native.hybridcontainerservice.v20240101')

