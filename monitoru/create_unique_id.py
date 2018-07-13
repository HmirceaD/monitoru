import uuid
import platform
import stat
import os
import subprocess
import re

class CreateUniqueId:

    def __init__(self):
        self.system = platform.system()
        self.root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.filepath = os.path.join(self.root, 'unique_id.txt')

    def handle_unique_id_file(self):

        if self.check_if_file_exists() is 0:
            self.create_unique_id_file()
        else:
            self.check_file_structure()

    def check_if_file_exists(self):

        if self.system == "Windows":

            try:
                return bool(os.stat(self.filepath).st_file_attributes
                            & stat.FILE_ATTRIBUTE_HIDDEN)
            except FileNotFoundError:
                return 0

        if self.system == "Linux":

            return os.path.isfile("."+self.filepath)

    def create_unique_id_file(self):
        unique_id = uuid.uuid4()

        if self.system == "Linux":
            unique_id_file = open("."+self.filepath, "w")
            unique_id_file.write("<Don't overwrite this, stupid>"
                                 "\n{}"
                                 "\n</Don't overwrite this, stupid>"
                                 .format(unique_id))
            unique_id_file.close()
        if self.system == "Windows":
            open(self.filepath, "w")\
                .write("<Don't overwrite this, stupid>"
                       "\n{}"
                       "\n</Don't overwrite this, stupid>"
                       .format(unique_id))
            subprocess.check_call(["attrib", "+H", self.filepath])

    def get_unique_id_from_file(self):
        unique_id_file = open(self.filepath, "r")
        regex = "[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}"

        unique_id_result = re.findall(regex, unique_id_file.read())
        unique_id_file.close()
        return unique_id_result

    def check_file_structure(self):

        unique_id_result = self.get_unique_id_from_file()

        if unique_id_result is None or len(unique_id_result) != 1:

            self.create_unique_id_file()

