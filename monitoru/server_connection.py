import pika


class ServerConnection:
    
    def __init__(self, address):
        connection = pika.BlockingConnection(pika.ConnectionParameters(address))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='machine_status')

    def send_packet(self, packet):
        self.channel.basic_publish(exchange='',
                                   routing_key='machine_status',
                                   body=packet)

        print("Packet sent to server : " + packet)
