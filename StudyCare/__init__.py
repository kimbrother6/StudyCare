from flask import Flask, Response, redirect, render_template, request
from functions.create.templates import get_todo_template
from settings import settings
from DB_cmd import DB_set_reference_day, get_reference_day

temp_user = 'kimbro6'


app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template('home-page.html')


@app.route("/api/download_todo_template")
def download_todo_template():	

	template, template_name = get_todo_template(get_reference_day(temp_user))
	
	response = Response(template, mimetype='text/plain')

	#다운로드하게 리스폰스 헤더 설정
	response.headers["Content-Disposition"] = f"attachment; filename={template_name}"

	return response

@app.route("/api/setting/reference_day/")
def set_reference_day():
	reference_day = request.args.get('reference_day')
	DB_set_reference_day(temp_user, reference_day)

	return redirect('/')    

