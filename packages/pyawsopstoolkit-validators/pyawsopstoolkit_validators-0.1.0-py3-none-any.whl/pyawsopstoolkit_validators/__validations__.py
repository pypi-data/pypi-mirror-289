def _check_type(value, expected_type, raise_error, error_message) -> bool:
    """
    Checks if the given value has the expected type.

    :param value: The value to be checked.
    :type value: Any
    :param expected_type: The expected type for the value.
    :type expected_type: type
    :param raise_error: Flag indicating whether to raise an error if the type check fails.
    :type raise_error: bool
    :param error_message: The error message to be raised if the type check fails and raise_error is True.
    :type error_message: str
    :return: True if the value has the expected type, False otherwise.
    :rtype: bool
    """
    if not isinstance(value, expected_type):
        if raise_error:
            raise TypeError(error_message)
        return False

    return True


def _validate_type(value, expected_type, message) -> None:
    """
    Validates if the given value has the expected type.

    :param value: The value to be validated.
    :type value: Any
    :param expected_type: The expected type for the value.
    :type expected_type: type
    :param message: The error message to be raised if the type check fails.
    :type message: str
    """
    if not isinstance(value, expected_type):
        raise TypeError(message)
