Module src.task2
================
Homework task #2 [goit-pycore-hw-03]

This module provides a function to generate a list of unique random numbers for a lottery ticket.

Functions
---------

`get_numbers_ticket(min: int, max: int, quantity: int) ‑> list[int]`
:   Generate a sorted list of unique random numbers for a lottery ticket.
    
    Args:
        min (int): The minimum possible value (inclusive).
        max (int): The maximum possible value (inclusive).
        quantity (int): The number of unique random numbers to generate.
    
    Returns:
        list[int]: A sorted list of unique random numbers, or an empty list if parameters are invalid.

`test_generation_of_numbers()`
:   Test function for get_numbers_ticket().
    Prints a sample list of generated lottery numbers.