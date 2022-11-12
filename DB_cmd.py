import mysql.connector

#DB에 접속
mydb = mysql.connector.connect(
	host='localhost', 
	user='root', 
	password='june0525!', 
	database="StudyCare"
)

mycursor = mydb.cursor()

def DB_cmd(cmd):
	mycursor.execute(f"{cmd}")


def DB_set_reference_day(user, reference_day):
	"""user: str
	reference_day: int"""


	update = f"""UPDATE StudyCare.setting
	SET reference_day={reference_day}
	WHERE user='{user}'
	"""

	mycursor.execute(update)
	mydb.commit()

	print(mycursor.rowcount, "record inserted.")

def get_reference_day(user):
	mycursor.execute(f"SELECT reference_day FROM StudyCare.setting WHERE user='{user}'")

	reference_day = mycursor.fetchall()[0][0]
	return reference_day

def get_this_week_schedule(year, week):

	schedules = get_schedule(year, week)

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

def get_schedules(year, week):

	mycursor.execute(f"""
	SELECT st_year, st_week, ed_year, ed_week, content, cycle FROM StudyCare.Schedule 
	WHERE (st_year = {year} and st_week <= {week}) or (st_year < {year} and {year} < ed_year) or ({year} = ed_year and {week} <= ed_week)""")

	schedules = mycursor.fetchall()

	return schedules


def create(data_bundle):
	crate = f"""INSERT IGNORE INTO TODO
		(success, content, DayofWeek, week, year)
		VALUES (%s, %s, %s, %s, %s)
		"""

	mycursor.executemany(crate, data_bundle)
	mydb.commit()

	print(mycursor.rowcount, "record inserted.")


def select():
	mycursor.execute("SELECT * FROM TODO")
	# 추가로 조건: WHERE id = 2, 정렬: 'ORDER BY name', 거꾸로 정렬: 'ORDER BY name DESC' 사용가능

	myresult = mycursor.fetchall()
	print(myresult)

def delete():
	# sql = "DELETE FROM TODO WHERE week = 36"

	# mycursor.execute(sql)

	mydb.commit()

	print(mycursor.rowcount, "record(s) deleted")


