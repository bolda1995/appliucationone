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
