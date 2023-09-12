import re

# FORMATTING
############


# OPERATIONS
############


def is_valid_landline(phone_number):  # type: (str) -> bool
    """
    Returns whether or not the verifying first 3 digits are a
    match.This function validates only Brazilian landline numbers
    and does not verify if the number actually exists.
    Input should be a digit string of proper length.

    """
    pattern = re.compile(r"^[1-9][1-9][2-5]\d{7}$")
    return isinstance(phone_number, str) and re.match(pattern, phone_number)


def is_valid_mobile(phone_number):  # type: (str) -> bool
    """
    Returns whether or not the verifying first 3 digits are a
    match.This function validates only Brazilian mobile numbers
    and does not verify if the number actually exists.
    Input should be a digit string of proper length.

    """
    pattern = re.compile(r"^[1-9][1-9][9]\d{8}$")
    return isinstance(phone_number, str) and re.match(pattern, phone_number)


def is_valid(phone_number):  # type: (str) -> bool
    """
    Returns whether or not the verifying first 3 digits are a
    match.This function validates only Brazilian phone numbers
    and does not verify if the number actually exists.
    Input should be a digit string of proper length.

    """
    return is_valid_landline(phone_number) or is_valid_mobile(phone_number)
