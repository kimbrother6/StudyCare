from functions.create import year, year_weeks, str_weekly_monday, str_weekly_sunday

def crearte_template_TODO():
	"""내일을 기준으로 새로운 주 TODO템플릿을 문자열로 만들고, 그것과 파일이름 반환

	Returns환
		str : file_text
		str : file_name
	"""
	file_text = f"{year}년 {year_weeks}주차({str_weekly_monday}~{str_weekly_sunday}) TODO\n[] - "
	file_name = f"{year}_{year_weeks}week_TODO"
	return file_text, file_name