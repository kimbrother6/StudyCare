import mysql.connector

#DB에 접속
mydb = mysql.connector.connect(
	host='localhost', 
	user='root', 
	password='june0525!', 
	database="StudyCare"
)

mycursor = mydb.cursor()


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