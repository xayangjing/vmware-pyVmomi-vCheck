from vCenter_legacy import legacy
from pyVmomi import vim,vmodl

def drs_rules():

    rule_type=''
    drs_rule = []

    for cluster in legacy().get_vim_objects(legacy.content, vim.ClusterComputeResource):
        for rule in cluster.configuration.rule:
            vms = []
            rule_spec_type = str(type(rule))[1:-1].split(" ")[1].split('.')[4][0:-1]
            if rule_spec_type == 'AntiAffinityRuleSpec':
                rule_type = 'VMAntiAffinity'
            if rule_spec_type == 'AffinityRuleSpec':
                rule_type = 'VMAffinity'
            if rule_spec_type == 'VmHostRuleInfo':
                rule_type = 'VMHostAffinity'
            if rule_type is not 'VMHostAffinity':
                vms = rule.vm

            enabled = rule.enabled
            cluster_name = cluster.name
            rule_name = rule.name
            drs_rule.append((cluster_name, enabled, rule_name, rule_type, vms))

    return drs_rule


print drs_rules()


#not yet done




# hosts = cluster.host
# vms = []
# for host in hosts:
#     vms.append(host.vm)
# for obj in vms:
#
#     info = {}
#     for vm in obj:
#         host_list = []
#         vm_list = []
#         if cluster.FindRulesForVm(vm):
#             rule = cluster.FindRulesForVm(vm)[0]
#             info['enabled'] = rule.enabled
#             if type(rule) is vim.cluster.AntiAffinityRuleSpec:
#                 info['rule_type'] = 'VMAntiAffinity'
#             if type(rule) is vim.cluster.AffinityRuleSpec:
#                 info['rule_type'] = 'VMAffinity'
#             info['cluster_name'] = cluster.name
#             vm_list.append([rule_vm.name for rule_vm in rule.vm])
#             info['vm'] = vm_list
#             for item in rule.vm:
#                 host_list.append(item.runtime.host.name)
#             info['running_host'] = host_list
#             rule_info[str(rule.name)] = info  # assuming rule names are unique
# return rule_info








