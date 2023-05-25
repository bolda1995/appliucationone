import logging
import pika

# establish connection with RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# create a queue if it doesn't already exist
channel.queue_declare(queue='my_queue')

# send a message to the queue
message = 'Hello, world!'
channel.basic_publish(exchange='', routing_key='my_queue', body=message)

# close the connection
connection.close()

# set up logging configuration
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# use logging functions to log messages
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
