from pyVim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim,vmodl
from vCenter_legacy import legacy

legacy_env = legacy()

hostCount = len(legacy_env.get_vim_objects(legacy_env.content,vim.HostSystem))
vmCount = legacy_env.getVmInfo(legacy_env.content)
datastoreCount = len(legacy_env.datastore_map.keys())
templateCount = [vm for vm in legacy_env.get_vim_objects(legacy_env.content, vim.VirtualMachine) if vm.config.template ]
