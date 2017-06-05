from vCenter_legacy import legacy
from pyVmomi import vim,vmodl

def incorrect_HostName():
    for host in legacy().get_vim_objects(legacy.content,vim.HostSystem):


# not yet done