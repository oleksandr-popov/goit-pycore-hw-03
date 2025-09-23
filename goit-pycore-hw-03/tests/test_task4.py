"""
Unit tests for get_upcoming_birthdays function in task4.py
"""
from datetime import datetime, timedelta

from src.task4 import get_upcoming_birthdays


def test_empty_list():
    assert get_upcoming_birthdays([]) == []


def test_birthday_today():
    today = datetime.today().strftime('%Y.%m.%d')
    users = [{"name": "Test User", "birthday": today}]
    result = get_upcoming_birthdays(users)
    assert result and result[0]["name"] == "Test User"


def test_birthday_in_range():
    in_range = (datetime.today() + timedelta(days=3)).strftime('%Y.%m.%d')
    users = [{"name": "Soon User", "birthday": in_range}]
    result = get_upcoming_birthdays(users)
    assert result and result[0]["name"] == "Soon User"


def test_birthday_out_of_range():
    out_of_range = (datetime.today() + timedelta(days=30)).strftime('%Y.%m.%d')
    users = [{"name": "Far User", "birthday": out_of_range}]
    assert get_upcoming_birthdays(users) == []


def test_birthday_on_weekend():
    # Find the next Saturday
    today = datetime.today()
    days_until_saturday = (5 - today.weekday()) % 7
    saturday = today + timedelta(days=days_until_saturday)
    saturday_str = saturday.strftime('%Y.%m.%d')
    users = [{"name": "Weekend User", "birthday": saturday_str}]
    result = get_upcoming_birthdays(users)
    assert result and result[0]["name"] == "Weekend User"
