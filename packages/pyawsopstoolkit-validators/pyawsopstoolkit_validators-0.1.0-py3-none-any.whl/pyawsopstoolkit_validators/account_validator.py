import re
from typing import Optional, Union

from pyawsopstoolkit_validators.__validations__ import _check_type
from pyawsopstoolkit_validators.exceptions import ValidationError

NUMBER_PATTERN: str = r'^\d{12}$'


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
        f'https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html '
        f'for more information.'
    )


def number(
        value: str,
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate the account number.

    :param value: Account number to validate.
    :type value: str
    :param raise_error: Flag indicating whether to raise an error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: True if validation succeeds, False otherwise.
    :rtype: bool
    """
    _check_type(value, str, True, 'value should be a string.')
    _check_type(raise_error, Union[bool, None], True, 'raise_error should be a boolean.')
    _check_type(custom_error_message, Union[str, None], True, 'custom_error_message should be a boolean.')

    error_message = _get_error_message(value, 'string', custom_error_message)

    if not _check_type(value, str, raise_error, error_message) or not re.match(NUMBER_PATTERN, value):
        if raise_error:
            raise ValidationError(error_message)
        return False

    return True
