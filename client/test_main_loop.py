"""module that holds the unittest for the main_loop module"""
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import call
from unittest.mock import MagicMock


class TestMainLoop(TestCase):
    """Tests to see if the main_loop module calls
    the correct functions and has correct work flow"""
    def test_init_client(self):
        """tests to see if the init_client function
        calls the correct functions in correct order"""
        source_mock = MagicMock()

        with patch('monitoru.main_loop.init_config',
                   source_mock.function1):

            expected = call.function1()

            main_loop.init_client()
            self.assertEqual(source_mock.mock_calls, expected)

    @classmethod
    def test_init_config(cls):
        """tests to see if the init_config function
        calls the correct function from the CreateConfigFile object"""
        with patch.object(CreateConfigFile,
                          "check_if_config_file_exists") as mock:
            main_loop.init_config()

        mock.assert_called()

    @classmethod
    def test_begin_sending_packets(cls):
        """tests to see if the begin_sending_packets function
        calls the correct function from the MainMonitoring object"""
        with patch.object(MainMonitoring, "start_monitor_loop") as mock:
            main_loop.begin_sending_packets()

        mock.assert_called()
