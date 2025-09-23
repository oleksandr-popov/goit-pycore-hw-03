Module src.task1
================
Homework task #1 [goit-pycore-hw-03]

This module provides a function to calculate the difference in days between a given date and today.
It also includes a simple CLI for user input.

Functions
---------

`get_days_from_today(date: str) ‑> int`
:   Calculate the difference in days between the given date and today.
    
    Args:
        date (str): The date string in 'YYYY-MM-DD' format.
    
    Returns:
        int: The number of days between the given date and today. If the date is in the future, returns a negative number.
    
    Raises:
        ValueError: If the input date string is not in the correct format or is invalid.

`test_days_calculation()`
:   Command-line interface for testing get_days_from_today().
    Prompts the user for a date and prints the number of days between the input date and today.
    Handles invalid input format.