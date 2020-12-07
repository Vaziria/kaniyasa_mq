import pickle
from dataclasses import dataclass, asdict
from typing import Union

from .base_model import BaseModel

@dataclass
class Msg:
	action: str
	data: Union[BaseModel, dict]

	def serialize(self):
		return pickle.dumps(self)

	@classmethod
	def deserialize(cls, data):
		return pickle.loads(data)


