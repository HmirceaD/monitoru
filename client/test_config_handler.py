"""module that holds the unittest for the ConfigHandler"""
import os
from unittest import TestCase
from client import config_handler


class TestConfigHandler(TestCase):
    """Tests if the config handler reads and returns the correct data"""
    @classmethod
    def setUpClass(cls):
        cls.test_file = open("test.txt", "w+")\
            .write("[REQUIREMENTS]\n"
                   "metrics = cpu_percent\n"
                   "time = 5\n"
                   "[RABBIT]\n"
                   "ip = localhost\n"
                   "port = 5672\n"
                   "[SERVER]\n"
                   "server_ip = localhost\n"
                   "server_port = 5500\n"
                   "[MONGO]\n"
                   "mongo_uri = db_uri\n"
                   "mongo_db = db_name\n")
        cls.test_obj = config_handler.ConfigParser("test.txt")

    @classmethod
    def tearDownClass(cls):

        os.remove("test.txt")

    def test_read_requirements(self):
        """tests read of requirements"""
        self.assertEqual(['cpu_percent'], self.test_obj.read_requirements())
        self.assertNotEqual("Dorian Popa este cel mai bun "
                            "cantaret din romania",
                            self.test_obj.read_requirements())

    def test_read_time(self):
        """tests read of time"""
        self.assertEqual('5', self.test_obj.read_time())
        self.assertNotEqual('32', self.test_obj.read_time())

    def test_read_rabbitmq_ip(self):
        """tests read of rabbitmq ip"""
        self.assertEqual('localhost', self.test_obj.read_rabbitmq_ip())
        self.assertNotEqual('nanananana batman',
                            self.test_obj.read_rabbitmq_ip())

    def test_read_rabbitmq_port(self):
        """tests read of rabbitmq port"""
        self.assertEqual('5672', self.test_obj.read_rabbitmq_port())
        self.assertNotEqual('8080', self.test_obj.read_rabbitmq_port())

    def test_read_server_ip(self):
        """tests read of server ip"""
        self.assertEqual('localhost', self.test_obj.read_server_ip())
        self.assertNotEqual('cocolino', self.test_obj.read_server_ip())

    def test_read_server_port(self):
        """tests read of server port"""
        self.assertEqual('5500', self.test_obj.read_server_port())
        self.assertNotEqual('8080', self.test_obj.read_server_port())

    def test_read_mongo_uri(self):
        """tests read of mongo_uri"""
        self.assertEqual('db_uri', self.test_obj.read_mongo_uri())
        self.assertNotEqual('cocolino', self.test_obj.read_mongo_uri())

    def test_read_mongo_db(self):
        """tests read of mongo db name"""
        self.assertEqual('db_name', self.test_obj.read_mongo_db())
        self.assertNotEqual('janel', self.test_obj.read_mongo_db())
