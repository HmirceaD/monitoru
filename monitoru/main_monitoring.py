"""Module that holds the MainMonitoring class"""
from threading import Timer
import json
import psutil
from monitoru.read_config_file import ConfigFileReader
from monitoru.server_connection import ServerConnection


class MainMonitoring:
    """Class that gathers the specific information about
    the machine and sends the info to a server as a json
    object converted from a python dictionary"""
    def __init__(self):
        self.config_file_reader = ConfigFileReader()
        self.communication_period = \
            self.config_file_reader.get_send_communication_time()
        self.metrics_array = self.config_file_reader.get_metrics()
        self.monitoring_object = {}
        self.monitor_functions = [self.cpu_freq,
                                  self.cpu_percent,
                                  self.ram_percent,
                                  self.disk_usage]
        self.server_connection = ServerConnection(
            address='localhost')

    def start_monitor_loop(self):
        """first gets the information from the config
        file and starts the function to start gathering info"""
        read_config_file = ConfigFileReader()

        communication_time = read_config_file.get_send_communication_time()
        metrics_array = read_config_file.get_metrics()

        self.add_metrics_to_monitor_object(communication_time, metrics_array)

    def add_metrics_to_monitor_object(self, communication_time, metrics_array):
        """calls all of the functions enabled in the config file
        and creates the object and sends the object to the through
        the connection object, then starts the timer to call after
        n seconds and calls itself again"""
        for index in range(len(metrics_array)):
            if metrics_array[index] == '1':
                self.monitor_functions[index]()

        self.server_connection.send_packet(json.dumps(
            self.monitoring_object, indent=1))

        pid = Timer(int(communication_time),
                    self.add_metrics_to_monitor_object,
                    args=(communication_time, metrics_array,))
        pid.start()

    def cpu_percent(self):
        """add to the obj the cpu usage, all cores"""
        self.monitoring_object['cpu_percent'] = \
            psutil.cpu_percent(interval=1, percpu=True)

    def cpu_freq(self):
        """add to the obj the cpu frequencies, all cores"""
        self.monitoring_object['cpu_freq'] = \
            psutil.cpu_freq(percpu=True)

    def ram_percent(self):
        """add to the obj the used ram"""
        self.monitoring_object['ram_percent'] = \
            psutil.virtual_memory().used

    def disk_usage(self):
        """add to the obj the used disk"""
        self.monitoring_object['disk_usage'] =\
            psutil.disk_usage('/')
