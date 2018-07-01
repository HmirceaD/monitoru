"""start the loop,
check the config files for the things to monitor and send to rabbitmq"""

from monitoru.create_config_file import CreateConfigFile


def start_loop():
    """starts the loop which will
     monitor the metrics and the configured time frame"""



def init_config():
    config_file = CreateConfigFile()
    config_file.check_if_config_file_exists()


def init_client():
    init_config()
    start_loop()


if __name__ == "__main__":
    init_client()
