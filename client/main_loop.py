"""start the loop,
check the config files for the things to monitor and send to rabbitmq"""

import sys
import os
import client.file_path
from client import main_monitoring


def init_client():
    """starts the loop which will
     monitor the metrics and the configured time frame"""

    client.file_path.init()

    try:
        if os.path.isfile(sys.argv[1]):
            monitoru = main_monitoring.MainMonitoring(sys.argv[1])
            monitoru.start_monitor_loop()
        else:
            print("You did not enter a correct config file")
            sys.exit(1)
    except IndexError:
        print("You must enter a config file")
        sys.exit(2)


