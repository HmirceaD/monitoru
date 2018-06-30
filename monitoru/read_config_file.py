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


