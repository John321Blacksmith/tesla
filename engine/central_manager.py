"""API of input and stored data processing """

from typing import List
from .input_management.input_processing import InputProcessor
from .storage_management.data_processing import DataManager
from .data_tools.d_s import InputsList


class Manager:
    """
    This object will perform both
    input processing and data store
    management operations.
    """
    def __init__(self, source: str | dict[str, set[str]]):
        self.source = source
        self.input_processor = InputProcessor(source)
        self.data_manager = DataManager()
        
    @property
    def unknown_inputs(self) -> List["Input"]: # type: ignore
        """
        A list of unrecognized inputs.
        """
        return self._unknown_inputs
    
    @property
    def known_inputs(self) -> List["Input"]: # type: ignore
        """
        A list of recognized inputs.
        """
        return self._known_inputs
    
    @unknown_inputs.setter
    def unknown_inputs(self, inputs: List["Input"]): # type: ignore
        self._unknown_inputs = inputs
        
    @known_inputs.setter
    def known_inputs(self, inputs: List["Input"]): # type: ignore
        self._known_inputs = inputs
    
    def process_input(self, *inputs):
        """
        Take a client's input
        and return a result.
        """
        self.input_processor.take_input(*inputs)
        self.unknown_inputs = self.input_processor.inputs.unrecognized_inputs
        self.known_inputs = self.input_processor.inputs.recognized_inputs
        
    def manage_data(self):
        """
		Handle either classified
		or unknown data.
        """
        ...
        
    def get_main_context(self) -> str:
        return self.input_processor.inputs.main_context