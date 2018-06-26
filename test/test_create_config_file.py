import unittest
import os
import sys
from monitoru import create_config_file as test_module


class TestCreateConfigFile(unittest.TestCase):

    def setUp(self):

        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.config_file_path = os.path.join(self.root, 'config.txt')

        self.config_file_structure = 'cpu_percent=1\ncpu_freq=1\nram_percent=1\nfan_speed=1\ndisk_usage=1' \
                                     '\nsystem_temperatures=1\ncommunication_elapsed_time=5sec'

        self.config_file = open(self.config_file_path, 'r+')

    def tearDown(self):
        self.config_file.close()

    def test_check_file_structure(self):
        #test_module.create_config_file(self.config_file_path)

        self.assertEqual(test_module.check_file_structure(), True)
        self.config_file.close()

        self.config_file = open(self.config_file_path, 'w')
        self.config_file.close()

        self.assertEqual(test_module.check_file_structure(), False)

    def test_create_config_file(self):
        test_module.create_config_file()

        self.assertEqual(os.path.exists(self.config_file_path), 1)
        self.assertEqual(self.config_file.read(), self.config_file_structure)


if __name__ == '__main__':
    unittest.main()
