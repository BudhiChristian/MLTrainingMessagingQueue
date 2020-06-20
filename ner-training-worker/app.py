import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.queue_declare(queue='crf_training_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')

def listenerCallback(ch, method, props, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='crf_training_queue', on_message_callback=listenerCallback)

channel.start_consuming()