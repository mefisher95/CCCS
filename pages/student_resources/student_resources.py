import os
from flask import render_template, url_for
from mysite import *

from mysite.config import *
from mysite.pages.site_info import *


@app.route(ROUTES['student_resources'].link)
def student_resources():

    # all_professors = database_conn.get_all_Professors()
    all_courses = database_conn.get_all_Courses()


    return render_template(
        'student_resources_templates/student_resources.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA,
        # all_professors = all_professors,
        all_courses = all_courses
    )