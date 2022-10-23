from create import year, year_weeks, str_weekly_monday, str_weekly_sunday

def TODO():
	f = open(f"{year}년_{year_weeks}주차_TODO", "w")
	f.write(f"{year}년 {year_weeks}주차({str_weekly_monday}~{str_weekly_sunday}) TODO\n")
	f.write("[] - ")
	f.close()

#[O] = 완료
#[X] = 미완료
