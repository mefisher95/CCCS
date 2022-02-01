from urllib import response
from flask import redirect, render_template, session, url_for
from mysite import *

from mysite.config import *
from mysite.pages.site_info import *

from mysite.utils.security_utils import is_admin


@app.route('/view_quizzes<args>', methods=['GET', 'POST'])
def view_quiz(args):
    args = eval(args)
    course_id = args['course_id']
    quiz_id = args['quiz_id']

    if not is_allowed_course_access(course_id=course_id): return redirect(url_for('home'))
    quiz_page = database_conn.get_Course_Quiz_by_ID(quiz_id=quiz_id)
    
    return render_template(
        'view_pdf.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA,
        link = quiz_page['pdf_link']
    )
    

def is_allowed_course_access(course_id : int) -> response:
    return is_enrolled(course_id) or is_admin()

def is_enrolled(course_id : int) -> bool:
    if 'id' not in session: return False
    return session['id'] in [user['User_id'] for user in database_conn.get_all_Users_in_Course(course_id)]

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

