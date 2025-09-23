"""
Unit tests for normalize_phone function in task3.py
"""
from src.task3 import normalize_phone


def test_ukrainian_mobile():
    assert normalize_phone('067 123 4567') == '+380671234567'
    assert normalize_phone('095-234-5678') == '+380952345678'
    assert normalize_phone('0503451234') == '+380503451234'
    assert normalize_phone('(050)8889900') == '+380508889900'


def test_with_plus_and_spaces():
    assert normalize_phone('+380 44 123 4567') == '+380441234567'
    assert normalize_phone('    +38(050)123-32-34') == '+380501233234'


def test_with_different_separators():
    assert normalize_phone('38050-111-22-22') == '+380501112222'
    assert normalize_phone('38050 111 22 11   ') == '+380501112211'


def test_invalid_input():
    assert normalize_phone('test_for_crash') == ''
    assert normalize_phone('') == ''
    assert normalize_phone('++--') == ''
