"""start the loop, check config files, keep listening for commands from input,
check the config files for the things to monitor and send to rabbitmq"""

from monitoru.create_config_file import CreateConfigFile
from utils import string_resources
from monitoru.parse_arguments import ParseArguments


def start_loop():

    print(string_resources.get_main_loop_start_message())
    argument_parser = ParseArguments()

    while True is True:
        command_line_arguments = input("$>")

        if command_line_arguments != "":
            argument_parser.set_arguments(command_line_arguments)


def init_config():
    config_file = CreateConfigFile()
    config_file.check_if_config_file_exists()


def init_client():
    init_config()
    start_loop()


if __name__ == "__main__":
    init_client()
