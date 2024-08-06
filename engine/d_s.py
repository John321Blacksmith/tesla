from typing import Union
from .exceptions import UnknownInputError


class Input:
	"""
	This class represents every
	user's input with its literal
	words and category.
	"""
	def __init__(self, data: Union[str | tuple[str]]):
		self.data = data if isinstance(data, str) else ' '.join(d for d in data)
		
	@property
	def category(self) -> str:
		"""
		A category to which
		the input can be
		associated.
		"""
		return self._category
	
	@category.setter
	def category(self, category) -> Union[str | None]:
		"""
  		Category automatically gets unknown
		if no suitable category was found.
    	"""
		self._category = category if category else 'unknown'
	
	@property
	def literal_data(self) -> set[str]:
		"""
		A collection of words
		the input consists.
		"""
		return {w.lower() for w in self.data.split(' ') if len(w) > 2 and w.isalpha()}

	def is_valid(self):
		"""
		Ensure the input is not
  		empty.
		"""
		return len(self.literal_data) != 0

	def __repr__(self) -> str:
		return f'{self.__class__}, category <{self.category}>'


class FrequencyDict(dict):
	"""
	A customized dictionary
	with an implemented
	data attribute.
	"""
	@property
	def greatest_pair(self) -> tuple[str, int]:
		"""
		Evaluate key-value pairs
		and find one with the
		greatest value.
		:returns: tuple[int, str]
		"""
		tups: list[tuple[str, int]] = [(k, v) for k, v in self.items() if v > 0]
		if len(tups) > 0:
			possible_tuple: tuple[str, int] = tups[0]
			for i in range(1, len(tups)):
				if tups[i][1] > possible_tuple[1]:
					possible_tuple = tups[i]
			return possible_tuple
		return (None, 0)
		

class InputsList(list):
	"""
	A data structure which contains
	input objects with their data.
	"""
	@property
	def main_context(self) -> Union[str | None]:
		"""
		Collect context frequencies
		in a dict and find the main
		context.
		:returns: str | None
		"""
		if len(self.contexts) > 0:
			frequency = FrequencyDict()
			for context in self.contexts:
				if context in frequency:
					frequency[context] += 1
				else:
					frequency[context] = 1
			try:
				if frequency.greatest_pair[0] == 'unknown':
					raise UnknownInputError('The main context of the input was not understood')
			except UnknownInputError as exc:
				print(exc.args[0])
			else:
				return frequency.greatest_pair[0]
		return None

	@property
	def contexts(self) -> list[str]:
		"""
		Collect the categories of
		all the sentences being
		taken from input.
		:returns: list[str]
		"""
		return [s.category for s in self]
	
	@property
	def unrecognized_inputs(self):
		"""
		Gather a list of all the
		inputs not classified.
		"""
		return [inp for inp in self if inp.category == 'unknown']
