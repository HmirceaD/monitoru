"""Object that holds all strings for easier access"""


def get_config_file_structure():
    """returns structure of default
    structure of the file as string"""
    return 'cpu_percent=1\ncpu_freq=1' \
           '\nram_percent=1' \
           '\ndisk_usage=1' \
           '\ncommunication_elapsed_time=5sec' \
           '\nrabbitmq_ip=localhost' \
           '\nrabbitmq_port=5672'


def get_config_file_regex():
    """returns the regex for checking
    the file structure"""
    return r'cpu_percent=(0|1)\ncpu_freq=(0|1)' \
           r'\nram_percent=(0|1)' \
           r'\ndisk_usage=(0|1)' \
           r'\ncommunication_elapsed_time=' \
           r'([1-9]|[1-9][0-9])sec' \
           r'\nrabbitmq_ip=(localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' \
           r'\nrabbitmq_port=(\d{1,5})'
