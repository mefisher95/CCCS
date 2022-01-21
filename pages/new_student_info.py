from flask import redirect, url_for, render_template
from mysite import *

from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *
from mysite.pages.site_info import *


@app.route(ROUTES['new_student_info'].link)
def why_cs():
    return render_template('new_student_info.html',
                            menu_data = MENU_LINKS,
                            site_data = SITE_DATA)