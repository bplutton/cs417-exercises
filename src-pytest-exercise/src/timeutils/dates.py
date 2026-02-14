from datetime import datetime, timedelta
def days_between(date1: str, date2: str) -> int:
    fmt = "%Y-%m-%d"
    d1 = datetime.strptime(date1, fmt)
    d2 = datetime.strptime(date2, fmt)
    return abs((d2 - d1).days)


def is_weekend(date_str: str) -> bool:
    """Check whether a date falls on a Saturday or Sunday.
    Args:
    date_str: A date string in YYYY-MM-DD format.
    Returns:
    True if the date is a Saturday or Sunday, False otherwise.
    Raises:
    ValueError: If the string doesn't match YYYY-MM-DD format.
    """
    fmt = "%Y-%m-%d"
    dt = datetime.strptime(date_str, fmt)
    return dt.weekday() >= 5
    """Return the absolute number of days between two ISO-format date strings.
    Args:
    date1: A date string in YYYY-MM-DD format.
    date2: A date string in YYYY-MM-DD format.
    Returns:
    The absolute difference in days.
    Raises:
    ValueError: If either string doesn't match YYYY-MM-DD format.
    """


def next_weekday(date_str: str, weekday: int) -> str:
    """
    Given a date string in YYYY-MM-DD format and a weekday integer (0=Monday through 6=Sunday), return the next occurrence of that weekday as a YYYY-MM-DD string. If the given date is already that weekday, return the following week's occurrence.

    Hints:

    dt.weekday() gives you the current day's weekday number.
    Think about the arithmetic: if today is Wednesday (2) and you want the next Friday (4), that's 2 days away. If today is Wednesday and you want the next Monday (0), that's 5 days away.
    The formula (target - current) % 7 gives you the number of days to add — but if the result is 0, the date is already that weekday, so you'd want 7 instead.
    timedelta(days=n) lets you add days to a datetime object.
    Use .strftime("%Y-%m-%d") to convert back to a string.
    """
    fmt = "%Y-%m-%d"
    dt = datetime.strptime(date_str, fmt)
    current_weekday = dt.weekday()
    days_ahead = (weekday - current_weekday) % 7
    if days_ahead == 0:
        days_ahead = 7
    next_dt = dt + timedelta(days=days_ahead)
    return next_dt.strftime(fmt)