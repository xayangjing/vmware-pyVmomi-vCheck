from pyVim.connect import SmartConnectNoSSL, Disconnect
from pyVmomi import vim,vmodl
import getpass

class legacy:

    HOST = 'umwvcenter01.ad.umassmed.edu'
    PASSWORD = getpass.getpass('Enter password')
    PORT = 443
    USER = 'LingamaS1@ad.umassmed.edu'
    connection = SmartConnectNoSSL(host=HOST, user=USER, pwd=PASSWORD, port=PORT)
    content = connection.RetrieveContent()

    vmlist =[]
    datastore_map = {}
    datastore_list = []
    host_map = {}



    #retrieves objects in vcenter
    def get_vim_objects(self,content, vim_type):
        return [item for item in content.viewManager.CreateContainerView(
            content.rootFolder, [vim_type], recursive=True
        ).view]



    #VM information
    def getVmInfo(self,content):
        vmlist= [vm for vm in self.get_vim_objects(content, vim.VirtualMachine)  ]
        vmCount = len(vmlist)
        return vmCount,vmlist



    #datastores mapped to hosts,hosts mapped to VMs
    def datastoreMap(self,content):
        for datastore in self.get_vim_objects(content,vim.Datastore):
            self.datastore_map[datastore] = datastore.host
            for host in datastore.host:
                 self.host_map[host.key.summary.host] =host.key.vm
        return self.datastore_map,self.host_map







































