from typing import Union, Iterable
from dataclasses import dataclass

from .exceptions import UnknownSentenceError


@dataclass
class Sentence:
	"""
	This class represents
	a prepared sentence
	with its context.
	"""
	data: set[str]
	context: str = "undefined"
	object_set: Union[set[str] | None] = None
	
	@property
	def is_valid(self) -> bool:
		return len(self.data) > 0

	def __repr__(self) -> str:
		return f'{self.__class__}, context <{self.context}>'


class FrequencyDict(dict):
	"""
	A customized dictionary
	with an implemented
	data attribute.
	"""
	def __init__(self) -> None:
		self._greatest_pair: tuple[str, int]

	@property
	def greatest_pair(self) -> tuple[str, int]:
		return self._greatest_pair
	
	@greatest_pair.setter()
	def greatest_pair(self, pair: tuple[str, int]) -> None:
		self._greatest_pair = pair

	def find_greatest_pair(self) -> None:
		"""
		Evaluate key-value pairs
		and find one with the
		greatest value.
		"""
		tups: list[tuple[str, int]] = [(k, v) for k, v in self.items() if v > 0]
		if len(tups) > 0:
			possible_tuple: tuple[str, int] = tups[0]
			for i in range(1, len(tups)):
				if tups[i][1] > possible_tuple[1]:
					possible_tuple = tups[i]
			self.greatest_pair = possible_tuple

class KnownSentences(list):
	"""
	A list of all recognized sentences.
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
			frequency.find_greatest_pair()
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
					raise UnknownSentenceError('The main context of the Sentence was not understood')
			except UnknownSentenceError as exc:
				print(exc.args[0])
			else:
				return result
		return None

	@property
	def contexts(self) -> list[str]:
		"""
		Collect the categories of
		all the sentences being
		taken from Sentence.

		:returns:
		"""
		return [s.context for s in self]
	

class UnknownSentences(list):
	"""
	A list of all unrecognized Sentences.
	"""
	...