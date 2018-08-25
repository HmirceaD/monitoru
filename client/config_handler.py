"""module that holds the CreateConfigFile class"""
import configparser


class ConfigParser:

    def __init__(self, path):

        self.CONFIG = configparser.ConfigParser()

        self.CONFIG.read(path)

    def read_requirements(self):
        try:

            character_list = self.CONFIG.get("REQUIREMENTS", "metrics")

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
            time = self.CONFIG.get("REQUIREMENTS", "time")

            if time == 0:
                raise ArithmeticError("Sending period must be greater than zero")
            else:
                return time
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

    def read_server_ip(self):
        try:
            return self.CONFIG.get("SERVER", "server_ip")
        except configparser.MissingSectionHeaderError:
            raise ResourceWarning("The header you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoSectionError:
            raise ResourceWarning("The Section you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoOptionError:
            raise ResourceWarning("The option you specified does not exist"
                                  "\nPlease check config file for errors")

    def read_server_port(self):
        try:
            return self.CONFIG.get("SERVER", "server_port")
        except configparser.MissingSectionHeaderError:
            raise ResourceWarning("The header you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoSectionError:
            raise ResourceWarning("The Section you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoOptionError:
            raise ResourceWarning("The option you specified does not exist"
                                  "\nPlease check config file for errors")

    def read_mongo_uri(self):
        try:
            return self.CONFIG.get("MONGO", "mongo_uri")
        except configparser.MissingSectionHeaderError:
            raise ResourceWarning("The header you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoSectionError:
            raise ResourceWarning("The Section you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoOptionError:
            raise ResourceWarning("The option you specified does not exist"
                                  "\nPlease check config file for errors")

    def read_mongo_db(self):
        try:
            return self.CONFIG.get("MONGO", "mongo_db")
        except configparser.MissingSectionHeaderError:
            raise ResourceWarning("The header you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoSectionError:
            raise ResourceWarning("The Section you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoOptionError:
            raise ResourceWarning("The option you specified does not exist"
                                  "\nPlease check config file for errors")
