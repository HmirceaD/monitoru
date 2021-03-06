"""module holds the unitttest for the ReadConfigFile class"""
import unittest
import os
from utils import string_resources
from monitoru.read_config_file import ConfigFileReader


class TestReadConfigFile(unittest.TestCase):
    """tests if all the the parameters from the
    config file are read correctly"""
    @classmethod
    def setUpClass(cls):
        cls.read_config_file = ConfigFileReader()
        cls.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cls.config_file_path = os.path.join(cls.root, "config.txt")

    def test_get_send_communication(self):
        """checks to see if the get_send_communication_time function
        returns the correct communication time"""
        self.assertEqual(
            self.read_config_file.get_send_communication_time(), "5")

        self.assertNotEqual(
            self.read_config_file.get_send_communication_time(), "6969")

    def test_get_metrics(self):
        """checks if the read config file path reads the data"""
        test_config_file = open(self.config_file_path, "r+")
        test_config_file.truncate(0)
        test_config_file.write('cpu_percent=1\ncpu_freq=0' +
                               '\nram_percent=1' +
                               '\ndisk_usage=1' +
                               '\ncommunication_elapsed_time=5sec')
        test_config_file.close()

        self.assertEqual(
            self.read_config_file.get_metrics(), ['1', '0', '1', '1'])

        test_config_file = open(self.config_file_path, "r+")
        test_config_file.truncate(0)
        test_config_file.write('cpu_percent=0\ncpu_freq=0' +
                               '\nram_percent=0' +
                               '\ndisk_usage=0' +
                               '\ncommunication_elapsed_time=5sec')
        test_config_file.close()

        self.assertEqual(
            self.read_config_file.get_metrics(), ['0', '0', '0', '0'])
        self.assertNotEqual(
            self.read_config_file.get_metrics(), ['0', '0', '1', '1'])

    def test_get_server_ip(self):
        """test get_server_ip if it returns
        correct ip as a string"""
        with open(self.config_file_path, "w") as temp_file:
            temp_file.write(string_resources.get_config_file_structure())

        self.assertEqual(
            self.read_config_file.get_server_ip(), 'localhost')
        self.assertNotEqual(
            self.read_config_file.get_server_ip(), 'muiepsd')
        self.assertNotEqual(
            self.read_config_file.get_server_ip(), 'daddylapuscarie')

    def test_get_server_port(self):
        """test get_server_port if it returns
        correct port as a string"""
        with open(self.config_file_path, "w") as temp_file:
            temp_file.write(string_resources.get_config_file_structure())

        self.assertEqual(self.read_config_file.get_server_port(), '5672')
        self.assertNotEqual(self.read_config_file.get_server_port(), '420')
        self.assertNotEqual(self.read_config_file.get_server_port(), '1337')
