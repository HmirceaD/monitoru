"""module that holds the unittest for the main_loop module"""
from unittest import TestCase
from unittest.mock import patch
from unittest.mock import call
from unittest.mock import MagicMock
from client import main_loop
from client import main_monitoring


class TestMainLoop(TestCase):
    """Tests to see if the main_loop module calls
    the correct functions and has correct work flow"""

    @classmethod
    def test_init_client(cls):
        """tests to see if the begin_sending_packets function
        calls the correct function from the MainMonitoring object"""
        with patch.object(main_monitoring.MainMonitoring, "start_monitor_loop") as mock:
            main_loop.init_client()

        mock.assert_called()
