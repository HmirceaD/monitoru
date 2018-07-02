import psutil
from monitoru.read_config_file import ConfigFileReader
from threading import Timer


class MainMonitoring:

    def __init__(self):
        self.config_file_reader = ConfigFileReader()
        self.communication_period = self.config_file_reader.get_send_communication_time()
        self.metrics_array = self.config_file_reader.get_metrics()
        self.monitoring_object = {}

    def start_monitor_loop(self):

        read_config_file = ConfigFileReader()

        communication_time = read_config_file.get_send_communication_time()
        metrics_array = read_config_file.get_metrics()

        self.add_metrics_to_monitor_object(communication_time, metrics_array)

    def add_metrics_to_monitor_object(self, communication_time, metrics_array):

        print(metrics_array)

        pid = Timer(int(communication_time),
                    self.add_metrics_to_monitor_object,
                    args=(communication_time, metrics_array,))
        pid.start()

    def cpu_percent(self):
        self.monitoring_object['cpu_percent'] = \
            psutil.cpu_percent(interval=1, percpu=True)

    def cpu_freq(self):
        self.monitoring_object['cpu_freq'] = \
            psutil.cpu_freq(percpu=True)

    def ram_percent(self):
        self.monitoring_object['ram_percent'] = \
            psutil.virtual_memory().used

    '''def fan_speed(self):
        self.monitoring_object['fan_speed'] = \
            psutil.sensors_fans()'''

    def disk_usage(self):
        self.monitoring_object['disk_usage'] =\
            psutil.disk_usage('/')

    '''def system_temperatures(self):
        self.monitoring_object['system_temperatures'] = \
            psutil.sensors_temperatures()'''

coi = MainMonitoring()
coi.start_monitor_loop()