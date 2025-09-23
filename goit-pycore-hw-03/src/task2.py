"""
Homework task #2 [goit-pycore-hw-03]

This module provides a function to generate a list of unique random numbers
for a lottery ticket.
"""

import random


def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    """
    Generate a sorted list of unique random numbers for a lottery ticket.

    Args:
        min (int): The minimum possible value (inclusive).
        max (int): The maximum possible value (inclusive).
        quantity (int): The number of unique random numbers to generate.

    Returns:
        list[int]: A sorted list of unique random numbers, or an empty list
            if parameters are invalid.
    """
    if min < 1 or min > max:
        return []
    if max < min or max > 1000:
        return []
    if max - min < quantity:
        # in this case we're never fill set with enoght random numbers
        return []
    numbers_set = set()
    while len(numbers_set) < quantity:
        random_number = random.randint(min, max)
        numbers_set.add(random_number)
    result = list(numbers_set)
    result.sort()
    return result


def test_generation_of_numbers():
    """
    Test function for get_numbers_ticket().
    Prints a sample list of generated lottery numbers.
    """
    lottery_numbers = get_numbers_ticket(1, 100, 10)
    print(lottery_numbers)


test_generation_of_numbers()
