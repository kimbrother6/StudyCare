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
	# 추가로 조건: WHERE id = 2, 정렬: 'ORDER BY name', 거꾸로 정렬: 'ORDER BY name DESC' 사용가능

	reference_day = mycursor.fetchall()[0][0]
	return reference_day


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


