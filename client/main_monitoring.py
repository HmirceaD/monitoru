"""Module that holds the MainMonitoring class"""
from threading import Timer
import json
import atexit
import sys
from socket import gaierror
import psutil
from pika.exceptions import ConnectionClosed
from client import server_connection
from client import config_handler
import client.file_path


class MainMonitoring:
    """Class that gathers the specific information about
    the machine and sends the info to a server as a json
    object converted from a python dictionary"""
    def __init__(self):

        try:
            self.config_file_reader = \
                config_handler.ConfigParser(client.file_path.config_file_path)
        except FileNotFoundError as exp:
            print(str(exp))
            sys.exit(3)

        try:
            self.metrics_array = self.config_file_reader.read_requirements()
            self.communication_time = self.config_file_reader.read_time()
        except (ResourceWarning, ArithmeticError) as exp:
            print(str(exp))
            sys.exit(4)

        self.monitoring_object = {}

        try:
            self.server_connection = server_connection.ServerConnection(
                address=self.config_file_reader.read_rabbitmq_ip(),
                port=self.config_file_reader.read_rabbitmq_port())
        except (gaierror, ConnectionClosed, AttributeError, ResourceWarning) as exp:
            print("Something went wrong when connecting to the RabbitMq server"
                  "\n check if ip and port in the config file are correct and"
                  "\n check your internet connection"
                  "\n\n {}".format(str(exp)))
            sys.exit(5)

        atexit.register(self.server_connection.close_connection)

    def start_monitor_loop(self):
        """first gets the information from the config
        file and starts the function to start gathering info"""

        self.add_metrics_to_monitor_object(self.communication_time, self.metrics_array)

    def add_metrics_to_monitor_object(self, communication_time, metrics_array):
        """calls all of the functions enabled in the config file
        and creates the object and sends the object to the through
        the connection object, then starts the timer to call after
        n seconds and calls itself again"""

        for metric in metrics_array:
            if hasattr(self, metric):
                getattr(self, metric)()

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
