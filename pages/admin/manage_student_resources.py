from flask import redirect, render_template, request, url_for
from mysite import app, database_conn
import mysite
# from mysite.config import *
from mysite.config.config_all import *
from mysite.utils.security_utils import is_admin

import os, shutil

@app.route(ROUTES['manage_student_resources'].link, methods = ['GET', 'POST'])
def manage_student_resources() -> None:

    if not is_admin(): return redirect(url_for('home'))

    if request.method == "POST":
        print(request.form)
        if 'create_department_submit' in request.form: create_department()

        if 'delete_course_submit' in request.form: delete_course()

        if 'delete_department_submit' in request.form: delete_department()

        if 'create_course_submit' in request.form: create_course()

        if 'create_software_submit' in request.form: create_software()

        if 'delete_software_submit' in request.form: delete_software()

        if 'create_tutorial_submit' in request.form: create_tutorial()

        if 'delete_tutorial_submit' in request.form: delete_tutorial()


    all_departments = database_conn.get_all_Departments()
    all_courses = database_conn.get_all_Courses()
    all_software = database_conn.get_all_Software()
    all_tutorials = database_conn.get_all_Tutorial()


    return render_template(
        'student_resources_management_templates/manage_student_resources.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA,
        all_departments = all_departments,
        all_courses = all_courses, 
        all_software = all_software,
        all_tutorials = all_tutorials
        )

def create_tutorial() -> None:
    if not os.path.isdir('mysite/static/tutorials'): os.mkdir('mysite/static/tutorials')
    
    files = request.files.getlist("tutorial_list")
    
    for fl in files: 
        filepath ='static/tutorials/' + fl.filename
        fl.save('mysite/' + filepath) 

        database_conn.add_Tutorial(
            tutorial_name=fl.filename,
            pdf_link=filepath
        )

def delete_tutorial() -> None: 
    tutorial_id = request.form['delete_tutorial_submit']
    tutorial = database_conn.get_Tutorial_by_ID(tutorial_id)

    filepath = 'mysite/static/tutorials/' + tutorial['tutorial_name']
    os.remove(filepath) 

    database_conn.remove_Tutorial(tutorial_id)

def create_software() -> None:
    software_name = request.form['software_name']
    link = request.form['software_link']

    print(software_name, link)

    database_conn.add_Software(
        software_name=software_name,
        link=link
    )

def delete_software() -> None:
    software_id = request.form['delete_software_submit']
    database_conn.remove_Software(software_id)

def create_course() -> None:

    dept_id = request.form['department_id']
    course_num = request.form['course_number']
    course_name = request.form['course_name']
    course_cred = request.form['course_credit']
    course_link = request.form['course_link']


    if course_link == "": 
        dep = database_conn.get_Department_by_id(dept_id)

        # try:
        course_link = url_for('course_template', course_code = dep['code'], course_num = course_num)
        print(course_link)

        if not os.path.isdir('mysite/static/courses'): os.mkdir('mysite/static/courses')

        course_dir = 'mysite/static/' + course_link
        overview = course_dir + '/overview'
        notes = course_dir + '/notes'
        assignments = course_dir + '/assignments'
        quizzes = course_dir + '/quizzes'
        project = course_dir + '/project'
        
        if not os.path.isdir(course_dir): os.mkdir(course_dir)
        if not os.path.isdir(overview): os.mkdir(overview)
        if not os.path.isdir(assignments): os.mkdir(assignments)
        if not os.path.isdir(quizzes): os.mkdir(quizzes)
        if not os.path.isdir(project): os.mkdir(project)
        if not os.path.isdir(notes): os.mkdir(notes)

    database_conn.add_Course(
        department_id=dept_id,
        course_num = course_num,
        course_name = course_name,
        credit_hour=course_cred, 
        course_link = course_link
    )

def delete_course() -> None:
    course_id = request.form['delete_course_submit']
    course = database_conn.get_Course_by_id(course_id)

    course_dir = "mysite/static/courses/" + course['department']['code'] + '-' + str(course['course_num'])

    shutil.rmtree(course_dir, ignore_errors=True)

    database_conn.delete_Course(course_id)
    
    return None


def create_department() -> None:
    dept_code = request.form['department_code']
    dept_name = request.form['department_name']
    database_conn.add_Department(
        code=dept_code,
        name=dept_name
    )

    return None

def delete_department() -> None:
    dept_id = request.form['delete_department_submit']
    database_conn.delete_Department(dept_id)

