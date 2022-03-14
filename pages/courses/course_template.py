import re
from urllib import response
from flask import redirect, render_template, render_template_string, request, session, url_for
from sqlalchemy import over
from mysite import *
import mysite
import os

from mysite.config import *
from mysite.pages.site_info import *

from mysite.utils.security_utils import is_admin


@app.route('/courses/<course_code>-<course_num>', methods=['GET', 'POST'])
def course_template(course_code, course_num):
    course_data = get_course_data(course_code, course_num)
    course_name = course_data['department']['code'] + '-' + str(course_data['course_num'])


    if request.method == "POST":
        if 'create_overview_submit' in request.form:
            file = request.files.get('overview_file')
            print(file)

            filepath ='static/courses/' + course_name + '/overview/' + course_name + '.html'
            file.save('mysite/' + filepath)


        if 'toggle_enroll_submit' in request.form:
            modify_enrollment_data = eval(request.form['toggle_enroll_submit'])
            if not modify_enrollment_data['enrolled']:
                database_conn.add_Course_Assignment(
                    modify_enrollment_data['id'],
                    course_data['id']
                )
            else:
                database_conn.remove_User_from_Course_Assignment(
                    modify_enrollment_data['id'],
                    course_data['id']
                )

        if 'create_notes_submit' in request.form:
            files = request.files.getlist("notes_list")
            for fl in files: 
                filepath ='static/courses/' + course_name + '/notes/' + fl.filename
                fl.save('mysite/' + filepath) 

                database_conn.add_Course_Notes(
                    course_id=course_data['id'],
                    notes_name=fl.filename,
                    pdf_link=filepath
                )

        if 'delete_notes_submit' in request.form:
            notes_id = request.form['delete_notes_submit']
            note = database_conn.get_Course_Notes_by_ID(notes_id)

            filepath = 'mysite/static/courses/' + course_name + '/notes/' + note['notes_name']
            os.remove(filepath) 

            database_conn.remove_Course_Notes_from_Course(notes_id)
        
        if 'view_notes_submit' in request.form:
            return redirect(url_for('view_notes', args={'course_id' : course_data['id'], 'notes_id' : request.form['view_notes_submit']}))

        if 'create_assignments_submit' in request.form:
            files = request.files.getlist('assignments_list')

            for fl in files: 
                filepath ='static/courses/' + course_name + '/assignments/' + fl.filename
                fl.save('mysite/' + filepath) 

                database_conn.add_Course_Homework(
                    course_id = course_data['id'],
                    homework_name=fl.filename,
                    pdf_link = filepath,
                )


        if 'delete_assignment_submit' in request.form:
            assignment_id = request.form['delete_assignment_submit']
            assignment = database_conn.get_Course_Homework_by_ID(assignment_id)

            filepath = 'mysite/static/courses/' + course_name + '/assignments/' + assignment['homework_name']
            os.remove(filepath)
            database_conn.remove_Course_Homework_from_Course(assignment_id)

        if 'view_assignment_submit' in request.form:
            return redirect(url_for('view_assignment', args={'course_id' : course_data['id'], 'assignment_id' : request.form['view_assignment_submit']}))
    
        if 'create_quiz_submit' in request.form:
            files = request.files.getlist('quiz_list')

            for fl in files:
                filepath = 'static/courses/' + course_name + '/quizzes/' + fl.filename
                fl.save('mysite/' + filepath)
                database_conn.add_Course_Quiz(
                    course_id=course_data['id'],
                    quiz_name=fl.filename,
                    pdf_link=filepath,
                )

        if 'delete_quiz_submit' in request.form:
            quiz_id = request.form['delete_quiz_submit']
            quiz = database_conn.get_Course_Quiz_by_ID(quiz_id)
            filepath = 'mysite/static/courses/' + course_name + '/quizzes/' + quiz['quiz_name']
            os.remove(filepath)

            database_conn.remove_Course_Quiz_from_Course(quiz_id)

        if 'view_quiz_submit' in request.form:
            return redirect(url_for('view_quiz', args={'course_id' : course_data['id'], 'quiz_id' : request.form['view_quiz_submit']}))

        if 'create_project_submit' in request.form:

            files = request.files.getlist('project_list')

            for fl in files:
                filepath = "static/courses/" + course_name + '/project/' + fl.filename
                fl.save('mysite/' + filepath)

                database_conn.add_Course_Project(
                    course_id=course_data['id'],
                    project_name=fl.filename,
                    pdf_link=filepath,
                )

        if 'delete_project_submit' in request.form:
            project_id = request.form['delete_project_submit']
            project = database_conn.get_Course_Project_by_ID(project_id)

            filepath = 'mysite/static/courses/' + course_name + '/project/' + project['project_name']
            os.remove(filepath)
            database_conn.remove_Course_Project_from_Course(project_id)

        if 'view_project_submit' in request.form:
            return redirect(url_for('view_project', args={'course_id' : course_data['id'], 'project_id' : request.form['view_project_submit']}))


    if not is_allowed_course_access(course_data['id']): 
        return redirect(url_for('student_resources'))

    if is_admin(): 
        all_users = get_user_data(course_data['id'])
    else: all_users = None


    all_notes = database_conn.get_all_Course_Notes_in_Course(course_data['id'])
    all_assignments = database_conn.get_all_Course_Homework_in_Course(course_data['id'])
    all_quizzes = database_conn.get_all_Course_Quizzes_in_Course(course_data['id'])
    all_projects = database_conn.get_all_Course_Projects_in_Course(course_data['id'])
    overview = get_overview_data(course_name)


    return render_template(
        'courses/course_skeleton.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA,
        course_data = course_data,
        course_name = course_name,
        overview = overview,
        all_users = all_users,
        all_notes = all_notes,
        all_assignments = all_assignments, 
        all_quizzes = all_quizzes,
        all_projects = all_projects
    )

def is_allowed_course_access(course_id : int) -> response:
    return is_enrolled(course_id) or is_admin()

def is_enrolled(course_id : int) -> bool:
    if 'id' not in session: return False
    return session['id'] in [user['User_id'] for user in database_conn.get_all_Users_in_Course(course_id)]
    pass

def get_user_data(course_id : int) -> list:
    all_users = database_conn.get_all_Users()
    users_in_course = database_conn.get_all_Users_in_Course(course_id)

    for user in all_users: 
        print(user['id'])
        user['enrolled'] = True if user['id'] in [x['User_id'] for x in users_in_course] else False

    return all_users

def get_course_data(dept_tag : str, course_num : int) -> dict:
    dept_tag = database_conn.get_Department_by_code(dept_tag.upper())
    return database_conn.get_Course_by_course_code(dept_tag['id'], course_num)

def get_overview_data(course_name: str) -> str:
    try: overview = open('mysite/static/courses/' + course_name + '/overview/' + course_name + '.html', 'r').read()
    except: overview = ""
    return overview

