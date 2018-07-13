"""Module that holds the CreateUniqueId class"""
import uuid
import platform
import stat
import os
import subprocess
import re


class CreateUniqueId:
    """This class checks if there exists a hidden file
    containing a unique id as a root element for
    the json packet sent to the server, it also
    creates it if it doesn't already exist,
    if it does exists than it checks
    if it has a correct id"""
    def __init__(self):
        self.system = platform.system()
        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.windows_filepath = os.path.join(self.root, 'unique_id.txt')
        self.linux_filepath = os.path.join(self.root, '.unique_id.txt')

    def handle_unique_id_file(self):
        """checks to see whether the file
        exists or not and calls the according
        function"""
        if self.check_if_file_exists() is 0:
            self.create_unique_id_file()
        else:
            self.check_file_structure()

    def check_if_file_exists(self):
        """checks if the unique id file exists
        for windows and for linux"""
        if self.system == "Windows":

            try:
                return bool(os.stat(self.windows_filepath).st_file_attributes
                            & stat.FILE_ATTRIBUTE_HIDDEN)
            except FileNotFoundError:
                return 0

        if self.system == "Linux":

            return os.path.isfile(self.linux_filepath)

    def create_unique_id_file(self):
        """creates the file on windows or linux
        and makes it hidden, also creates the
        unique id"""
        unique_id = uuid.uuid4()

        if self.system == "Linux":
            unique_id_file = open("." + self.linux_filepath, "w")
            unique_id_file.write("<Don't overwrite this, stupid>"
                                 "\n{}"
                                 "\n</Don't overwrite this, stupid>"
                                 .format(unique_id))
            unique_id_file.close()
        if self.system == "Windows":
            open(self.windows_filepath, "w")\
                .write("<Don't overwrite this, stupid>"
                       "\n{}"
                       "\n</Don't overwrite this, stupid>"
                       .format(unique_id))
            subprocess.check_call(["attrib", "+H", self.windows_filepath])

    def get_unique_id_from_file(self):
        """extracts the unique id from the file"""

        if self.system == "Windows":
            unique_id_file = open(self.windows_filepath, "r")
        else:
            unique_id_file = open(self.linux_filepath, "r")

        regex = "[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}"

        unique_id_result = re.findall(regex, unique_id_file.read())
        unique_id_file.close()
        return unique_id_result

    def check_file_structure(self):
        """checks if the unique id exists
        and if it is the correct structure"""
        unique_id_result = self.get_unique_id_from_file()

        if unique_id_result is None or len(unique_id_result) != 1:

            self.create_unique_id_file()
