from functions.create import date

def get_todo_template():
	"새로운 TODO템플릿을 만들고, 그것과 파일이름 반환"

	template = f"{date['year']}년 {date['week']}주차({date['monday']}~{date['sunday']}) TODO\n[] - "

	template_name= f"{date['year']}_{date['week']}_TODO"


	return template, template_name 