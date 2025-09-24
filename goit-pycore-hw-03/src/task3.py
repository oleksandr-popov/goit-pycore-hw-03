"""
Homework task #3 [goit-pycore-hw-03]

This module provides a function to normalize phone numbers to
international format.
"""

import re


def normalize_phone(phone_number: str) -> str:
    """
    Normalize a phone number to international format (+38...).

    Args:
        phone_number (str): The phone number string to normalize.

    Returns:
        str: The normalized phone number in international format, or an
        empty string if input is invalid.
    """
    pattern = r"^\+|\d+"
    plus_sign = "+"
    internation_code = "38"
    matches = re.findall(pattern, phone_number.lstrip())
    if len(matches) > 0:
        cleared_phone_number = "".join(matches)
        # If the cleared phone number contains only plus signs,
        # return empty string
        if not any(symbol.isdigit() for symbol in cleared_phone_number):
            return ""
        result_number: str
        if not cleared_phone_number.startswith(plus_sign):
            if cleared_phone_number.startswith(internation_code):
                result_number = plus_sign + cleared_phone_number
            else:
                result_number = plus_sign + internation_code + \
                    cleared_phone_number
        else:
            result_number = cleared_phone_number
        return result_number
    else:
        return ""


if __name__ == '__main__':
    """
    Test function for normalize_phone().
    Prints a list of sanitized phone numbers from various raw inputs.
    """
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "test_for_crash",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    pre_sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    sanitized_numbers = list(filter(lambda x: len(x) > 0,
                                    pre_sanitized_numbers))
    print("Sanitized numbers are:\n", sanitized_numbers)
