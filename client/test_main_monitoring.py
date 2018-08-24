"""Module holds unittest for the MainMonitoringClass"""
from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import call


class TestMainMonitoring(TestCase):
    """tests to see if the object that has to be sent to
    server is created prorperly and the correct functions
    are called"""
    @classmethod
    def setUpClass(cls):
        cls.main_monitoring_object = MainMonitoring()

    def test_add_metrics(self):
        """tests to see if the correct metrics are called
        given the [1,1,1,1] metrics array"""
        source_mock = MagicMock()

        with patch('monitoru.main_monitoring.MainMonitoring.cpu_percent',
                   source_mock.function1), \
                patch('monitoru.main_monitoring.MainMonitoring.cpu_freq',
                      source_mock.function2), \
                patch('monitoru.main_monitoring.MainMonitoring.ram_percent',
                      source_mock.function3), \
                patch('monitoru.main_monitoring.MainMonitoring.disk_usage',
                      source_mock.function4):

            expected = [call.function2(),
                        call.function1(),
                        call.function3(),
                        call.function4()]

            obj = MainMonitoring()
            obj.start_monitor_loop()

            self.assertEqual(source_mock.mock_calls, expected)

    def test_start_monitor_loop(self):
        """tests to see if the start_monitor_loop
        function calls the correct function"""
        with patch.object(MainMonitoring,
                          "add_metrics_to_monitor_object") as mock:
            self.main_monitoring_object.start_monitor_loop()

        mock.assert_called()

    def test_cpu_percent(self):
        """checks to see if this function
        calls the corresponding psutil function"""
        with patch('psutil.cpu_percent') as mock:
            self.main_monitoring_object.cpu_percent()

        mock.assert_called()

    def test_cpu_freq(self):
        """checks to see if this function
        calls the corresponding psutil function"""
        with patch('psutil.cpu_freq') as mock:
            self.main_monitoring_object.cpu_freq()

        mock.assert_called()

    def test_ram_percent(self):
        """checks to see if this function
        calls the corresponding psutil function"""
        with patch('psutil.virtual_memory') as mock:
            self.main_monitoring_object.ram_percent()

        mock.assert_called()

    def test_disk_usage(self):
        """checks to see if this function
        calls the corresponding psutil function"""
        with patch('psutil.disk_usage') as mock:
            self.main_monitoring_object.disk_usage()

        mock.assert_called()
