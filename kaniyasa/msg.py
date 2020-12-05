import pickle
from dataclasses import dataclass, asdict

from .base_model import BaseModel

@dataclass
class Msg:
	action: str
	data: BaseModel

	def serialize(self):
		return pickle.dumps(self)

	@classmethod
	def deserialize(cls, data):
		return pickle.loads(data)


