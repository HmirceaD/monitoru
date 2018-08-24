import os
from unittest import TestCase
import configparser
from client import config_handler


class TestConfigHandler(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_file = open("test.txt", "w+")\
            .write("[REQUIREMENTS]\n"
                   "metrics = cpu_percent\n"
                   "time = 5\n"
                   "[RABBIT]\n" 
                   "ip = localhost\n"
                   "port = 5672")
        cls.test_obj = config_handler.ConfigParser("test.txt")

    @classmethod
    def tearDownClass(cls):

        os.remove("test.txt")

    def test_read_requirements(self):

        self.assertEqual(['cpu_percent'], self.test_obj.read_requirements())
        self.assertNotEqual("Dorian Popa este cel mai bun "
                            "cantaret din romania", self.test_obj.read_requirements())

    def test_read_time(self):

        self.assertEqual('5', self.test_obj.read_time())
        self.assertNotEqual('32', self.test_obj.read_time())

    def test_read_rabbitmq_ip(self):
        self.assertEqual('localhost', self.test_obj.read_rabbitmq_ip())
        self.assertNotEqual('nanananana batman', self.test_obj.read_rabbitmq_ip())

    def test_read_rabbitmq_port(self):
        self.assertEqual('5672', self.test_obj.read_rabbitmq_port())
        self.assertNotEqual('8080', self.test_obj.read_rabbitmq_port())