from datetime import datetime
dt = datetime.strptime("2025-03-15", "%Y-%m-%d")
print(dt) # 2025-03-15 00:00:00
print(type(dt)) # <class 'datetime.datetime'>

from datetime import date
today = date.today()
print(today) # e.g., 2025-06-15

d1 = datetime.strptime("2025-01-01", "%Y-%m-%d")
d2 = datetime.strptime("2025-01-08", "%Y-%m-%d")
diff = d2 - d1
print(diff.days) # 7
print(type(diff)) # <class 'datetime.timedelta'>

dt = datetime.strptime("2025-03-15", "%Y-%m-%d")
print(dt.weekday()) # 5 (Monday=0, so 5=Saturday)

print(dt.strftime("%B %d, %Y")) # March 15, 2025
print(dt.strftime("%Y-%m-%d")) # 2025-03-15

def days_between(date1: str, date2: str) -> int:
    """Return the absolute number of days between two ISO-format date strings.
    Args:
    date1: A date string in YYYY-MM-DD format.
    date2: A date string in YYYY-MM-DD format.
    Returns:
    The absolute difference in days.
    Raises:
    ValueError: If either string doesn't match YYYY-MM-DD format.
    """
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