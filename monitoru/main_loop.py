"""start the loop,
check the config files for the things to monitor and send to rabbitmq"""

from monitoru.create_config_file import CreateConfigFile
from monitoru.main_monitoring import MainMonitoring


def begin_sending_packets():
    """starts the loop which will
     monitor the metrics and the configured time frame"""
    monitoru = MainMonitoring()
    monitoru.start_monitor_loop()


def init_config():
    """calls the object for handling the
    creation and check of config file"""
    config_file = CreateConfigFile()
    config_file.check_if_config_file_exists()


def init_client():
    """calls the two main functions here"""
    init_config()
    begin_sending_packets()


if __name__ == "__main__":
    init_client()
