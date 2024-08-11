# Regular expression pattern used to validate region codes.
import re
from typing import Optional, Union

from pyawsopstoolkit_validators.__globals__ import AWS_REGION_CODES
from pyawsopstoolkit_validators.__validations__ import _check_type
from pyawsopstoolkit_validators.exceptions import ValidationError

REGION_PATTERN: str = r'^[a-z]{2}-[a-z]{4,}-\d$'


def _get_error_message(
        variable_name: str,
        variable_type: str,
        custom_error_message: Optional[str] = None,
        reference_link: Optional[str] = None
) -> str:
    """
    Get the error message for the validation.

    :param variable_name: Name of the variable being validated.
    :type variable_name: str
    :param variable_type: Expected type of the variable.
    :type variable_type: str
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :param reference_link: Reference link, if provided.
    :type reference_link: str
    :return: Error message.
    :rtype: str
    """
    return custom_error_message or (
        f'{variable_name} should be of {variable_type}.'
        f'{f"Refer to {reference_link} for more information." if reference_link else ""}'
    )


def region(
        value: str,
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate a region value.

    :param value: The region value to be validated.
    :type value: str
    :param raise_error: Flag indicating whether to raise an error when validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message to be used if validation fails.
    :type custom_error_message: str
    :return: True if the region value is valid, False otherwise.
    :rtype: bool
    """
    _check_type(value, str, True, 'value should be a string.')
    _check_type(raise_error, Union[bool, None], True, 'raise_error should be a boolean.')
    _check_type(custom_error_message, Union[str, None], True, 'custom_error_message should be a string.')
    error_message = _get_error_message(
        'region',
        'string',
        custom_error_message,
        'https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeAccount.html'
    )

    if (
            not _check_type(value, str, raise_error, error_message)
            or not re.match(REGION_PATTERN, value)
            or value not in AWS_REGION_CODES
    ):
        if raise_error:
            raise ValidationError(error_message)
        return False

    return True
