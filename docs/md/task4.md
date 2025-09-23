Module src.task4
================
Homework task #4 [goit-pycore-hw-03]

This module provides a function to get a list of users with upcoming birthdays and their congratulation dates.

Functions
---------

`get_upcoming_birthdays(users: list) ‑> list`
:   Get a list of users with upcoming birthdays and their congratulation dates.
    
    Args:
        users (list): List of dicts, each with 'name' and 'birthday' in 'YYYY.MM.DD' format.
    
    Returns:
        list: List of dicts with 'name' and 'congratulation_date' for users whose birthdays are within the upcoming range.

`test_bitrhdays()`
:   Test function for get_upcoming_birthdays().
    Prints a list of users and their upcoming congratulation dates.