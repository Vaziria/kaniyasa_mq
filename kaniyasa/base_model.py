from dataclasses import dataclass, asdict

class BaseModel:
	def _asdict(self):
		return asdict(self)