"""Object that holds all strings for easier access"""


def get_config_file_structure():
    return 'cpu_percent=1\ncpu_freq=1' \
            '\nram_percent=1' \
            '\nfan_speed=1\ndisk_usage=1' \
            '\nsystem_temperatures=1\n' \
            'communication_elapsed_time=5sec'


def get_config_file_regex():
    return r'cpu_percent=(0|1)\ncpu_freq=(0|1)' \
           r'\nram_percent=(0|1)' \
           r'\nfan_speed=(0|1)\ndisk_usage=(0|1' \
           r'\nsystem_temperatures=(0|1))' \
           r'\ncommunication_elapsed_time=' \
           r'(\d|\d\d)sec'
