import unittest
from monitoru.read_config_file import ConfigFileReader


class TestReadConfigFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.read_config_file = ConfigFileReader()

    def test_get_send_communication_time(self):

        self.assertEqual(self.read_config_file.get_send_communication_time(), "5")
        self.assertNotEqual(self.read_config_file.get_send_communication_time(), "6969")
