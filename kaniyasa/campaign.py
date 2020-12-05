import abc
import pickle
from datetime import datetime
from dataclasses import dataclass, asdict

from .consumer import Consumer
from .base_model import BaseModel
from .msg import Msg




@dataclass
class Akun(BaseModel):
	id: int
	name: str
	email: str
	token: str



@dataclass
class AddAcount(BaseModel):

	"""struktur data untuk ads account
	"""
	
	id: str
	name: str
	created: datetime

	


@dataclass
class Campaign(BaseModel):

	"""struktur data untuk Campaign
	"""
	
	id: str
	adaccount_id: str
	effective_status: str
	name: str
	objective: str
	tax: int
	amount: int
	owner_id: int
	created: datetime


class IklanProducer:
	con = None
	def __init__(self, con):
		self.con = con

	def update_akun(self, akun: Akun):
		
		self.send('ads', 'update_akun', akun)


	def send(self, routing, action, data, *arg, **kwarg):
		
		msg = Msg(action, data)
		self.con.send(exchange = '', routing_key = routing, body = msg.serialize(),  *arg, **kwarg)

	def serialize(self, data):
		return json.dumps(data, default = self.date_parse)

	def date_parse(self, data):
		if isinstance(data, datetime):
			return data.isoformat()


class IklanConsumer(Consumer, metaclass=abc.ABCMeta):
	

	@abc.abstractmethod
	def update_akun(self, ch, method, properties, msg):
		pass


	@abc.abstractmethod
	def update_campaign(self, ch, method, properties, msg):
		pass

	@abc.abstractmethod
	def update_ad_account(self, ch, method, properties, msg):
		pass

	@abc.abstractmethod
	def update_campaign(self, ch, method, properties, msg):
		pass

	


	

if __name__ == '__main__':
	
	akun = AddAcount(10, 'heri san', datetime.utcnow())

	print(akun.serialize())


