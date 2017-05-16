from vCenter_legacy import legacy
from pyVmomi import vim,vmodl

def incorrectOS():

    vmlist = [vm for vm in legacy().get_vim_objects(legacy().content, vim.VirtualMachine)]
    incorrectOS_count =0
    incorrectOS_vm = []

    for vm in vmlist:
        if vm.summary.config.guestId != vm.summary.guest.guestId:
            incorrectOS_count+=1
            incorrectOS_vm.append((vm.name,vm.summary.config.guestId,vm.config.guestFullName,vm.summary.guest.guestId,vm.summary.guest.guestFullName))
    return (incorrectOS_count,incorrectOS_vm)

print incorrectOS()
