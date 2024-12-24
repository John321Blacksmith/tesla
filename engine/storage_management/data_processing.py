"""API for classified data management"""
from typing import List



class DataManager:
    """
    This manager performs data
    oriented work over the processed
    inputs.
    """
    def __init__(self, storage_path: str) -> None:
        self.storage_path = storage_path

    def take_data(self, data) -> None:
        """
        Take processed data.
        """
        ...
    
    def serialize_data(self) -> None:
        """
        Serialize data.
        """
        ...
    
    def deserialize_data(self)-> None:
        """
        Deserialize data.
        """
        ...
    
    def save_data(self)-> None:
        """
        Save serialized data.
        """
        ...

    def retrive_data(self) -> None:
        """
        Query data from storage.
        """
        ...