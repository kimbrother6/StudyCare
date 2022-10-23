import create.template
import DB.cmd
from DB import translate
#명령어 입력
cmd = input("Cmd: ")

try: 
	if cmd == "create TODO":
		create.template.TODO()

	elif cmd == "update":

		#변수 입력
		week = input("week: ")
		year = input("year: ")
		#입력 하지 않고 그냥 엔터 누르면 defualt값(utf-8)이 자동으로 됨
		encoding = input("encoding: (defualt: utf-8)") or 'utf-8' #utf-8로 하면 거의다 되는데 안될때가 있음

		#year과 week를 변수로 그주의 TODO리스트 데이터를 TODO_data에 임시 저장함
		TODO_data = translate.TODO_data(week, year, encoding)

		if TODO_data: #데이터가 존재 한다면
			#위의 TODO_data를 DB에 저장함
			DB.cmd.create(TODO_data)
			
	else :
		raise ValueError

except ValueError:
	print('\033[31m' + '에러: ') #에러코드 빨간색으로
	print('https://github.com/kimbrother6/StudyCare/blob/main/README.md 를 확인하고\n명령어를 제대로 입력해 주세요.')
	print('\033[97m') #색깔 다시 하얀색으로