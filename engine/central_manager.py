"""API of input and stored data processing """

from typing import List
from .input_management.input_processing import InputManager
from .storage_management.data_processing import DataManager
from .data_tools.d_s import InputsList, FrequencyDict


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
    
    def process_input(self, *inputs):
        """
        Take a client's input
        and return a result.
        """
        self.input_processor.take_input(*inputs)
        self.unknown_inputs = self.input_processor.unknown_inputs
        self.known_inputs = self.input_processor.known_inputs
        
    def get_main_context(self) -> str:
        return self.input_processor.known_inputs.main_context