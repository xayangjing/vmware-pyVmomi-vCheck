from vCenter_legacy import legacy
from pyVmomi import vim,vmodl

#includes templates
def vmtools():
    no_tools = []
    vm_tool_issues = []
    for vm in legacy().get_vim_objects(legacy().content, vim.VirtualMachine):
        if vm.summary.guest.toolsStatus!="toolsOk":
            no_tools.append((vm.name,vm.summary.guest.toolsStatus))
            vm_tool_issues.append((vm.name,vm.guest.ipAddress,vm.guest.guestFullName,vm.guest.hostName))
    return no_tools,vm_tool_issues



#network label
#vm.guest.net



