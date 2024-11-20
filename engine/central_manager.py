"""API of input and stored data processing """

from typing import List
from .input_management.input_processing import InputManager
from .storage_management.data_processing import DataManager
from .data_tools.d_s import (
    KnownInputs, UnknownInputs, 
    FrequencyDict, Input
)


class Manager:
    """
    This object will perform both
    input processing and data store
    management operations.
    """
    def __init__(self, source: str | dict[str, set[str]]):
        self.source = source
        self.input_processor = InputManager(source)
        self.data_manager = DataManager()
        self._known_inputs = KnownInputs
        self._unknown_inputs = UnknownInputs

    @property
    def known_inputs(self)-> KnownInputs:
        return self._known_inputs
    
    @known_inputs.setter
    def known_inputs(self, inputs: KnownInputs) -> None:
        self._known_inputs = inputs
    
    @property
    def unknown_inputs(self) -> UnknownInputs:
        return self._unknown_inputs
    
    @unknown_inputs.setter
    def unknown_inputs(self, inputs: UnknownInputs) -> None:
        self._unknown_inputs = inputs
    
    def process_input(self, inp: str):
        """
        Take a client's input
        and split it to known
        and unknown inputs.

        :param inp:
        """
        self.input_processor.take_input(inp)
        self.unknown_inputs = self.input_processor.unknown_inputs
        self.known_inputs = self.input_processor.known_inputs
        
    def get_main_context(self) -> str:
        """
        Return a main context of the
        user's text.
        """
        return self.known_inputs.main_context