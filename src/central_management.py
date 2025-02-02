"""
This module contains a logic where
work over known and unknown data
is split to two processes.
"""
from __future__ import annotations

from typing import Union, List, Dict
from engine.input_processing import InputProcessor
from engine.sentence_recognition import Recognizer
from engine.data_management import DataManager
from .data_tools.d_s import (
    KnownSentences, UnknownSentences, 
    FrequencyDict, Sentence
)
    

class CentralManager:
    """
    This manager facilitates
    all three domains of working
    with data.

    # Input processing -> domain
    # Sentence recognition -> domain
    # Data management -> domain
    """
    def __init__(
            self
    ) -> None:
        self.input_processor = InputProcessor()
        self._unknown_sentences = UnknownSentences()
        self._known_sentences = KnownSentences()


    def process_input(self)-> List[Sentence]:...

    def recognize_sentences(self)-> Dict[
                                        str,
                                        Union[
                                            KnownSentences,
                                            UnknownSentences
                                        ]
                                    ]:...
    
    def manage_data(self) -> None:...