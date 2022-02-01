from flask import redirect, render_template, request, url_for
from mysite import app, database_conn
import datetime
# from mysite.config import *
from mysite.config.config_all import *
from mysite.utils.security_utils import is_admin

@app.route(ROUTES['manage_site_data'].link, methods = ['GET', 'POST'])
def course_not_found() -> None:
    return render_template(
        'page_not_available/course_page_not_available.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA
        )