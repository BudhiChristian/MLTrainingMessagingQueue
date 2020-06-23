import pika
import logging

class Messenger():
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)

        self.connection_params = pika.ConnectionParameters(
            host=config['host'],
            blocked_connection_timeout=config['connectionTimeout'],
            heartbeat=config['heartbeat']
        )
        
    def start(self, callback):
        with pika.BlockingConnection( self.connection_params ) as connection:
            channel = connection.channel()

            channel.queue_declare(queue='crf_training_queue', durable=True)
            self.logger.info('Waiting for messages. To exit press CTRL+C')

            def wrapped_callback(ch, method, props, body):
                self.logger.info("Received message")

                callback(body.decode())
                
                ch.basic_ack(delivery_tag=method.delivery_tag)
                self.logger.info("Acknowledged Message")

            channel.basic_qos(prefetch_count=1)
            channel.basic_consume(queue='crf_training_queue', on_message_callback=wrapped_callback)

            channel.start_consuming()