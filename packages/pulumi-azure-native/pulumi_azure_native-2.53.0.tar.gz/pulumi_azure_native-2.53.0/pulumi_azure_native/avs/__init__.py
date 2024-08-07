# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .addon import *
from .authorization import *
from .cloud_link import *
from .cluster import *
from .datastore import *
from .get_addon import *
from .get_authorization import *
from .get_cloud_link import *
from .get_cluster import *
from .get_datastore import *
from .get_global_reach_connection import *
from .get_hcx_enterprise_site import *
from .get_iscsi_path import *
from .get_placement_policy import *
from .get_private_cloud import *
from .get_script_execution import *
from .get_script_execution_logs import *
from .get_workload_network_dhcp import *
from .get_workload_network_dns_service import *
from .get_workload_network_dns_zone import *
from .get_workload_network_port_mirroring import *
from .get_workload_network_public_ip import *
from .get_workload_network_segment import *
from .get_workload_network_vm_group import *
from .global_reach_connection import *
from .hcx_enterprise_site import *
from .iscsi_path import *
from .list_cluster_zones import *
from .list_private_cloud_admin_credentials import *
from .placement_policy import *
from .private_cloud import *
from .script_execution import *
from .workload_network_dhcp import *
from .workload_network_dns_service import *
from .workload_network_dns_zone import *
from .workload_network_port_mirroring import *
from .workload_network_public_ip import *
from .workload_network_segment import *
from .workload_network_vm_group import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.avs.v20200320 as __v20200320
    v20200320 = __v20200320
    import pulumi_azure_native.avs.v20210101preview as __v20210101preview
    v20210101preview = __v20210101preview
    import pulumi_azure_native.avs.v20210601 as __v20210601
    v20210601 = __v20210601
    import pulumi_azure_native.avs.v20220501 as __v20220501
    v20220501 = __v20220501
    import pulumi_azure_native.avs.v20230301 as __v20230301
    v20230301 = __v20230301
    import pulumi_azure_native.avs.v20230901 as __v20230901
    v20230901 = __v20230901
else:
    v20200320 = _utilities.lazy_import('pulumi_azure_native.avs.v20200320')
    v20210101preview = _utilities.lazy_import('pulumi_azure_native.avs.v20210101preview')
    v20210601 = _utilities.lazy_import('pulumi_azure_native.avs.v20210601')
    v20220501 = _utilities.lazy_import('pulumi_azure_native.avs.v20220501')
    v20230301 = _utilities.lazy_import('pulumi_azure_native.avs.v20230301')
    v20230901 = _utilities.lazy_import('pulumi_azure_native.avs.v20230901')

