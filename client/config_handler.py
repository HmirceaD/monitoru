"""module that holds the CreateConfigFile class"""
import configparser


class ConfigParser:
    """Class that receives the path of the config object as parameter,
    and can read each part of the config file separately"""
    def __init__(self, path):

        self.config = configparser.ConfigParser()

        self.config.read(path)

    def read_requirements(self):
        """"Read the requirements and return them as an array"""
        try:

            character_list = self.config.get("REQUIREMENTS", "metrics")

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
        """Reads the time for sending the object to the db,
        checks if it is greater than zero"""
        try:
            time = self.config.get("REQUIREMENTS", "time")

            if time == 0:
                raise ArithmeticError("Sending period "
                                      "must be greater than zero")
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
        """Read the rabbitmq ip"""
        try:
            return self.config.get("RABBIT", "ip")
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
        """Read the rabbitmq port"""
        try:
            return self.config.get("RABBIT", "port")
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
        """Read the server ip"""
        try:
            return self.config.get("SERVER", "server_ip")
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
        """Read the server port"""
        try:
            return self.config.get("SERVER", "server_port")
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
        """Read the mongo uri"""
        try:
            return self.config.get("MONGO", "mongo_uri")
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
        """Read the mongo db name"""
        try:
            return self.config.get("MONGO", "mongo_db")
        except configparser.MissingSectionHeaderError:
            raise ResourceWarning("The header you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoSectionError:
            raise ResourceWarning("The Section you specified does not exist"
                                  "\nPlease check config file for errors")
        except configparser.NoOptionError:
            raise ResourceWarning("The option you specified does not exist"
                                  "\nPlease check config file for errors")
