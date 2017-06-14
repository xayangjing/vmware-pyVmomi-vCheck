from vCenter_legacy import legacy
from pyVmomi import vim,vmodl

def clusterConfigissue():

    config_issue = {}
    for cluster in legacy().get_vim_objects(legacy.content,vim.ClusterComputeResource):
        if cluster.configIssue():
            config_issues = cluster.configIssue()
            for issue in config_issues:
                config_issue[cluster.name].append(issue)
    return config_issue




#not yet done



