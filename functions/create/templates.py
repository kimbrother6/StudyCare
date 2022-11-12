from functions.create import get_date
from DB_cmd import get_this_week_schedules

def get_todo_template(reference_day):
	"새로운 TODO템플릿을 만들고, 그것과 파일이름 반환"
	
	date = get_date(reference_day)
	schedules = get_this_week_schedules(date['year'], date['week'])

	template = f"{date['year']}년 {date['week']}주차({date['monday']}~{date['sunday']}) TODO\n"

	if schedules:
		for schedule in schedules:
			template += f"[] - {schedule}\n"
	else:
		template += "[] - "

	template_name= f"{date['year']}_{date['week']}_TODO"


	return template, template_name 