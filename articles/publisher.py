import pika
import json


class Publisher:
    def send(self, content):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbit"))
        channel = connection.channel()

        channel.queue_declare(queue="articles")

        channel.basic_publish(exchange="", routing_key="articles", body=content)
        print(f"Message send {content}")
        connection.close()
