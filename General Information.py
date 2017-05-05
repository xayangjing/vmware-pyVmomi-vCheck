from pyVim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim,vmodl
from vCenter_legacy import legacy

legacy_env = legacy()

hostCount = len(legacy_env.get_vim_objects(legacy_env.content,vim.HostSystem))
vmCount = legacy_env.getVmInfo(legacy_env.content)[0]
datastoreCount = legacy_env.datastore_map.keys()
templateCount = len([vm for vm in legacy_env.getVmInfo(legacy_env.content)[1] if vm.config.template ])
active_vm = len([vm for vm in legacy_env.getVmInfo(legacy_env.content)[1] if vm.summary.runtime.powerState == 'poweredOn'])
inactive_vm = len([vm for vm in legacy_env.getVmInfo(legacy_env.content)[1] if not vm.summary.runtime.powerState == 'poweredOn'])

print hostCount
print vmCount
print datastoreCount
print templateCount
print active_vm
print inactive_vm
