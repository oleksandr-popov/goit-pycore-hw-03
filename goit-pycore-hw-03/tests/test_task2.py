"""
Unit tests for get_numbers_ticket function in task2.py
"""
from src.task2 import get_numbers_ticket


def test_valid_ticket():
    numbers = get_numbers_ticket(1, 10, 5)
    assert len(numbers) == 5
    assert all(1 <= n <= 10 for n in numbers)
    assert len(set(numbers)) == 5
    assert numbers == sorted(numbers)


def test_min_greater_than_max():
    assert get_numbers_ticket(10, 5, 3) == []


def test_min_less_than_1():
    assert get_numbers_ticket(0, 10, 3) == []


def test_max_greater_than_1000():
    assert get_numbers_ticket(1, 1001, 3) == []


def test_quantity_too_large():
    assert get_numbers_ticket(1, 5, 10) == []


def test_unique_numbers():
    numbers = get_numbers_ticket(1, 20, 20)
    assert len(numbers) == 0
    assert len(set(numbers)) == 0
