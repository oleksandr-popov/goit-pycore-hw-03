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


if __name__ == '__main__':
    """
    Test function for get_upcoming_birthdays().
    Prints a list of users and their upcoming congratulation dates.
    """
    users = [
        {"name": "Olivia Smith", "birthday": "1992.03.15"},
        {"name": "Liam Johnson", "birthday": "1988.07.22"},
        {"name": "Emma Williams", "birthday": "1995.11.30"},
        {"name": "Noah Brown", "birthday": "1991.05.09"},
        {"name": "Ava Jones", "birthday": "1987.12.02"},
        {"name": "Oliver Garcia", "birthday": "1993.04.18"},
        {"name": "Sophia Miller", "birthday": "1990.09.27"},
        {"name": "Elijah Davis", "birthday": "1989.06.14"},
        {"name": "Isabella Rodriguez", "birthday": "1994.02.25"},
        {"name": "Lucas Martinez", "birthday": "1996.08.11"},
        {"name": "Mia Hernandez", "birthday": "1992.10.05"},
        {"name": "Mason Lopez", "birthday": "1986.01.19"},
        {"name": "Charlotte Gonzalez", "birthday": "1993.12.23"},
        {"name": "Logan Wilson", "birthday": "1991.03.08"},
        {"name": "Amelia Anderson", "birthday": "1988.05.29"},
        {"name": "James Thomas", "birthday": "1990.07.13"},
        {"name": "Harper Taylor", "birthday": "1995.09.21"},
        {"name": "Benjamin Moore", "birthday": "1987.11.04"},
        {"name": "Evelyn Jackson", "birthday": "1992.02.16"},
        {"name": "Jacob Martin", "birthday": "1994.06.28"},
        {"name": "Abigail Lee", "birthday": "1989.08.17"},
        {"name": "Carter Perez", "birthday": "1991.12.12"},
        {"name": "Ella White", "birthday": "1993.04.03"},
        {"name": "William Harris", "birthday": "1996.10.27"},
        {"name": "Scarlett Clark", "birthday": "1988.01.07"},
        {"name": "Henry Lewis", "birthday": "1990.05.15"},
        {"name": "Grace Robinson", "birthday": "1992.09.02"},
        {"name": "Alexander Walker", "birthday": "1987.03.19"},
        {"name": "Chloe Young", "birthday": "1995.07.25"},
        {"name": "Sebastian Allen", "birthday": "1991.11.10"},
        {"name": "Penelope King", "birthday": "1994.02.01"},
        {"name": "Jack Wright", "birthday": "1989.06.22"},
        {"name": "Layla Scott", "birthday": "1993.08.14"},
        {"name": "Aiden Green", "birthday": "1990.12.29"},
        {"name": "Riley Adams", "birthday": "1992.04.09"},
        {"name": "Samuel Baker", "birthday": "1988.09.18"},
        {"name": "Aria Nelson", "birthday": "1991.01.31"},
        {"name": "Matthew Carter", "birthday": "1995.05.06"},
        {"name": "Zoe Mitchell", "birthday": "1987.07.12"},
        {"name": "David Perez", "birthday": "1993.11.16"},
        {"name": "Lily Roberts", "birthday": "1990.03.27"},
        {"name": "Joseph Turner", "birthday": "1992.08.20"},
        {"name": "Nora Phillips", "birthday": "1989.10.02"},
        {"name": "Jackson Campbell", "birthday": "1994.12.08"},
        {"name": "Mila Parker", "birthday": "1991.06.03"},
        {"name": "Levi Evans", "birthday": "1988.02.21"},
        {"name": "Emily Edwards", "birthday": "1995.09.15"},
        {"name": "Wyatt Collins", "birthday": "1993.01.11"},
        {"name": "Sofia Stewart", "birthday": "1990.05.23"},
        {"name": "Daniel Sanchez", "birthday": "1987.11.29"},
        {"name": "Victoria Morris", "birthday": "1992.07.04"},
        {"name": "Gabriel Rogers", "birthday": "1994.03.20"},
        {"name": "Hannah Reed", "birthday": "1989.08.30"},
        {"name": "Julian Cook", "birthday": "1991.12.17"},
        {"name": "Aurora Morgan", "birthday": "1993.06.25"},
        {"name": "Lincoln Bell", "birthday": "1990.09.08"},
        {"name": "Savannah Murphy", "birthday": "1995.02.13"},
        {"name": "Anthony Bailey", "birthday": "1988.04.26"},
        {"name": "Addison Rivera", "birthday": "1992.10.19"},
        {"name": "Isaac Cooper", "birthday": "1994.01.05"},
        {"name": "Brooklyn Richardson", "birthday": "1991.07.23"},
        {"name": "Dylan Cox", "birthday": "1987.03.02"},
        {"name": "Stella Howard", "birthday": "1993.05.30"},
        {"name": "Luke Ward", "birthday": "1990.11.12"},
        {"name": "Paisley Torres", "birthday": "1995.08.03"},
        {"name": "Andrew Peterson", "birthday": "1989.01.28"},
        {"name": "Ellie Gray", "birthday": "1992.06.07"},
        {"name": "Nathan Ramirez", "birthday": "1994.09.26"},
        {"name": "Skylar James", "birthday": "1991.02.15"},
        {"name": "Caleb Watson", "birthday": "1988.12.20"},
        {"name": "Hazel Brooks", "birthday": "1993.03.04"},
        {"name": "Christian Kelly", "birthday": "1990.07.18"},
        {"name": "Violet Sanders", "birthday": "1995.10.29"},
        {"name": "Jonathan Price", "birthday": "1987.05.11"},
        {"name": "Aurora Bennett", "birthday": "1992.01.14"},
        {"name": "Hunter Wood", "birthday": "1994.08.22"},
        {"name": "Samantha Barnes", "birthday": "1991.04.02"},
        {"name": "Eli Ross", "birthday": "1989.09.09"},
        {"name": "Penelope Henderson", "birthday": "1993.12.19"},
        {"name": "Christopher Coleman", "birthday": "1990.02.24"},
        {"name": "Layla Jenkins", "birthday": "1995.06.16"},
        {"name": "Joshua Perry", "birthday": "1988.08.28"},
        {"name": "Lillian Powell", "birthday": "1992.11.01"},
        {"name": "Samuel Long", "birthday": "1994.05.13"},
        {"name": "Zoey Patterson", "birthday": "1991.10.07"},
        {"name": "Owen Hughes", "birthday": "1987.04.15"},
        {"name": "Avery Flores", "birthday": "1993.07.31"},
        {"name": "Grayson Washington", "birthday": "1990.12.04"},
        {"name": "Madison Butler", "birthday": "1995.03.22"},
        {"name": "Leah Simmons", "birthday": "1989.06.01"},
        {"name": "Jack Foster", "birthday": "1992.09.13"},
        {"name": "Scarlett Bryant", "birthday": "1994.11.24"},
        {"name": "Julian Alexander", "birthday": "1991.01.02"},
        {"name": "Eleanor Russell", "birthday": "1988.05.20"},
        {"name": "Isaiah Griffin", "birthday": "1993.10.10"},
        {"name": "Camila Diaz", "birthday": "1990.08.26"},
        {"name": "Hudson Hayes", "birthday": "1995.12.30"},
        {"name": "Victoria Myers", "birthday": "1987.02.08"},
        {"name": "Easton Ford", "birthday": "1992.06.29"},
        {"name": "Lucy Hamilton", "birthday": "1994.04.12"},
        {"name": "Ezra Graham", "birthday": "1991.09.05"},
        {"name": "Aurora Sullivan", "birthday": "1989.11.21"},
        {"name": "Thomas Wallace", "birthday": "1993.02.27"},
        {"name": "Stella West", "birthday": "1990.07.16"},
        {"name": "Aaron Jordan", "birthday": "1995.05.18"},
        {"name": "Nora Owens", "birthday": "1988.10.25"},
        {"name": "Elianna Hunter", "birthday": "1992.03.08"},
        {"name": "Colton Stone", "birthday": "1994.09.30"},
        {"name": "Paisley Dean", "birthday": "1991.12.21"},
        {"name": "Adrian Bishop", "birthday": "1987.06.06"},
        {"name": "Aubrey Ray", "birthday": "1993.08.17"},
        {"name": "Jaxon Holt", "birthday": "1990.11.28"},
        {"name": "Maya Kim", "birthday": "1995.01.09"},
    ]
    print("List of users:\n", users)
    upcoming_birthdays = get_upcoming_birthdays(users)
    print("List of upcoming congratulations:\n", upcoming_birthdays)
