from pyVmomi import vim,vmodl
from vCenter_legacy import legacy


def host_hardware_warnings():
    hw_info=[]
    for cluster in legacy().get_vim_objects(legacy.content, vim.ClusterComputeResource):
        hosts = cluster.host
        for host in hosts:
            numeric_Sensor = host.runtime.healthSystemRuntime.systemHealthInfo.numericSensorInfo
            cpu_status_info = host.runtime.healthSystemRuntime.hardwareStatusInfo.cpuStatusInfo
            memory_status_info = host.runtime.healthSystemRuntime.hardwareStatusInfo.memoryStatusInfo

            for sensor in numeric_Sensor:
                if sensor.healthState.key != 'green' and sensor.healthState.key != 'unknown':
                    hw_info.append((cluster.name,host.name,sensor.name,sensor.healthState.key))

            for cpu_stat in cpu_status_info:
                if cpu_stat.status.key != 'Green' and cpu_stat.status.key != 'Unknown':
                    hw_info.append((cluster.name,host.name,cpu_stat.name,cpu_stat.status.key))

            for mem_stat in memory_status_info:
                if mem_stat.status.key != 'Green' and mem_stat.status.key != 'Unknown':
                    hw_info.append((cluster.name,host.name,mem_stat.name,mem_stat.status.key))
    return hw_info




