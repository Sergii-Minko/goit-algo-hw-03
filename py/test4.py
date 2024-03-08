from datetime import datetime
from datetime import timedelta

users = [
    {"name": "John Doe", "birthday": "1985.03.15"},
    {"name": "Jane Smith", "birthday": "1990.03.11"},
    {"name": "Alice Johnson", "birthday": "1988.09.22"},
    {"name": "Bob Brown", "birthday": "1995.07.05"},
    {"name": "Boby Brown", "birthday": "1995.01.05"},
]


def find_amount_of_days_before_birthday(birthday_date, today):

    birthday_date = birthday_date.replace(year=today.year).date()
    print(birthday_date)
    if birthday_date >= today:
        amount_of_days = (birthday_date - today).days
        print(amount_of_days)
        return amount_of_days
    elif birthday_date < today:
        birthday_date = birthday_date.replace(year=(today.year + 1))
        amount_of_days = (birthday_date - today).days
        print(amount_of_days)
        return amount_of_days


# Function to get upcoming birthdays within a week
def get_upcoming_birthdays(users):
    # Create an empty list to store upcoming birthdays
    upcoming_birthdays = []
    today = datetime.today().date()

    for user in users:
        # Convert the birthday string to a date object (not datetime)
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d")
        # Calculate the number of days until the upcoming birthday
        days_until_birthday = find_amount_of_days_before_birthday(birthday_date, today)
        # Check if the birthday falls within the upcoming week
        if (days_until_birthday >= 0) and (days_until_birthday < 7):
            # Add the user to the list of upcoming birthdays
            new_user = {}
            new_user["name"] = user["name"]
            new_user["congratulation_date"] = today + datetime.timedelta(
                days=days_until_birthday
            )
            print(f"{new_user} - {days_until_birthday} днів до дня народження!")
            upcoming_birthdays.append(new_user)
    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
