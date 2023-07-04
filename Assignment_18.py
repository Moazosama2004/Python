# Assignment 1

import datetime
date = datetime.datetime(2021, 6, 25)
date_now = datetime.datetime(2021, 8, 10)
print(
    f"Days From {date.date()} To {date_now.date()} Is => {(date_now - date).days}")
print("=" * 30)
# Assignment 2

dateNow = datetime.datetime(2021, 8, 10)
print(dateNow.strftime("%Y-%m-%d"))
print(dateNow.strftime("%b %d, %Y"))
print(dateNow.strftime("%d - %b - %Y"))
print(dateNow.strftime("%d / %b / %y"))
print(dateNow.strftime("%d / %B / %Y"))
print(dateNow.strftime("%a, %d %B %Y"))

