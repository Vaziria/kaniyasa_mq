import time
import random

from kaniyasa import Kaniyasa, RabbitCon
from kaniyasa.campaign import IklanConsumer, Akun



app = Kaniyasa()
# app.config['rabbitmq_server'] = '206.189.40.65'
app.config['rabbitmq_server'] = '192.168.1.2'
app.config['rabbitmq_user'] = 'rabbitmq'
app.config['rabbitmq_password'] = 'rabbitmq'

con = RabbitCon()
con.init_app(app)
	
channel = con.channel

class TestConsumer(IklanConsumer):
	def update_akun(self, ch, method, properties, msg):
		print("{} update akun".format(msg))

consumer = TestConsumer()


with app.create_context() as out:
	channel.queue_declare(queue='ads')
	channel.basic_consume(queue='ads',
					  on_message_callback=consumer)


	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()