'''
Q1. How do you get the current date and time in Python?
Ans:
Use datetime.datetime.now(), which returns the current local date & time.
'''
# Example
import datetime
now = datetime.datetime.now()
print(now)


'''
Q2. How do you create a specific date or datetime manually?
Ans:
Use datetime.datetime(year, month, day, hour, minute, second).
Only year, month, day are mandatory — others default to 0.
'''
# Example
dt = datetime.datetime(2025, 1, 15, 14, 30)
print(dt)


'''
Q3. How do you extract components like year, month, or hour?
Ans:
Access attributes: dt.year, dt.month, dt.day, dt.hour, etc.
'''
# Example
print(dt.year, dt.month, dt.day)   # 2025 1 15


'''
Q4. How do you format a datetime object into a string?
Ans:
Use dt.strftime(format_string) with codes like %Y, %m, %d, %H, %M, etc.
'''
# Example
formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
print(formatted)


'''
Q5. How do you perform date/time arithmetic?
Ans:
Use datetime.timedelta to add/subtract days, hours, weeks, etc.
'''
# Example
from datetime import timedelta
future = dt + timedelta(days=2, hours=5)
print(future)


'''
Q6. Most commonly used strftime() format codes:
%Y → full year (2025)
%y → short year (25)
%m → month number (01–12)
%B → month name (January)
%d → day of month
%H → hour (24h)
%M → minute
%S → second
'''
# Example
print(now.strftime("%B %d, %Y"))


'''
Q7. Difference between datetime.date, datetime.time, and datetime.datetime:
date → only Y/M/D  
time → only H/M/S  
datetime → both date + time  
'''
# Example
d = datetime.date.today()
t = datetime.time(12, 30)
dt2 = datetime.datetime.now()
print(d, t, dt2)


'''
Q8. How do you parse a date string into a datetime?
Ans:
Use datetime.datetime.strptime(string, format).
Opposite of strftime().
'''
# Example
s = "2025-01-15 14:30:00"
parsed = datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print(parsed)


'''
Q9. What happens if you try to create an invalid date?
Ans:
Python raises ValueError for invalid dates like month=13 or day=32.
'''
# Example
# datetime.datetime(2025, 13, 1)  # ValueError


'''
Q10. How do you calculate the difference between two dates?
Ans:
Subtract datetime/date objects → returns timedelta.
'''
# Example
d1 = datetime.date(2025, 1, 1)
d2 = datetime.date(2025, 1, 20)
diff = d2 - d1
print(diff.days)   # 19


'''
Q11. Difference between naive and timezone-aware datetimes?
Ans:
Naive datetimes → no timezone info  
Aware datetimes → contain timezone offset  
'''
# Example
naive = datetime.datetime.now()
aware = datetime.datetime.now(datetime.timezone.utc)
print(naive.tzinfo, aware.tzinfo)
