import pkg_resources
import os
import re

config_file_structure = 'cpu_percent=1\ncpu_freq=1\nram_percent=1\nfan_speed=1\ndisk_usage=1' \
                        '\nsystem_temperatures=1\ncommunication_elapsed_time=5sec'

config_file_regex = r'cpu_percent=(0|1)\ncpu_freq=(0|1)\nram_percent=(0|1)\nfan_speed=(0|1)' \
                    r'\ndisk_usage=(0|1\nsystem_temperatures=(0|1))\ncommunication_elapsed_time=(\d|\d\d|\d\d\d)sec'

''''''

''' first we check if the config file exists, if it exists than we check
    if it has the correct structure, if it doesn't exist or isn't correct
    we recreate it with default parameters'''

def create_config_file():
    config_file = open('../config.txt', 'w')

    config_file.write(config_file_structure)


def check_file_structure():
    config_file = open('../config.txt', 'r+')

    if re.search(config_file_regex, config_file.read()):
        print('bun')
    else:
        config_file.close()
        config_file = open('../config.txt', 'w')
        config_file.write(config_file_structure)


def check_if_config_file_exists():
    if os.path.isfile('../config.txt'):
        check_file_structure()
    else:
        create_config_file()

check_if_config_file_exists()