from DB_cmd import mycursor, mydb

def DB_set_reference_day(user: str, reference_day: int) -> None:
	"user의 새로운 생성기준일 설정"

	update = f"""UPDATE StudyCare.setting
	SET reference_day={reference_day}
	WHERE user='{user}'
	"""

	mycursor.execute(update)
	mydb.commit()

	print(mycursor.rowcount, "record inserted.")

def DB_get_reference_day(user: str) -> int:
	"user의 생성기준일 제공"

	mycursor.execute(f"SELECT reference_day FROM StudyCare.setting WHERE user='{user}'")

	reference_day = mycursor.fetchall()[0][0]
	return reference_day