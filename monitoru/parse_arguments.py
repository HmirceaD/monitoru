"""Parses the arguments from the command
line and takes the appropriate actions"""


class ParseArguments:
    """keeps all the supported functions to
    match with the commands the user inputs"""

    def __init__(self):
        self.supported_commands = ['help', 'stop',
                                   'reset', 'config']

    def check_command(self, argument):
        """check if the user's command mathches
        the system's supported commands"""

        for counter in range(len(self.supported_commands)):
            if self.supported_commands[counter] == argument:
                return counter

        return -1
