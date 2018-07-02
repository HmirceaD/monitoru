import unittest
from monitoru.read_config_file import ConfigFileReader
import os


class TestReadConfigFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.read_config_file = ConfigFileReader()
        cls.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        cls.config_file_path = os.path.join(cls.root, "config.txt")

    def test_get_send_communication_time(self):

        self.assertEqual(self.read_config_file.get_send_communication_time(), "5")
        self.assertNotEqual(self.read_config_file.get_send_communication_time(), "6969")

    def test_get_metrics(self):
        """checks if the read config file path reads the data"""
        self.test_config_file = open(self.config_file_path, "r+")
        self.test_config_file.truncate(0)
        self.test_config_file.write('cpu_percent=1\ncpu_freq=0' +
                                    '\nram_percent=1' +
                                    '\ndisk_usage=1' +
                                    '\ncommunication_elapsed_time=5sec')
        self.test_config_file.close()

        self.assertEqual(self.read_config_file.get_metrics(), ['1', '0', '1', '1'])

        self.test_config_file = open(self.config_file_path, "r+")
        self.test_config_file.truncate(0)
        self.test_config_file.write('cpu_percent=0\ncpu_freq=0' +
                                    '\nram_percent=0' +
                                    '\ndisk_usage=0' +
                                    '\ncommunication_elapsed_time=5sec')
        self.test_config_file.close()

        self.assertEqual(self.read_config_file.get_metrics(), ['0', '0', '0', '0'])
        self.assertNotEqual(self.read_config_file.get_metrics(), ['0', '0', '1', '1'])
