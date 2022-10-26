def TODO_data(week, year, encoding='utf-8'):
	try:
		f = open(f"before/{year}년_{week}주차_TODO", 'r', encoding=encoding)

	except FileNotFoundError:
		print('\033[31m' + '에러: ') #에러코드 빨간색으로
		print(f'{year}년 {week}주차 TODO_List 파일이 before 폴더 안에 없습니다.')
		print('\033[97m') #색깔 다시 하얀색으로
		return None
	except LookupError:
		print('\033[31m' + '에러: ') #에러코드 빨간색으로
		print(f'encoding을 제대로 입력해 주세요. encoding: {encoding}')
		print('\033[97m') #색깔 다시 하얀색으로
		return None

	txt = f.readlines()
	data = txt[1:]
	TODO_data = []

	for i in data:
		i = i.strip()
		DayofWeek = None
		boolean = ['X', 'O']
		try : 
			success = boolean.index(i[1])
		except ValueError:
			print('\033[31m') #에러코드 빨간색으로
			print("""에러:
파일에 TODO 완료/미완료 표시를 해 주세요.
힌트: 완료표시는 O, 미완료표시는 X 입니다.""")
			print('\033[97m') #색깔 다시 하얀색으로
			break #에러가 났으므로, for문 종료

		if i[6] == "(":
			one_week = ['월', '화', '수', '목', '금', '토', '일']
			DayofWeek = one_week.index(i[7]) #요일을 0부터 6까지로 변환
			content = i[10:]

		else:
			content = i[6:]

		TODO_data.append((success, content, DayofWeek, week, year))

	#위에서 비정상적으로 종료되었을때, 
	if not len(data) == len(TODO_data):
		print('\033[31m' + '에러: ') #에러코드 빨간색으로
		print('파일을 다시 수정 해 주세요.')
		print('\033[97m') #색깔 다시 하얀색으로
		return None
	f.close()
	return TODO_data