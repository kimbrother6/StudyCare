from fileinput import filename
from flask import render_template
from flask import Flask, send_file
from functions.create.templates import crearte_template_TODO

app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template('main.html')


@app.route("/api/createTODO")
def createTODO():
	"""새롭게 생성된 일주일 TODO템플릿 다운로드

	Returns:
		text file: 다음주 템플릿
	"""
	file_name = crearte_template_TODO()
	
	return send_file(file_name,
                    mimetype='text/plain',
                    as_attachment=True)