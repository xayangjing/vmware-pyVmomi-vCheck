from pyVmomi import vim,vmodl
from vCenter_legacy import legacy


def lost_network_redundancy():
    for host in legacy().get_vim_objects(legacy.content, vim.HostSystem):
        for pnic in host.config.network.pnic:

# not yet done