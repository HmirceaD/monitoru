import psutil
from monitoru.read_config_file import ConfigFileReader


class MainMonitoring:

    def __init__(self):
        self.config_file_reader = ConfigFileReader()
        self.communication_period = self.config_file_reader.get_send_communication_time()
        self.metrics_array = self.config_file_reader.get_metrics()
        self.monitoring_object = {}

    def monitor(self):
        pass

    def cpu_percent(self):
        self.monitoring_object['cpu_percent'] = \
            psutil.cpu_percent(interval=1, percpu=True)

    def cpu_freq(self):
        self.monitoring_object['cpu_freq'] = \
            psutil.cpu_freq(percpu=True)

    def ram_percent(self):
        self.monitoring_object['ram_percent'] = \
            psutil.virtual_memory().used

    def fan_speed(self):
        self.monitoring_object['fan_speed'] = \
            psutil.sensors_fans()

    def system_temperatures(self):
        self.monitoring_object['system_temperatures'] = \
            psutil.sensors_temperatures()


