from pyVmomi import vim,vmodl
from vCenter_legacy import legacy


def drs_migrations():
    for cluster in legacy().get_vim_objects(legacy.content, vim.ClusterComputeResource):
        if cluster.migrationHistory:
            return cluster.migrationHistory






