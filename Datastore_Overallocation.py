from vCenter_legacy import legacy
from pyVmomi import vim,vmodl

def Datastore_Overallocation():

    overallocated_datastore = []
    low_datastore = []
    datastore_list = [datastore for datastore in legacy().get_vim_objects(legacy.content,vim.Datastore)]
    for datastore in datastore_list:

        percentFree = float(datastore.summary.freeSpace)/datastore.summary.capacity * 100
        if percentFree <25:
            low_datastore.append((datastore.summary.name,datastore.summary.type,datastore.summary.capacity,datastore.summary.freeSpace,percentFree))
        if datastore.summary.uncommitted!=None:
            allocation = ((datastore.summary.capacity - datastore.summary.freeSpace+datastore.summary.uncommitted) * 100) / datastore.summary.capacity
            if allocation > 50:
                overallocated_datastore.append((datastore.summary.name,allocation))
    return overallocated_datastore,low_datastore










