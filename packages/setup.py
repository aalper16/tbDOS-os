import toml 
from packages import sys_info, process_toml


system = {
    'OS': f'{sys_info.get_os()}',
    'Versys_infoon': f'{sys_info.get_version()}',
    'Architecture': f'{sys_info.get_type()}',
    'Processor': f'{sys_info.get_processor()}',
    'Python': f'{sys_info.get_python()}',
    'RAM Memory': f'{sys_info.get_ram()}'
}


process_toml.load_data('reg/datapack.toml', system)
