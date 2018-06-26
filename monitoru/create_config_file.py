""" first we check if the config file exists, if it
    exists than we check
    if it has the correct structure, if it does, do nothing,
    if it doesn't exist or isn't correct
    we recreate it with default parameters"""

import os
import re
from utils import string_resources


class CreateConfigFile:

    def __init__(self):

        self.config_file_structure = string_resources.get_config_file_structure()

        self.config_file_regex = string_resources.get_config_file_regex()

        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_file_path = os.path.join(self.root, 'config.txt')

    def create_config_file(self):
        config_file = open(self.config_file_path, 'w')

        config_file.write(self.config_file_structure)
        config_file.close()

    def check_file_structure(self):
        config_file = open(self.config_file_path, 'r')

        if re.search(self.config_file_regex, config_file.read()) is None:
            config_file.close()
            return False

        config_file.close()
        return True

    def check_if_config_file_exists(self):

        if os.path.isfile(self.config_file_path):

            if self.check_file_structure() is False:
                config_file = open('../config.txt', 'w')
                config_file.write(self.config_file_structure)
                config_file.close()

        else:
            self.create_config_file()
