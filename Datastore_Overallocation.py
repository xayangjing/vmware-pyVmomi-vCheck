from vCenter_legacy import legacy
from pyVmomi import vim,vmodl

def Datastore_Overallocation():

    overallocated_datastore = []
    datastore_list = [datastore for datastore in legacy().get_vim_objects(legacy.content,vim.Datastore)]
    for datastore in datastore_list:
        if datastore.summary.uncommitted!='None':
            allocation = ((datastore.summary.capacity - datastore.summary.freeSpace) * 100) / datastore.summary.capacity
            if allocation > 50:
                overallocated_datastore.append((datastore.summary.name,allocation))
    return overallocated_datastore


print Datastore_Overallocation()




