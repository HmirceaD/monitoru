"""start the loop, check config files, keep listening for commands from input,
check the config files for the things to monitor and send to rabbitmq"""

from monitoru.create_config_file import CreateConfigFile
from utils import string_resources
from monitoru.parse_arguments import ParseArguments


def config_function():
    print("config")


def reset_function():
    print("reset")


def stop_function():
    print("stop")


def help_function():
    print("help")


command_functions = [help_function, stop_function, reset_function, config_function]


def start_loop():
    """starts the loop which will listen for commands
    and monitor the metrics and the configured time frame"""
    print(string_resources.get_main_loop_start_message())
    argument_parser = ParseArguments()

    while True is True:
        command_line_arguments = input("$>")

        if command_line_arguments != "":
            result = argument_parser.check_command(command_line_arguments)
            if result != -1:
                command_functions[result]()


def init_config():
    config_file = CreateConfigFile()
    config_file.check_if_config_file_exists()


def init_client():
    init_config()
    start_loop()


if __name__ == "__main__":
    init_client()
