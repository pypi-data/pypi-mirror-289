import re
from typing import Optional, Union

from pyawsopstoolkit_validators.__validations__ import _check_type
from pyawsopstoolkit_validators.exceptions import ValidationError

# Regular expression pattern for AWS ARNs
ARN_PATTERN: str = (
    r'arn:'  # arn
    r'(aws|aws-cn|aws-us-gov):'  # partition
    r'([a-z0-9-]+):'  # service
    r'([a-z0-9-]+)?:'  # region (optional for global services)
    r'([0-9]{12})?:'  # account id (option for s3)
    r'([a-zA-Z0-9-_:/\*]+)'  # resource id or type
    r'(:[a-zA-Z0-9-_:/\*]+)*'  # resource id
)


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
        f'https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html '
        f'for more information.'
    )


def _arn(
        value: str,
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate if the given string matches the ARN pattern.

    :param value: The string to be validated.
    :type value: str
    :param raise_error: Flag to raise an error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message to be used if raise_error is True and validation fails.
    :type custom_error_message: str
    :return: True if the string matches the ARN pattern, False otherwise.
    :rtype: bool
    """
    error_message = _get_error_message('arn', 'string', custom_error_message)

    if not _check_type(value, str, raise_error, error_message) or not re.match(ARN_PATTERN, value):
        if raise_error:
            raise ValidationError(error_message)
        return False

    return True


def arn(
        value: Union[str, list],
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate if the given ARN(s) match the ARN pattern.

    :param value: The ARN(s) to be validated.
    :type value: str (or) list
    :param raise_error: Flag to raise an error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message to be used if raise_error is True and validation fails.
    :type custom_error_message: str
    :return: True if the ARN(s) match the pattern, False otherwise.
    :rtype: bool
    """
    _check_type(value, Union[str, list], True, 'value should be a string or list of strings.')
    _check_type(raise_error, Union[bool, None], True, 'raise_error should be a boolean.')
    _check_type(custom_error_message, Union[str, None], True, 'custom_error_message should be a boolean.')

    error_message = _get_error_message('arn', 'string or list of strings', custom_error_message)

    if not _check_type(value, Union[str, list], raise_error, error_message):
        return False

    if isinstance(value, str):
        return _arn(value, raise_error, error_message)
    elif isinstance(value, list):
        return all(_arn(val, raise_error, error_message) for val in value)
