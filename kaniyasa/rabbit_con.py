import json
import pika


class RabbitCon:
	app = None
	connection = None
	_channel = None

	def init_app(self, app):
		self.app = app
		app.add_teardown(self.close)

		uri = app.config.get('rabbitmq_server', 'localhost')

		options = {}

		if app.config.get('rabbitmq_user'):
			options['credentials'] = pika.PlainCredentials(app.config.get('rabbitmq_user'), app.config.get('rabbitmq_password', ''))

		if app.config.get('rabbitmq_port'):
			options['port'] = app.config.get('rabbitmq_port')

		if app.config.get('rabbitmq_vhost'):
			options['virtual_host'] = app.config.get('rabbitmq_vhost')

		self.connection = pika.BlockingConnection(pika.ConnectionParameters(uri, **options))

	def close(self):
		if self.connection:
			self.connection.close()
		print('rabbit closed')

	@property
	def channel(self):
		if not self._channel:
			self._channel = self.connection.channel()

		return self._channel

	def send(self, *arg, **kwarg):
		return self.channel.basic_publish(*arg, **kwarg)