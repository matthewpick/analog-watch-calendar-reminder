import calendar
from datetime import date, timedelta


def reset_watch_after_short_month(check_date: date):

    # Current first-of-month minus one day, should equal 31...

    if check_date.day != 1:
        raise Exception('Invalid input for check_date, day must be first of month')

    check_date = date(check_date.year, check_date.month, 1)

    if (check_date - timedelta(days=1)).day == 31:
        return False

    return True


def calculate_reset_dates_for_next_two_years():
    current_year = date.today().year
    start_year = current_year - 1

    for year in range(start_year, current_year + 2):
        for month in range(1, 13):
            check_date = date(year=year, month=month, day=1)
            if reset_watch_after_short_month(check_date):
                yield check_date


if __name__ == "__main__":
    for check_date in calculate_reset_dates_for_next_two_years():
        year = check_date.year
        month = check_date.month
        weekday_name = calendar.day_name[check_date.weekday()]
        print(f"Reset watch on {calendar.month_name[month]} {year}: "
              f"{check_date.strftime('%Y-%m-%d')} ({weekday_name})")
