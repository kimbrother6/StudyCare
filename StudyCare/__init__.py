from flask import Flask, Response, redirect, render_template
from functions.create.templates import get_todo_template
from settings import settings

app = Flask(__name__)

@app.route("/")
def home_page():
	return render_template('home-page.html')


@app.route("/api/download_todo_template")
def download_todo_template():	

	template, template_name = get_todo_template(settings['reference_day'])
	
	response = Response(template, mimetype='text/plain')

	#다운로드하게 리스폰스 헤더 설정
	response.headers["Content-Disposition"] = f"attachment; filename={template_name}"

	return response

@app.route("/api/setting/reference_day/<int:reference_day>")
def set_reference_day(reference_day):
	settings['reference_day'] = reference_day
	print(settings)
	return redirect('/')    

