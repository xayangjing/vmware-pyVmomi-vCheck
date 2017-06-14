from vCenter_legacy import legacy
from pyVmomi import vim,vmodl
import socket

def incorrect_HostName():
    for host in legacy().get_vim_objects(legacy.content,vim.HostSystem):
        if host.name != socket.gethostbyaddr(host.)

# not yet done
incorrect_HostName()