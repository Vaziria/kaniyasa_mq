from kaniyasa import Kaniyasa, RabbitCon


app = Kaniyasa()
app.config['rabbitmq_server'] = '206.189.40.65'
# app.config['rabbitmq_user'] = 'rabbitmq'
# app.config['rabbitmq_password'] = 'rabbitmq'

con = RabbitCon()
con.init_app(app)

channel = con.channel





def callback(ch, method, properties, body):
	print(" [x] Received %r" % body)




with app.create_context() as out:
	channel.queue_declare(queue='examples')
	channel.basic_consume(queue='examples',
					  auto_ack=True,
					  on_message_callback=callback)


	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()