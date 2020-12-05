"""library untuk mengatur microservice, Bismillah
"""
import pika
from contextlib import contextmanager

from .rabbit_con import RabbitCon



class Kaniyasa:
	config = {}
	teardown = []

	def add_teardown(self, func):
		self.teardown.append(func)

	@contextmanager
	def create_context(self):
		
		yield self

		for tear in self.teardown:
			tear()


if __name__ == '__main__':
	app = Kaniyasa()
	con = RabbitCon()
	con.init_app(app)

	with app.create_context() as out:
		print('asdasdasd')

