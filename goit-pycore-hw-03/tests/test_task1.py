"""
Unit tests for get_days_from_today function in task1.py
"""
import pytest
from datetime import datetime, timedelta

from src.task1 import get_days_from_today


def test_today():
    today = datetime.today().strftime('%Y-%m-%d')
    assert get_days_from_today(today) == 0


def test_past_date():
    date = (datetime.today() - timedelta(days=10)).strftime('%Y-%m-%d')
    assert get_days_from_today(date) == 10


def test_future_date():
    date = (datetime.today() + timedelta(days=5)).strftime('%Y-%m-%d')
    assert get_days_from_today(date) == -5


def test_invalid_format():
    with pytest.raises(ValueError):
        get_days_from_today('2025/09/24')


def test_nonexistent_date():
    with pytest.raises(ValueError):
        get_days_from_today('2025-02-30')
