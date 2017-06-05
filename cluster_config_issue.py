from vCenter_legacy import legacy
from pyVmomi import vim,vmodl

def clusterConfigissue():
    config_issue={}
    for cluster in legacy().get_vim_objects(legacy.content,vim.ClusterComputeResource):
        config_issue[cluster.name] = cluster.configIssue()
    return config_issue

#not yet done