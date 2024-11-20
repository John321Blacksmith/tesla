from typing import Union, Iterable
from .exceptions import UnknownInputError


class Input:
	"""
	This class represents every
	user's input with its literal
	words and category.
	"""
	def __init__(self, data: Union[str | Iterable]):
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
	def category(self, category):
		"""
  		Category automatically gets unknown
		if no suitable category was found.

    	:param category:
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
	def greatest_pair(self) -> Union[tuple[str, int] | None] :
		"""
		Evaluate key-value pairs
		and find one with the
		greatest value.

		:returns:
		"""
		tups: list[tuple[str, int]] = [(k, v) for k, v in self.items() if v > 0]

		if len(tups) > 0:
			possible_tuple: tuple[str, int] = tups[0]
			for i in range(1, len(tups)):
				if tups[i][1] > possible_tuple[1]:
					possible_tuple = tups[i]

			return possible_tuple[0]
		

class KnownInputs(list):
	"""
	A all recognized inputs.
	"""
	def categorize_particles(self, particles: Iterable[str]) -> tuple[str, int]:
		"""
		Take a python object
		and categorize it based
		on its particles.

		:param particles:
		"""
		frequency = FrequencyDict()
		if len(particles) != 0:
			for p in particles:
				if p in frequency: frequency[p] += 1
				else: frequency[p] = 1
		return frequency.greatest_pair

	@property
	def main_context(self) -> Union[tuple[str, int] | None]:
		"""
		Collect context frequencies
		in a dict and find the main
		context.
		
		:returns:
		"""
		if len(self.contexts) > 0:
			result: tuple[str, int] = self.categorize_particles(self.contexts)
			try:
				if result[0] == 'unknown':
					raise UnknownInputError('The main context of the input was not understood')
			except UnknownInputError as exc:
				print(exc.args[0])
			else:
				return result
		return None

	@property
	def contexts(self) -> list[str]:
		"""
		Collect the categories of
		all the sentences being
		taken from input.

		:returns:
		"""
		return [s.category for s in self]
	

class UnknownInputs(list):
	"""
	A list of all unrecognized inputs.
	"""
	...