# Regular expression pattern for validating version strings in policies.
import re
from typing import Optional, Union

from pyawsopstoolkit_validators.__validations__ import _check_type
from pyawsopstoolkit_validators.exceptions import ValidationError

VERSION_PATTERN: str = r'(2008-10-17|2012-10-17)'
# Regular expression pattern for validating effect strings in policies.
EFFECT_PATTERN: str = r'(Allow|Deny)'
# Regular expression pattern for validating principal strings in policies.
PRINCIPAL_PATTERN: str = r'(AWS|Federated|Service|CanonicalUser)'


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
        f'https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_grammar.html '
        f'for more information.'
    )


def _version(
        value: str,
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate version string.

    :param value: The value to validate.
    :type value: str
    :param raise_error: Whether to raise error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: True if validation passes, False otherwise.
    :rtype: bool
    """
    error_message = _get_error_message('version', 'string', custom_error_message)

    if not _check_type(value, str, raise_error, error_message) or not re.match(VERSION_PATTERN, value):
        if raise_error:
            raise ValidationError(error_message)
        return False

    return True


def _id(
        value: str,
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate id string.

    :param value: The value to validate.
    :type value: str
    :param raise_error: Whether to raise error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: True if validation passes, False otherwise.
    :rtype: bool
    """
    error_message = _get_error_message('id', 'string', custom_error_message)

    return _check_type(value, str, raise_error, error_message)


def _sid(
        value: str,
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate sid string.

    :param value: The value to validate.
    :type value: str
    :param raise_error: Whether to raise error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: True if validation passes, False otherwise.
    :rtype: bool
    """
    error_message = _get_error_message('sid', 'string', custom_error_message)

    return _check_type(value, str, raise_error, error_message)


def _effect(
        value: str,
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate effect string.

    :param value: The value to validate.
    :type value: str
    :param raise_error: Whether to raise error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: True if validation passes, False otherwise.
    :rtype: bool
    """
    error_message = _get_error_message('effect', 'string', custom_error_message)

    if not _check_type(value, str, raise_error, error_message) or not re.match(EFFECT_PATTERN, value):
        if raise_error:
            raise ValidationError(error_message)
        return False

    return True


def _action(
        value: Union[str, list],
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate action string or list of strings.

    :param value: The value to validate.
    :type value: str or list
    :param raise_error: Whether to raise error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: True if validation passes, False otherwise.
    :rtype: bool
    """
    error_message = _get_error_message('action', 'string (*) or list of strings', custom_error_message)

    if not _check_type(value, Union[str, list], raise_error, error_message):
        return False

    if isinstance(value, str) and value != '*':
        if raise_error:
            raise ValidationError(error_message)
        return False
    elif isinstance(value, list):
        if len(value) == 0 or not all(_check_type(val, str, raise_error, error_message) for val in value):
            if raise_error:
                raise ValidationError(error_message)
            return False

    return True


def _resource(
        value: Union[str, list],
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate resource string or list of strings.

    :param value: The value to validate.
    :type value: str or list
    :param raise_error: Whether to raise error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: True if validation passes, False otherwise.
    :rtype: bool
    """
    error_message = _get_error_message(
        'resource', 'string (* or single value) or list of strings', custom_error_message
    )

    if not _check_type(value, Union[str, list], raise_error, error_message):
        return False

    if isinstance(value, list):
        if len(value) == 0 or not all(_check_type(val, str, raise_error, error_message) for val in value):
            if raise_error:
                raise ValidationError(error_message)
            return False

    return True


def _principal(
        value: Union[str, dict],
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate principal string or dictionary.

    :param value: The value to validate.
    :type value: str or dict
    :param raise_error: Whether to raise error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: True if validation passes, False otherwise.
    :rtype: bool
    """
    error_message = _get_error_message('principal', 'string (*) or dictionary', custom_error_message)

    if not _check_type(value, Union[str, dict], raise_error, error_message):
        return False

    if isinstance(value, str) and value != '*':
        if raise_error:
            raise ValidationError(error_message)
        return False
    elif isinstance(value, dict):
        if len(value) == 0:
            if raise_error:
                raise ValidationError(error_message)
            return False

        for p_key, p_values in value.items():
            if not _check_type(p_key, str, raise_error, error_message) \
                    or not re.match(PRINCIPAL_PATTERN, p_key):
                if raise_error:
                    raise ValidationError(error_message)
                return False

            if len(p_values) == 0 or not _check_type(p_values, list, raise_error, error_message) \
                    or not all(_check_type(p_value, str, raise_error, error_message) for p_value in p_values):
                if raise_error:
                    raise ValidationError(error_message)
                return False

    return True


def _condition(
        value: dict,
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate condition dictionary.

    :param value: The value to validate.
    :type value: dict
    :param raise_error: Whether to raise error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: True if validation passes, False otherwise.
    :rtype: bool
    """
    error_message = _get_error_message('condition', 'dictionary', custom_error_message)

    if not _check_type(value, dict, raise_error, error_message) or len(value) == 0:
        if raise_error:
            raise ValidationError(error_message)
        return False

    for c_map_key, c_map_values in value.items():
        if len(c_map_values) == 0 or not _check_type(c_map_key, str, raise_error, error_message) \
                or not _check_type(c_map_values, dict, raise_error, error_message):
            if raise_error:
                raise ValidationError(error_message)
            return False

        for c_type_key, c_type_values in c_map_values.items():
            if len(c_type_values) == 0 or not _check_type(c_type_key, str, raise_error, error_message) \
                    or not _check_type(c_type_values, Union[str, list, dict], raise_error, error_message):
                if raise_error:
                    raise ValidationError(error_message)
                return False

            if isinstance(c_type_values, list) \
                    and not all(_check_type(c_type_value, str, raise_error, error_message)
                                for c_type_value in c_type_values):
                return False
            elif isinstance(c_type_values, dict):
                for c_key_key, c_key_values in c_type_values.items():
                    if len(c_key_values) == 0 or not _check_type(c_key_key, str, raise_error, error_message) \
                            or not _check_type(c_key_values, Union[str, list], raise_error, error_message):
                        if raise_error:
                            raise ValidationError(error_message)
                        return False

                    if isinstance(c_key_values, list) \
                            and (len(c_key_values) == 0
                                 or not all(_check_type(c_key_value, str, raise_error, error_message)
                                            for c_key_value in c_key_values)):
                        if raise_error:
                            raise ValidationError(error_message)
                        return False

    return True


def policy(
        value: dict,
        raise_error: Optional[bool] = True,
        custom_error_message: Optional[str] = None
) -> bool:
    """
    Validate policy dictionary.

    :param value: The value to validate.
    :type value: dict
    :param raise_error: Whether to raise error if validation fails.
    :type raise_error: bool
    :param custom_error_message: Custom error message, if provided.
    :type custom_error_message: str
    :return: True if validation passes, False otherwise.
    :rtype: bool
    """
    _check_type(value, dict, True, 'value should be a dictionary.')
    _check_type(raise_error, Union[bool, None], True, 'raise_error should be a boolean.')
    _check_type(custom_error_message, Union[str, None], True, 'custom_error_message should be a string.')
    error_message = _get_error_message('policy', 'dictionary', custom_error_message)

    if not _check_type(value, dict, raise_error, error_message):
        return False

    if 'Statement' not in value.keys():
        if raise_error:
            raise ValidationError(error_message)
        return False

    for p_key, p_values in value.items():
        if len(p_values) == 0:
            if raise_error:
                raise ValidationError(error_message)
            return False

        if p_key == 'Version':
            if not _version(p_values, raise_error, error_message):
                return False
        elif p_key == 'Id':
            if not _id(p_values, raise_error, error_message):
                return False
        elif p_key == 'Statement':
            statements = value.get('Statement', {})
            if 'Effect' not in statements.keys() or 'Action' not in statements.keys() \
                    or 'Resource' not in statements.keys():
                if raise_error:
                    raise ValidationError(error_message)
                return False

            if not _effect(statements.get('Effect', ''), raise_error, error_message) \
                    or not _action(statements.get('Action', ''), raise_error, error_message) \
                    or not _resource(statements.get('Resource', ''), raise_error, error_message):
                return False

            for s_key, s_values in statements.items():
                if len(s_values) == 0:
                    if raise_error:
                        raise ValidationError(error_message)
                    return False

                if s_key == 'Sid':
                    if not _sid(s_values, raise_error, error_message):
                        return False
                elif s_key in ['Principal', 'NotPrincipal']:
                    if not _principal(s_values, raise_error, error_message):
                        return False
                elif s_key == 'Condition':
                    if not _condition(s_values, raise_error, error_message):
                        return False
                elif s_key not in ['Effect', 'Action', 'Resource']:
                    if raise_error:
                        raise ValidationError(error_message)
                    return False
        elif p_key not in ['Version', 'Id', 'Statement']:
            if raise_error:
                raise ValidationError(error_message)
            return False

    return True
