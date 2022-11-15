from DB_cmd import mycursor, mydb

def insert_schedule(schedule: list) -> None:
	insert = f"""INSERT INTO StudyCare.schedule
	(st_year, st_week, ed_year, ed_week, content, cycle)
	VALUES (%s, %s, %s, %s, %s, %s)
	"""
	
	mycursor.execute(insert, schedule)
	mydb.commit()

	print(mycursor.rowcount, "record inserted.")

def get_schedules(year: int, week: int) -> list:
	"DB에서 입력한 날짜에 반복될 수 있는 스케줄 제공"

	mycursor.execute(f"""
	SELECT st_year, st_week, ed_year, ed_week, content, cycle FROM StudyCare.Schedule 
	WHERE (st_year = {year} and st_week <= {week}) or (st_year < {year} and {year} < ed_year) or ({year} = ed_year and {week} <= ed_week)""")

	schedules = mycursor.fetchall()

	return schedules

def get_this_week_schedules(year: int, week: int) -> list:
	"이번주 스케줄만 제공"

	schedules = get_schedules(year, week)

	this_week_schedule = []

	for schedule in schedules:
		#이 일정이 이번주 일정인지 확인하기 위한 boolean들
		cycle_state = schedule[5]
		cycle_of_repetition = cycle_state % 10
		is_repetition = cycle_state > 1
		is_right_repetition = (week - schedule[1]) % cycle_of_repetition == 0
		is_no_reptition = schedule[0] == schedule[2] and schedule[1] == schedule[3]
		is_this_week_schedule = (is_repetition and is_right_repetition) or is_no_reptition
		
		if is_this_week_schedule:
			this_week_schedule.append(schedule[4])

	return this_week_schedule
