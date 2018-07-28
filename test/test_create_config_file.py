"""unit test for checking if the create_config_file module works properly
currently testing if the create file function creates file correctly
and if check file function returns correct results"""

import unittest
import os
from monitoru.create_config_file import CreateConfigFile
from utils import string_resources


class TestCreateConfigFile(unittest.TestCase):

    def setUp(self):

        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_file_path = os.path.join(self.root, 'config.txt')

        self.config_file_structure = string_resources.get_config_file_structure()

        self.config_file = open(self.config_file_path, 'r+')

        self.test_module = CreateConfigFile()

    def tearDown(self):
        self.config_file.close()

    def test_check_file_structure(self):
        """"checks check_file_structure function if it returns correct result
        under certain circumstances"""
        self.config_file.write(string_resources.get_config_file_structure())
        self.assertEqual(self.test_module.check_file_structure(), True)
        self.config_file.close()

        self.config_file = open(self.config_file_path, 'w')

        self.config_file.close()

        self.assertEqual(self.test_module.check_file_structure(), False)

    def test_create_config_file(self):
        """"checks create_config_file function and if it creates
        file and writes correct structure"""
        self.test_module.create_config_file()

        self.assertEqual(os.path.exists(self.config_file_path), 1)
        self.assertEqual(self.config_file.read(), self.config_file_structure)
