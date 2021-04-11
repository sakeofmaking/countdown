"""
Countdown

Admin Inputs:
* start_msg = "Countdown to dad's retirement"
* end_msg = "Congrats!"
* count_to = YYYY-MM-DD HH:MM:SS

Display:
* Display start_message if counting down
* Display real-time countdown to count_to
* After countdown, change start_message to end_message

@source: https://realpython.com/python-datetime/
@source: https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
@source: https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
@source: https://css-tricks.com/how-to-create-an-animated-countdown-timer-with-html-css-and-javascript/
"""

# import the time module
import time
from dateutil import tz
from datetime import datetime


def date_to_sec(date_str):
    """Takes input date and returns number of seconds until date"""
    format_str = "%Y-%m-%d %H:%M:%S"
    try:
        duedate = datetime.strptime(date_str, format_str)
    except ValueError:
        duedate = datetime.strptime("2021-04-30 17:00:00", format_str)

    # Create aware datetime instance to account for time zone and daylight saving time
    duedate = duedate.replace(tzinfo=tz.gettz("America/Los_Angeles"))
    countdown = duedate - datetime.now(tz=tz.tzlocal())

    # Don't return negative
    if int(countdown.total_seconds()) > 0:
        return int(countdown.total_seconds())
    return 0


def countdown(t):
    """Takes seconds and counts down until 0"""
    while t:
        print(t)
        time.sleep(1)
        t -= 1

    print('Countdown complete')


if __name__ == "__main__":
    seconds = date_to_sec("2021-04-10 07:33:00")
    countdown(seconds)


