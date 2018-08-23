"""module that holds the CreateConfigFile class"""
import configparser


class ConfigParser:

    def __init__(self, path):

        self.CONFIG = configparser.ConfigParser()

        try:
            self.CONFIG.read(path)
        except configparser.ParsingError:
            raise FileNotFoundError("The path you entered isn't correct")

    def read_requirements(self):
        try:

            character_list = self.CONFIG.get("REQUIREMENTS", "metrics")

            #config file returns the list of metrics as chars

            temp_list = ""
            for chars in character_list:
                temp_list += chars

            return temp_list.split(",")

        except configparser.MissingSectionHeaderError:
            raise ResourceWarning("The header you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoSectionError:
            raise ResourceWarning("The Section you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoOptionError:
            raise ResourceWarning("The option you specified does not exist"
                                  "\nPlease check config file for errors")

    def read_time(self):
        try:
            return self.CONFIG.get("REQUIREMENTS", "time")
        except configparser.MissingSectionHeaderError:
            raise ResourceWarning("The header you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoSectionError:
            raise ResourceWarning("The Section you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoOptionError:
            raise ResourceWarning("The option you specified does not exist"
                                  "\nPlease check config file for errors")

    def read_rabbitmq_ip(self):
        try:
            return self.CONFIG.get("RABBIT", "ip")
        except configparser.MissingSectionHeaderError:
            raise ResourceWarning("The header you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoSectionError:
            raise ResourceWarning("The Section you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoOptionError:
            raise ResourceWarning("The option you specified does not exist"
                                  "\nPlease check config file for errors")

    def read_rabbitmq_port(self):
        try:
            return self.CONFIG.get("RABBIT", "port")
        except configparser.MissingSectionHeaderError:
            raise ResourceWarning("The header you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoSectionError:
            raise ResourceWarning("The Section you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoOptionError:
            raise ResourceWarning("The option you specified does not exist"
                                  "\nPlease check config file for errors")
