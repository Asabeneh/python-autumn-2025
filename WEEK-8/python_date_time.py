def generate_time(time_format = 'eu', size = 'short'):
    from datetime import datetime 
    now = datetime.now()
    year = now.year
    month = now.month 
    day = now.day
    hour = now.hour 
    minute = now.minute
    seconds = now.second
    if time_format.lower() == 'us':
        if size  == 'short':
            return f'{month}/{day}/{year}'
        else:
            return f'{month}/{day}/{year} {hour}:{minute}'
    elif time_format.lower() == 'eu':
        if size == 'short':
            return f'{day}/{month}/{year}'
        else:
            return f'{day}/{month}/{year} {hour}:{minute}'
    else:
        return 'Not a valid time formmat'
     
    
    # print(f'{day}/{month}/{year}')
    # print(f'{day}-{month}-{year}')

    # print(f'{month}/{day}/{year}')

    # print(year, month, day, hour, minute, seconds)
    # print(now)

""" print(generate_time())
print(generate_time('us'))
print(generate_time('us', 'short'))
print(generate_time('US'))
print(generate_time('AU')) """


""" from datetime import datetime
new_year = datetime(2019, 1, 1)
print(new_year)      # 2020-01-01 00:00:00
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute) #1 1 2020 0 0
print(f'{day}/{month}/{year}, {hour}:{minute}')  # 1/1/2020, 0:0 """


""" from datetime import datetime
# current date and time
now = datetime.now()
t = now.strftime("%H:%M:%S")
print("time:", t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("time one:", time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("time two:", time_two)

time_three = now.strftime("%A %B %d, %Y %I:%M %p")
print(time_three) """

""" from datetime import datetime
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)
print(type(date_object), date_object.year, date_object.month) """

from datetime import date, datetime, timedelta
"""
today = date(year=2025, month=10, day=28)
new_year = date(year=2026, month=1, day=1)
time_left_for_newyear = new_year - today
print(time_left_for_newyear)

today = datetime(year=2025, month=10, day=28, hour = 19, minute = 36, second = 0)
new_year = datetime(year=2026, month=1, day=1, hour = 0, minute = 0, second=0)
time_left_for_newyear = new_year - today
print(time_left_for_newyear) """

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)