import pickle
from .msg import Msg

class Consumer:

	def __call__(self, ch, method, properties, body):
		msg = pickle.loads(body)
		event = msg.action


		func = getattr(self, event, self.on_default)
		func(ch, method, properties, msg)

		self.ack(ch, method)

	def send_to_db(self, ch, action, data, *arg, **kwarg):
		
		msg = Msg(action, data)
		ch.basic_publish(exchange = '', routing_key = 'database', body = msg.serialize(),  *arg, **kwarg)

	def on_default(self, ch, method, properties, msg):
		print('{} received'.format(msg))


	def ack(self, ch, method):
		ch.basic_ack(delivery_tag = method.delivery_tag)



