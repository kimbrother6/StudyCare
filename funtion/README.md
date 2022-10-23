# StudyCare

main.py 를 실행시켜서 cmd를 실행시킬수 있음.

## cmd

### create TODO 
내일을 기준으로 새로운 주 TODO template을 생성함.
예) 일요일에 cmd 실행 시 다음주 월요일을 기준으로 다음주 TODO template이 생성됨.

### update
update cmd입력시, week와 year을 입력하는 부분이 뜸.
입력한 정보를 바탕으로 before 폴더 안에 있는 파일을 읽어들여 success, content, DayofWeek를 DB에 새로 저장함

|Name|들어갈 데이터|DataType|defualt|예시|
|----|----------|--------|-------|---|
|week|이변년도 시작부터 몆주차인지|int|-|34(주차)
|year|이번년도|int|-|2022(년)
|encoding|인코딩 할 속성|str|utf-8|utf-16|
