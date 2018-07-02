"""module that will be used the read
and extract the values of the config file"""

import os
import re


class ConfigFileReader:

    def __init__(self):
        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_file_path = os.path.join(self.root, 'config.txt')

    def get_send_communication_time(self):
        temp_file = open(self.config_file_path, "r")

        communication_time = re.search("communication_elapsed_time=(\d|\d\d)sec",
                                       temp_file.read())

        temp_file.close()
        return communication_time.group(1)

    def get_metrics(self):

        temp_file = open(self.config_file_path, "r")

        metrics_groups = re.search('cpu_percent=(\d)' +
                                   '\ncpu_freq=(\d)' +
                                   '\nram_percent=(\d)' +
                                   '\nfan_speed=(\d)' +
                                   '\ndisk_usage=(\d)' +
                                   '\nsystem_temperatures=(\d)', temp_file.read())

        metrics_array = [metrics_groups.group(1),
                         metrics_groups.group(2),
                         metrics_groups.group(3),
                         metrics_groups.group(4),
                         metrics_groups.group(5),
                         metrics_groups.group(6)]
        temp_file.close()

        return metrics_array
