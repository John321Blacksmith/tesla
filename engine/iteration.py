"""
This module contains a few
iterators that work with
the input data.
"""
from typing import Tuple


class InputIterator:
    """
    Iterate through a list
    of inputs and validate
    each for a type.
    """
    def __init__(self, inputs: Tuple[str]):
        self.inputs = inputs
        self._start = 0
        self._next = self._start + 1
    
    def __iter__(self):
        ...
    
    def __next__(self):
        ...
        
def has_only_digits(inputs: Tuple[str]) -> bool:
    """
    Check if the input only contains
    numbers that are not categorized.
    Args:
        :inputs: Tuple[str]
    :returns: bool - True if there are only numbers, False otherwice
    """
    return all(
        (all(sym.isdigit() for sym in inp) for inp in inputs)
    )