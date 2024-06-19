class OnlyDigitsDetectedError(Exception):
    """
    Error raised when there are
    only numbers in the input.
    """
    ...


class IconsistentInputError(Exception):
    """
    Error is raised when the input
    contains types other than string.
    """
    ...