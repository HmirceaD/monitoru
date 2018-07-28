"""module that contains the unittest for CreateUniqueId"""
from unittest import TestCase
from os import remove
from os.path import isfile
from monitoru import create_unique_id


class TestCreateUniqueId(TestCase):
    """tests functions from the CreateUniqueId class,
    specifically the function that tests wether the file
    exists or not, the function that creates the file,
    and the function that extracts the unique id from the file"""
    @classmethod
    def setUpClass(cls):
        """create the file path depending on the os that the
        program in run on"""
        cls.create_unique_id = create_unique_id.CreateUniqueId()

        if cls.create_unique_id.system == "Windows":
            cls.system_file_path = cls.create_unique_id.windows_filepath
        else:
            cls.system_file_path = cls.create_unique_id.linux_filepath

    def test_check_if_file_exists(self):
        """tests the function when the file exists and
        when it does not"""
        try:
            remove(self.system_file_path)
        except FileNotFoundError:
            pass

        self.assertEqual(self.create_unique_id.check_if_file_exists(), 0)

        self.create_unique_id.create_unique_id_file()

        self.assertEqual(self.create_unique_id.check_if_file_exists(), 1)

    def test_get_unique_id_from_file(self):
        """hardcodes an incorrect unique id and then a
        correct one and checks the outputs"""
        try:
            remove(self.system_file_path)
        except FileNotFoundError:
            pass

        temp_unique_id_file = open(self.system_file_path, "w")

        temp_unique_id_file.write("<Don't overwrite this, stupid>"
                                  "\n6d18a"
                                  "\n</Don't overwrite this, stupid>")
        temp_unique_id_file.close()

        self.assertEqual(self.create_unique_id.get_unique_id_from_file(), None)

        temp_unique_id_file = open(self.system_file_path, "w")

        temp_unique_id_file.write("<Don't overwrite this, stupid>"
                                  "\n6d180df9-bf98-47dc-b85f-fd379f4cd4ba"
                                  "\n</Don't overwrite this, stupid>")
        temp_unique_id_file.close()

        self.assertEqual(self.create_unique_id.get_unique_id_from_file(),
                         "6d180df9-bf98-47dc-b85f-fd379f4cd4ba")

        self.assertNotEqual(self.create_unique_id.get_unique_id_from_file(),
                            "zile guta")
        self.assertNotEqual(self.create_unique_id.get_unique_id_from_file(),
                            "bf98-47dc")

        self.assertNotEqual(self.create_unique_id.get_unique_id_from_file(),
                            "f98-47dc-b85f-fd37")

        self.assertNotEqual(self.create_unique_id.get_unique_id_from_file(),
                            "b85f-fd379f4cd")

    def test_create_unique_id_file(self):
        """checks if the file is created after
        was deleted"""
        try:
            remove(self.system_file_path)
        except FileNotFoundError:
            pass
        finally:
            self.assertNotEqual(isfile(self.system_file_path), True)
            self.create_unique_id.create_unique_id_file()

        self.assertEqual(isfile(self.system_file_path), True)
