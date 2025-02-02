"""
This module contains logic
of recognition of the sentences.
"""
from __future__ import annotations
from typing import List, Iterable

from ..data_tools.d_s import (
    Sentence, FrequencyDict,
    KnownSentences, UnknownSentences
    )


class Recognizer:
    """
    This entity performs work
    over the incoming sentences
    and splits ones to known and
    unknown.
    """
    def __init__(
            self,
            all_sentences: List[Sentence],
            dataset: dict[str, set[str]]
    ) -> None:
        self.all_sentences = all_sentences
        self.dataset = dataset
        self.known_sentences = KnownSentences()
        self.unknown_sentences = UnknownSentences()

    def process_sentences(self) -> None:
        """
        Iterate over the list
        of sentences and give
        each a main context.
        """
        if self.all_sentences:
            for i in range(len(self.all_sentences)):
                if self.all_sentences[i].is_valid:
                    self.find_context(self.all_sentences[i])

    def find_context(
            self,
            sentence: Sentence
        ) -> str:
        """
        Take a sentence object
        and find out what it's
        mainly about.
        """
        frequency_dict = FrequencyDict()
        for label in self.dataset:
            for pattern in self.dataset[label]:
                for w in sentence.data:
                    if pattern in w:
                        sentence.object_set.add(pattern)
        frequency_dict.update(
            {k: len(sentence.object_set & v) for k, v in self.dataset.items()}
        )
        frequency_dict.find_greatest_pair()
        if frequency_dict.greatest_pair[0]:
            sentence.context = frequency_dict.greatest_pair[0]
        
    def divide_sentences(self) -> None:
        """
        Iterate over the recognized
        sentences and divide them
        two known and unknown.
        """
        for i in range(len(self.all_sentences)):
            if self.all_sentences[i].context == "undefined":
                self.unknown_sentences.append(self.all_sentences[i])
            else:
                self.known_sentences.append(self.all_sentences[i])

    def find_main_context(self) -> str:
        """
        Take a list of the known
        sentences and find the
        main context.
        """
        return self.known_sentences.main_context