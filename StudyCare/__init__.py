from flask import render_template
from flask import Flask, Response
from functions.create.templates import get_todo_template

app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template('home-page.html')


@app.route("/api/createTODO")
def download_todo_template():	

	template, template_name = get_todo_template()
	
	response = Response(template, mimetype='text/plain')

	#다운로드하게 리스폰스 헤더 설정
	response.headers["Content-Disposition"] = f"attachment; filename={template_name}"

	return response



