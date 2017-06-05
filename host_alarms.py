from vCenter_legacy import legacy
from pyVmomi import vim,vmodl

def host_alarms():
    alarm_info = []
    for host in legacy().get_vim_objects(legacy.content, vim.HostSystem):
        for alarm in host.declaredAlarmState:
            if alarm in host.triggeredAlarmState:
                alarm_info.append((host,alarm.key,alarm.overallStatus,alarm.time))
    return alarm_info







