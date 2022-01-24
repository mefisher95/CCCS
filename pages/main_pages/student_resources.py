import os
from flask import render_template
from mysite import *

from mysite.config import *
from mysite.pages.site_info import *


@app.route(ROUTES['student_resources'].link)
def student_resources():
    

    return render_template(
        'student_resources.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA
    )