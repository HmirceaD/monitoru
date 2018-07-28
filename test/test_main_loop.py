from unittest import TestCase
from monitoru import main_loop
from unittest.mock import patch
from unittest.mock import call
from unittest.mock import MagicMock
from monitoru.create_config_file import CreateConfigFile
from monitoru.main_monitoring import MainMonitoring


class TestMainLoop(TestCase):

    def test_init_client(self):
        source_mock = MagicMock()

        with patch('monitoru.main_loop.init_config', source_mock.function1), \
             patch('monitoru.main_loop.begin_sending_packets', source_mock.function2):

            expected = [call.function1(),
                        call.function2()]

            main_loop.init_client()
            self.assertEqual(source_mock.mock_calls, expected)

    def test_init_config(self):

        with patch.object(CreateConfigFile, "check_if_config_file_exists") as mock:
            main_loop.init_config()

        mock.assert_called()

    def test_begin_sending_packets(self):

        with patch.object(MainMonitoring, "start_monitor_loop") as mock:
            main_loop.begin_sending_packets()

        mock.assert_called()