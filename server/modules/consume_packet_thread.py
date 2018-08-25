"""module that holds the ConsumePacketThread class"""
from threading import Thread
import json
import pika
from server.modules.database_manager import DatabaseHandler


class ConsumePacketThread(Thread):
    """class creates a separate thread that listens for
    the packets from the rabbitmq server"""
    def __init__(self, app, config_manager):
        Thread.__init__(self)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(config_manager.read_rabbitmq_ip(),
                                      config_manager.read_rabbitmq_port()))

        self.channel = connection.channel()
        self.channel.queue_declare(queue='machine_status')
        self.app = app
        self.database_manager = DatabaseHandler(self.app)

    def packet_callback(self, blocking_channel, method, properties, body):
        """consumes the sent packet and sends it to db"""
        print("Consumed {}".format(body))
        print(str(blocking_channel))
        print(str(method))
        print(str(properties))
        self.database_manager.add_packet(json.loads(body))

    def run(self):
        """stars to listen in the packet queue"""
        self.channel.basic_consume(self.packet_callback,
                                   queue='machine_status',
                                   no_ack=True)
        print("START LISTENING")
        self.channel.start_consuming()
