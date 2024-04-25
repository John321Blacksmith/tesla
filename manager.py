from d_s import Input, InputsList, FrequencyDict


class DataManager:
	def __init__(self, filename: str):
		self.filename = filename
	
	def serialize(self, obj):
		"""
		Transform the python
		object to the Bytes.
		"""
		...
	
	def deserialize(self):
		"""
		Convert the bytes back
		to the python object.
		"""
		...
		

class Manager:
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
		self.inputs = InputsList()
		
	def format_object(self, obj) -> Input:
		"""
		Ensure the input being
		taken is of the Text
		type.
		Args:
			:obj: any[str] | Text
			
		:returns: Text
		"""
		return obj if isinstance(obj, Input) else Input(obj)
	
	def take_input(self, *inputs):
		"""
		Pick up the input/s and
		save it to the history.
		Args:
			:sentences: tuple[Text | any]
		"""
		for inp in inputs:
			defined_input: Input = self.format_object(inp)
			defined_input.category: str | None = self.classify(defined_input)
			self.inputs.append(defined_input)
		
	def classify(self, inp) -> str | None:
		"""
		Take an Input object and use its
		literal data attrubute for
		classification.
		Args:
			:sentence: Input
			
		:returns: str | None
		"""
		literal_data: set[str] = inp.literal_data
		object_set: set[str] = set()
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
	def main_context(self) -> str:
		"""
		Get a main subject from
		the list of inputs.
		:returns: str
		"""
		return self.inputs.main_context
