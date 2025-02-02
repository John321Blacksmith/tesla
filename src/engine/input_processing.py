"""
This module contains logic
of dealing with incoming
inputs from the external
clients.
"""

from __future__ import annotations
from typing import Union, List, Any

from ..data_tools.d_s import(
	Sentence, KnownSentences,
	UnknownSentences, FrequencyDict
)


class InputProcessor:
	"""
	This processor performs
	initial work over the raw
	text.
	"""
	def __init__(self) -> None:
		self._sentence_objects: List[Sentence]

	@property
	def sentences(self) -> List[Sentence]:
		return self._sentence_objects

	def process_input(
			self,
			inp: str
		) -> None:
		"""
		Receive the incoming
		input and prepare a
		list of Sentences.
		:Args:
			:param str input: client's input
		"""
		input_chunks = [s for s in inp.split(".") if s != " "]
		for i in range(len(input_chunks)):
			self.sentences.append(
				self.format_sentence(input_chunks[i])
			)
		
	def format_sentence(self, chunk: str) -> Sentence:
		"""
		Take a chunk of text and
		transform it to the
		Sentence object.
		"""
		refined_chunk: set[str] = {
			w.lower() for w in chunk.split(" ")\
				if w.isalpha() and len(w) > 2
		}
		return Sentence(refined_chunk)
			