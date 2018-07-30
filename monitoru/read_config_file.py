"""module that will be used the read
and extract the values of the config file"""

import os
import re


class ConfigFileReader:
    """Class for reading all of the important parts of the config file"""
    def __init__(self):
        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_file_path = os.path.join(self.root, 'config.txt')

    def get_send_communication_time(self):
        """reads and returns the elapsed communication
        time for sending packets to server"""
        temp_file = open(self.config_file_path, "r")

        communication_time = re.search(
            # master of regex
            r"communication_elapsed_time=([1-9]|[1-9][0-9])sec",
            temp_file.read())

        temp_file.close()

        try:
            return communication_time.group(1)
        except AttributeError:
            return 5

    def get_metrics(self):
        """reads and returns an array of 0 or
        1 depending on the current metrics
        we have in the config file"""
        temp_file = open(self.config_file_path, "r")

        metrics_groups = re.search(r'cpu_percent=(\d)' +
                                   r'\ncpu_freq=(\d)' +
                                   r'\nram_percent=(\d)' +
                                   r'\ndisk_usage=(\d)',
                                   temp_file.read())

        metrics_array = [metrics_groups.group(1),
                         metrics_groups.group(2),
                         metrics_groups.group(3),
                         metrics_groups.group(4)]
        temp_file.close()

        return metrics_array

    def get_server_ip(self):

        with open(self.config_file_path, "r") as temp_file:
            ip_addr = re.search(r'\nrabbitmq_ip='
                                r'(localhost|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})',
                                temp_file.read())
            return ip_addr.group(1)

    def get_server_port(self):

        with open(self.config_file_path, "r") as temp_file:
            port = re.search(r'\nrabbitmq_port=(\d{4})',
                             temp_file.read())
            return port.group(1)
