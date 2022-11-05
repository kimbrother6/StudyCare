import datetime


today = datetime.date.today()

reference_date = today + datetime.timedelta(days=1)

date = {
	'year': reference_date.year,
	'month':reference_date.month,
	'monday': (reference_date - datetime.timedelta(days=reference_date.weekday())).strftime("%m/%d"),
	'sunday': (reference_date + datetime.timedelta(days=6) - datetime.timedelta(days=reference_date.weekday())).strftime("%m/%d"),
	'week': reference_date.isocalendar().week
}