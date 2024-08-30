from typing import Union, List, Any
from ..data_tools.d_s import Input, InputsList, FrequencyDict


class InputManager:
	"""
	This manager processes every
	user's input and adds to an
	input history, defining a
	category of each input object.
	The Manager then uses the list
	of inputs to find a main context.
	"""
	def __init__(self, dataset: dict[str, set]):
		self.dataset = dataset
		self.known_inputs: List['Input'] = InputsList()
		self.unknown_inputs: List['Input'] = InputsList()
	
	@staticmethod
	def format_object(obj: Union[str, Input, Any]) -> Input:
		"""
		Ensure the input being
		taken is of the Input
		type.
		Args:
			:obj: str | Input
			
		:returns: Input
		"""
		if isinstance(obj, str):
			return Input(obj)
		else:
			if hasattr(obj, '__dict__'):
				data = {v for v in obj.__dict__.values() if isinstance(v, str)}
				return Input(data)
	
	def take_input(self, *inputs):
		"""
		Pick up the input/s and
		save it to the history
		if one is valid.
		Args:
			:inputs: tuple[str]
		"""
		for inp in inputs:
			formatted_input: Input = self.format_object(inp)
			if formatted_input.is_valid():
				formatted_input.category = self.classify(formatted_input)
				if formatted_input.category != 'unknown':
					self.known_inputs.append(formatted_input)
				else:
					self.unknown_inputs.append(formatted_input)
		
	def classify(self, inp: Input) -> Union[str | None]:
		"""
		Take an Input object and use its
		literal data attrubute for
		classification.
		Args:
			:inp: Input
			
		:returns: str | None
		"""
		# string data from an Input
		literal_data: set[str] = inp.literal_data
  
  		# a set of patterns which have occured in the Input
		object_set: set[str] = set()
  
		# table of occurencies
		frequency = FrequencyDict()
		
		if len(literal_data) > 0:
			for l_w in literal_data:
				for cat in self.dataset:
					for pattern in self.dataset[cat]:
						if pattern in l_w:
							object_set.add(pattern)
			frequency.update({k: len(object_set & v) for k, v in self.dataset.items()})
			
		return frequency.greatest_pair[0]
	
	@property
	def main_context(self) -> str | None:
		"""
		Get a main subject from
		the list of inputs.
		:returns: str
		"""
		return self.known_inputs.main_context