"""API for classified data management"""


class DataManager:
    """
    This manager performs data
    oriented work over the processed
    inputs.
    """
    
    def serialize_data(self): ...
    
    def deserialize_data(self): ...