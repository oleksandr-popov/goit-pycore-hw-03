"""
Homework task #4 [goit-pycore-hw-03]

This module provides a function to get a list of users with upcoming
birthdays and their congratulation dates.
"""

from datetime import datetime, date, timedelta

name_key = "name"
birthday_key = "birthday"
congratulation_date_key = "congratulation_date"
date_pattern = "%Y.%m.%d"
days_of_upcoming_range = 7
iso_saturday = 6
iso_sunday = 7


def get_upcoming_birthdays(users: list) -> list:
    """
    Get a list of users with upcoming birthdays and their congratulation dates.

    Args:
        users (list): List of dicts, each with 'name' and 'birthday'
        in 'YYYY.MM.DD' format.

    Returns:
        list: List of dicts with 'name' and 'congratulation_date' for
        users whose birthdays are within the upcoming range.
    """
    current_date = datetime.today().date()
    current_year = current_date.year
    upcoming_birthdays_result = []
    for user in users:
        birthday_date = datetime.strptime(user[birthday_key],
                                          date_pattern).date()
        birthday_month = birthday_date.month
        birthday_day = birthday_date.day
        this_year_birthday_date = date(current_year, birthday_month,
                                       birthday_day)
        is_birthday_passed = this_year_birthday_date < current_date
        congrats_date: date
        if is_birthday_passed:
            congrats_date = date(current_year + 1, birthday_month,
                                 birthday_day)
        else:
            congrats_date = this_year_birthday_date
        congrats_day_of_week = congrats_date.isoweekday()
        is_congrats_date_in_weekend = congrats_day_of_week >= iso_saturday
        if is_congrats_date_in_weekend:
            days_factor = 1 if congrats_day_of_week == iso_sunday else 2
            congrats_date = congrats_date + timedelta(days=days_factor)
        if (
            congrats_date.toordinal() - current_date.toordinal()
        ) <= days_of_upcoming_range:
            upcoming_birthdays_result.append(
                {
                    name_key: user[name_key],
                    congratulation_date_key: datetime.strftime(
                        congrats_date, date_pattern
                    ),
                }
            )
    return upcoming_birthdays_result


def test_bitrhdays():
    """
    Test function for get_upcoming_birthdays().
    Prints a list of users and their upcoming congratulation dates.
    """
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Jake Doe", "birthday": "1994.07.19"},
        {"name": "Jane Doe", "birthday": "1990.07.10"},
        {"name": "John Smith", "birthday": "1990.07.6"},
        {"name": "Agent Smith", "birthday": "1990.07.07"},
    ]
    print("We're testing this list of users:\n", users)
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("List of upcoming congratulations:\n", upcoming_birthdays)


test_bitrhdays()
