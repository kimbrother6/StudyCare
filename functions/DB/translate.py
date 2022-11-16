def get_TODO_data(TODO: str):

	lines = TODO.strip().split("\n")

	TODO_data = []
	boolean = ['X', 'O']
	
	for line in lines:

		is_first_line = line == lines[0]

		if is_first_line:
			year = int(line[0:4])
			week = int(line[6:8])
		else:
			success = boolean.index(line[1])
			content = line[5:]

			TODO_data.append((success, content, week, year))

	return TODO_data