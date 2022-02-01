from flask import redirect, render_template, request, url_for
from mysite import app, database_conn
import datetime
# from mysite.config import *
from mysite.config.config_all import *
from mysite.utils.security_utils import is_admin

@app.route(ROUTES['manage_site_data'].link, methods = ['GET', 'POST'])
def manage_site_data() -> None:

    if not is_admin(): return redirect(url_for('home'))


    if request.method == "POST":
        if 'create_department_submit' in request.form: create_department()

        if 'delete_course_submit' in request.form: delete_course()

        if 'delete_department_submit' in request.form: delete_department()

        if 'create_course_submit' in request.form: create_course()

        if 'toggle_admin_submit' in request.form: toggle_admin()

        if "create_professor_submit" in request.form: create_professor()

        if "delete_professor_submit" in request.form: delete_professor()

        if 'delete_user_submit' in request.form: delete_user()

        if 'delete_join_team_submit' in request.form: delete_join_request()

        if 'delete_bug_report_submit' in request.form: delete_bug_report()
        
        if 'announcement_submit' in request.form: create_announcement()

    all_announcements = database_conn.get_all_Announcements()
    all_users = database_conn.get_all_Users()
    all_join_requests = database_conn.get_all_join_team_requests()
    all_bug_reports = database_conn.get_all_bug_reports()
    all_professors = database_conn.get_all_Professors()
    all_departments = database_conn.get_all_Departments()
    all_courses = database_conn.get_all_Courses()


    return render_template(
        'site_management_templates/manage_site_data.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA,
        all_announcements = all_announcements,
        all_users = all_users,
        all_join_requests = all_join_requests,
        all_bug_reports = all_bug_reports,
        all_professors = all_professors, 
        all_departments = all_departments,
        all_courses = all_courses
        )

def create_course() -> None:
    dept_id = request.form['department_id']
    course_num = request.form['course_number']
    course_name = request.form['course_name']
    course_cred = request.form['course_credit']
    course_link = request.form['course_link']


    if course_link == "": 
        dep = database_conn.get_Department_by_id(dept_id)

        try:
            print('building handle', dep, course_num)
            print(dep['code'] + course_num)
            course_link = url_for(dep['code'] + course_num)
        
        except: 
            return redirect(url_for('course_not_found'))
            

    database_conn.add_Course(
        department_id=dept_id,
        course_num = course_num,
        course_name = course_name,
        credit_hour=course_cred, 
        course_link = course_link
    )

def delete_course() -> None:
    course_id = request.form['delete_course_submit']
    database_conn.delete_Course(course_id)

def create_department() -> None:
    dept_code = request.form['department_code']
    dept_name = request.form['department_name']
    database_conn.add_Department(
        code=dept_code,
        name=dept_name
    )

def delete_department() -> None:
    dept_id = request.form['delete_department_submit']
    database_conn.delete_Department(dept_id)

def toggle_admin() -> None:
    modify_admin_data = eval(request.form['toggle_admin_submit'])
    database_conn.set_User_admin(modify_admin_data['id'], not modify_admin_data['admin'])

def create_professor() -> None:
    prof_title = request.form['professor_title']
    prof_given_name = request.form['professor_given_name']
    prof_family_name = request.form['professor_family_name']
    prof_email = request.form['professor_email']

    database_conn.add_Professor(
        title=prof_title,
        given_name=prof_given_name,
        family_name=prof_family_name,
        email=prof_email
    )

def delete_professor() -> None:
    prof_id = request.form['delete_professor_submit']
    database_conn.delete_Professor(prof_id)  

def delete_user() -> None:
    user_id = request.form['delete_user_submit']
    database_conn.delete_User(user_id)

def delete_join_request() -> None:
    request_id = request.form['delete_join_team_submit']
    database_conn.delete_join_team_request(request_id)

def delete_bug_report() -> None:
    bug_id = request.form['delete_bug_report_submit']
    database_conn.delete_bug_report(bug_id)

def create_announcement() -> None:
    event_date = request.form['event_date']
    event_message = request.form['event_message']
    
    delete_list = request.form.getlist('delete_list')

    if event_message != "": database_conn.add_Announcement(event_message, event_date)
    if len(delete_list): database_conn.delete_Announcement_list(delete_list)
