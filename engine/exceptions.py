class IconsistentInputError(Exception):
    """
    Error is raised when the input
    contains types other than string.
    """
    ...
    
    
class EmptyInputsListError(Exception):
    """
    Raised when there are not any
    labels based upon inputs.
    """
    ...