from functions.create import year, year_weeks, str_weekly_monday, str_weekly_sunday

def crearte_todo_template():
	"""내일을 기준으로 새로운 TODO템플릿을 만들고, 그것과 파일이름 반환

	Returns
		str : template 
		str : template_name
	"""

	template = f"{year}년 {year_weeks}주차({str_weekly_monday}~{str_weekly_sunday}) TODO\n[] - "

	template_name= f"{year}_{year_weeks}week_TODO"


	return template, template_name 