from StudyCare import app

is_running = __name__ == "__main__"


if is_running:
	app.run(debug=True)