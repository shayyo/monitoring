import psutil


def convert_byte_to_megabyte(int):
    return int / 1024 / 1024

def retrieve_memory_information():

    memory_raw_data = psutil.virtual_memory()
    total_physical_memory = convert_byte_to_megabyte(memory_raw_data.total)
    available_physical_memory = convert_byte_to_megabyte(memory_raw_data.available)
    memory_usage_percentage = memory_raw_data.percent
    physical_memory_used = convert_byte_to_megabyte(memory_raw_data.used)
    physical_memory_active = convert_byte_to_megabyte(memory_raw_data.active)
    physical_memory_inactive = convert_byte_to_megabyte(memory_raw_data.inactive)
    physical_memory_wired = convert_byte_to_megabyte(memory_raw_data.wired)
    return {
        'total_physical_memory': total_physical_memory,
        'available_physical_memory': available_physical_memory,
        'memory_usage_percentage': memory_usage_percentage,
        'physical_memory_used': physical_memory_used,
        'physical_memory_active': physical_memory_active,
        'physical_memory_inactive': physical_memory_inactive,
        'physical_memory_wired': physical_memory_wired
    }


def retrieve_cpu_information():

    global_cpu_utilization_percentage = psutil.cpu_percent()
    percpu_utilization_percentage = psutil.cpu_percent(percpu=True)
    return {
        'global_cpu_utilization_percentage': global_cpu_utilization_percentage,
        'percpu_utilization_percentage': percpu_utilization_percentage
    }

def retrieve_disk_information(path):
    raw_disk_data = psutil.disk_usage(path=path)
    total_disk_size = convert_byte_to_megabyte(raw_disk_data.total)
    used_disk_size = convert_byte_to_megabyte(raw_disk_data.used)
    free_disk_size = convert_byte_to_megabyte(raw_disk_data.free)
    percentage_used_disk_size = convert_byte_to_megabyte(raw_disk_data.percent)
    return {
        'total_disk_size': total_disk_size,
        'used_disk_size': used_disk_size,
        'free_disk_size': free_disk_size,
        'percentage_used_disk_size': percentage_used_disk_size
    }


