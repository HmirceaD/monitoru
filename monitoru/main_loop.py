"""start the loop, check config files, keep listening for commands from input,
check the config files for the things to monitor and send to rabbitmq"""

from monitoru.create_config_file import CreateConfigFile
from utils import string_resources
from monitoru.parse_arguments import ParseArguments
from exceptions.reset_exception import ResetLoopException
from exceptions.stop_exception import StopLoopException
import os


def config_function():
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print("Location of config file is : '" +
          os.path.join(root, 'config.txt') + "'")


def reset_function():
    raise ResetLoopException


def stop_function():
    raise StopLoopException


def help_function():
    print(string_resources.get_main_loop_help_message())


command_functions = [help_function, stop_function, reset_function, config_function]


def start_loop():
    """starts the loop which will listen for commands
    and monitor the metrics and the configured time frame"""
    print(string_resources.get_main_loop_start_message())
    argument_parser = ParseArguments()

    try:
        while True is True:
            command_line_arguments = input("$>")

            if command_line_arguments != "":
                result = argument_parser.check_command(command_line_arguments)
                if result != -1:
                    command_functions[result]()

    except StopLoopException:
        print("\nProgram stopped")
    except ResetLoopException:
        print("\nProgram reset")
        init_client()


def init_config():
    config_file = CreateConfigFile()
    config_file.check_if_config_file_exists()


def init_client():
    init_config()
    start_loop()


if __name__ == "__main__":
    init_client()
