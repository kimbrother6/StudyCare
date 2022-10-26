import datetime
today = datetime.date.today()
tomorrow = today + datetime.timedelta(days=1)

year = tomorrow.year
month = tomorrow.month

str_weekly_monday = (tomorrow - datetime.timedelta(days=tomorrow.weekday())).strftime("%m/%d")
weekly_monday = tomorrow - datetime.timedelta(days=tomorrow.weekday())
str_weekly_sunday = (tomorrow + datetime.timedelta(days=6) - datetime.timedelta(days=tomorrow.weekday())).strftime("%m/%d")

year_weeks = tomorrow.isocalendar().week