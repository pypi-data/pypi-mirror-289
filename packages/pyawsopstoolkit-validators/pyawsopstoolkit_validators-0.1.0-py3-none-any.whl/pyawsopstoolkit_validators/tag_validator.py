# This regular expression pattern is used to validate keys in a dictionary of tags.
import re
from typing import Optional, Union

from pyawsopstoolkit_validators.__validations__ import _check_type
from pyawsopstoolkit_validators.exceptions import ValidationError

KEY_PATTERN: str = r'^[a-zA-Z0-9\.\-_:]{1,128}$'
# This regular expression pattern is used to validate values in a dictionary of tags.
VALUE_PATTERN: str = r'^[a-zA-Z0-9\.\-_:]{1,128}?$'


def _get_error_message(
        variable_name: str,
        variable_type: str,
        custom_error_message: Optional[str] = None
) -> str:
    """
    Get the error message for the validation.

    :param variable_name: Name of the variable being validated.
    :type variable_name: str
    :param variable_type: Expected type of the variable.
    :type variable_type: str
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: Error message.
    :rtype: str
    """
    return custom_error_message or (
        f'{variable_name} should be of {variable_type}. Refer to '
        f'https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html '
        f'for more information.'
    )


def _tag(
        value: dict,
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate a dictionary of tags.

    :param value: The dictionary of tags to validate.
    :type value: dict
    :param raise_error: Flag indicating whether to raise an error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message to use if validation fails.
    :type custom_error_message: str
    :return: True if the dictionary of tags is valid, False otherwise.
    :rtype: bool
    """
    error_message = _get_error_message('tag', 'dictionary', custom_error_message)

    key_pattern = re.compile(KEY_PATTERN)
    value_pattern = re.compile(VALUE_PATTERN)

    if not _check_type(value, dict, raise_error, error_message):
        return False

    for key, val in value.items():
        if not _check_type(key, str, raise_error, error_message) \
                or not _check_type(val, str, raise_error, error_message) \
                or not key_pattern.match(key) or not value_pattern.match(val):
            if raise_error:
                raise ValidationError(error_message)
            return False

    return True


def tag(
        value: Union[dict, list],
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate a dictionary or a list of dictionaries of tags.

    :param value: The value to validate, either a dictionary or a list of dictionaries.
    :type value: dict or list
    :param raise_error: Flag indicating whether to raise an error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message to use if validation fails.
    :type custom_error_message: str
    :return: True if the value is valid, False otherwise.
    :rtype: bool
    """
    _check_type(value, Union[dict, list], True, 'value should be a dictionary or list.')
    _check_type(raise_error, Union[bool, None], True, 'raise_error should be a boolean.')
    _check_type(custom_error_message, Union[str, None], True, 'custom_error_message should be a boolean.')

    error_message = _get_error_message('tag', 'dictionary or list of dictionaries', custom_error_message)

    if not _check_type(value, Union[dict, list], raise_error, error_message):
        return False

    if isinstance(value, dict):
        return _tag(value, raise_error, error_message)
    elif isinstance(value, list):
        return all(_tag(val, raise_error, error_message) for val in value)
