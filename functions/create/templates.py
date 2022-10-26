from functions.create import year, year_weeks, str_weekly_monday, str_weekly_sunday

def crearte_template_TODO():
	"""내일을 기준으로 새로운 주 TODO템플릿을 만들고, 파일 경로 반환

	Returns:
		str : 새로 만들어진 파일 경로
	"""
	file_name = f"files/{year}년_{year_weeks}주차_TODO"
	f = open(f"StudyCare/{file_name}", "w")
	f.write(f"{year}년 {year_weeks}주차({str_weekly_monday}~{str_weekly_sunday}) TODO\n")
	f.write("[] - ")
	f.close()
	return file_name

#[O] = 완료
#[X] = 미완료
