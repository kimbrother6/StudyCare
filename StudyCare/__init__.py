from urllib import response
from flask import render_template
from flask import Flask, send_file, Response
from functions.create.templates import crearte_template_TODO

app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template('main.html')


@app.route("/api/createTODO")
def createTODO():
	"""새롭게 생성된 일주일 TODO템플릿 다운로드

	Returns:
		text_file: 다음주 템플릿
	"""
	file_text, file_name = crearte_template_TODO()
	response = Response(file_text, mimetype='text/plain')

	response.headers["Content-Disposition"] = f"attachment; filename={file_name}"
	return response