from flask import Flask, Response, redirect, render_template, request
from functions.create.templates import get_todo_template
from settings import settings
from DB_cmd.reference_day import DB_set_reference_day, DB_get_reference_day
from DB_cmd.schedule import insert_schedule
from DB_cmd.TODO import insert_TODO_data
from functions.DB.translate import get_TODO_data

temp_user = 'kimbro6'


app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template('home-page.html')


@app.route("/api/download_todo_template")
def download_todo_template():	

	template, template_name = get_todo_template(DB_get_reference_day(temp_user))
	
	response = Response(template, mimetype='text/plain')

	#다운로드하게 리스폰스 헤더 설정
	response.headers["Content-Disposition"] = f"attachment; filename={template_name}"

	return response


@app.route("/api/setting/reference_day/")
def set_reference_day():
	reference_day = request.args.get('reference_day')
	DB_set_reference_day(temp_user, reference_day)

	return redirect('/')    

@app.route("/api/add_schedule/")
def add_schedule():

	schedule = [request.args.get('st_year'), request.args.get('st_week'), request.args.get('ed_year'), request.args.get('ed_week'), request.args.get('content'), request.args.get('cycle')]

	insert_schedule(schedule)

	return redirect('/')



@app.route("/api/upload_TODO/", methods=["POST"])
def upload_TODO():
	TODO_file = request.files['TODO']
	TODO = TODO_file.stream.read().decode('utf-8')

	TODO_data = get_TODO_data(TODO)

	insert_TODO_data(TODO_data)

	return redirect('/')