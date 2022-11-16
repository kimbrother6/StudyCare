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

def clean_TODO_records(TODO_records: list):
	"success의 0, 1을 X, O로 변환"
	ret = []
	for record in TODO_records:
		record = list(record)
		if record[0] == 0:
			record[0] = "X"
		else:
			record[0] = "O"
		ret.append(record)
	return ret



def get_TODO_records():
	mycursor.execute("SELECT success, content, week, year FROM StudyCare.TODO ORDER BY week DESC")
	# 추가로 조건: WHERE id = 2, 정렬: 'ORDER BY name', 거꾸로 정렬: 'ORDER BY name DESC' 사용가능

	TODO_records = mycursor.fetchall()
	TODO_records = clean_TODO_records(TODO_records)
	return TODO_records