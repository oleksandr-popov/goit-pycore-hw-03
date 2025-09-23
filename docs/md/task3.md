Module src.task3
================
Homework task #3 [goit-pycore-hw-03]

This module provides a function to normalize phone numbers to international format.

Functions
---------

`normalize_phone(phone_number: str) ‑> str`
:   Normalize a phone number to international format (+38...).
    
    Args:
        phone_number (str): The phone number string to normalize.
    
    Returns:
        str: The normalized phone number in international format, or an empty string if input is invalid.

`test_normalize()`
:   Test function for normalize_phone().
    Prints a list of sanitized phone numbers from various raw inputs.