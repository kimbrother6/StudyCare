from DB_cmd import mycursor, mydb

def insert_TODO_data(TODO_data):
	#INSERT IGNORE는 중복 키 에러가 발생했을 때 신규로 입력되는 레코드를 무시하는 단순한 방법이다.
	insert = f"""INSERT IGNORE INTO TODO
		(success, content, week, year)
		VALUES (%s, %s, %s, %s)
		"""

	mycursor.executemany(insert, TODO_data)
	mydb.commit()

	print(mycursor.rowcount, "record inserted.")