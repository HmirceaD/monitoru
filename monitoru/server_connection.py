"""this module contains the ServerConnection class"""
import pika


class ServerConnection:
    """Establishes the connection to
    rabbitmq server and sends data to it
    and kills the connection"""
    def __init__(self, address):
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(address))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='machine_status')

    def send_packet(self, packet):
        """sends data to the rabbitmq server
        as json objects"""
        self.channel.basic_publish(exchange='',
                                   routing_key='machine_status',
                                   body=packet)

        print("Packet sent to server : " + packet)

    def close_connection(self):
        """closes the connection to the
        rabbitmq server"""
        print("========\nExiting program")
        self.channel.close()
