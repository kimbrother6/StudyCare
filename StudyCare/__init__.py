from flask import render_template
from flask import Flask, Response
from functions.create.templates import crearte_todo_template

app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template('main.html')


@app.route("/api/createTODO")
def download_todo_template():

	template, template_name = crearte_todo_template()
	
	response = Response(template, mimetype='text/plain')

	#다운로드하게 리스폰스 헤더 설정
	response.headers["Content-Disposition"] = f"attachment; filename={template_name}"

	return response