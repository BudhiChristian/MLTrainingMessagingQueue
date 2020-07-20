from os import environ
import pika
import logging

class Messenger():
    def __init__(self, config):
        self.logger = logging.getLogger(__name__)
        
        # Check environment for host
        env_host = environ.get('RABBITMQ_HOST')
        self.logger.info("RABBITMQ_HOST={}".format(env_host))

        # Setup up connection params using config
        self.connection_params = pika.ConnectionParameters(
            host=config['host'] if env_host is None else env_host, # if there is no host env variable  use config file
            blocked_connection_timeout=config['connectionTimeout'],
            heartbeat=config['heartbeat']
        )
        self.logger.info(self.connection_params.host)
        self.queue_name = config['queueName']
        self.exchange_name = config['exchangeName']
        self.exchange_routing_keys = config['exchangeRoutingKeys']

    def start(self, callback=None):
        with pika.BlockingConnection( self.connection_params ) as connection:
            # Connection to a channel
            channel = connection.channel()

            # Ensuring exchange exisits
            channel.exchange_declare(exchange=self.exchange_name exchange_type='topic', durable=True)

            # Ensuring queue exists
            channel.queue_declare(queue=self.queue_name, durable=True)

            # Binding queue to exchange
            for key in self.exchange_routing_keys:
                channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key=key)

            # Only allow one fetch at a time time to distribute job where available
            channel.basic_qos(prefetch_count=1)
            
            # Wrap callback to acknowledge complete when training complete
            def wrapped_callback(ch, method, props, body):
                self.logger.info("Received message")
                
                # callback
                if callback == None:
                    self.logger.warn("Callback was not defined")
                else:
                    callback(body.decode())
                
                # acknowledgement of completion
                ch.basic_ack(delivery_tag=method.delivery_tag)
                self.logger.info("Acknowledged Message")

            # add callback
            channel.basic_consume(queue=self.queue_name, on_message_callback=wrapped_callback)

            self.logger.info('Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()