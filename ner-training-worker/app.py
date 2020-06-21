import pika
import yaml
import logging
import logging.config

from training_module.main import train_data

with open('./logging/log.config.yml', 'r') as log_config_file:
    log_config = yaml.load(log_config_file, Loader=yaml.FullLoader)
    logging.config.dictConfig(log_config)
logger = logging.getLogger(__name__)

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.queue_declare(queue='crf_training_queue', durable=True)
logger.info('Waiting for messages. To exit press CTRL+C')

def listenerCallback(ch, method, props, body):
    logger.info("Received message")
    
    train_data(body.decode())
    
    ch.basic_ack(delivery_tag=method.delivery_tag)
    logger.info("Acknowledged Message")

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='crf_training_queue', on_message_callback=listenerCallback)

channel.start_consuming()