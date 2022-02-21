#!/usr/bin/env python
import pika, sys, os
import json

from init import app
from worker import NotificationWorker

worker = NotificationWorker()


def main():
    with app.app_context():
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbit"))
        channel = connection.channel()

        channel.queue_declare(queue="hello")

        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)
            worker.process(json.loads(body))

        channel.basic_consume(
            queue="articles", on_message_callback=callback, auto_ack=True
        )

        print(" [*] Waiting for messages. To exit press CTRL+C")
        channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
