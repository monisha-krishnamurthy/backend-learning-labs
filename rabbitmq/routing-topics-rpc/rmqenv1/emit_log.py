#to broadcast messages to many users
import pika
import sys

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')    #name of the exchange is logs

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)   #no queue is bound to the exchange yet
print(" [x] Sent %r" % message)
connection.close()