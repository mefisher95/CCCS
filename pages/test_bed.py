from flask import redirect, url_for, render_template
from mysite import *

from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *
from mysite.pages.site_info import ROUTES


@app.route('/test_bed')
def test_besd():
    return redirect(url_for('course_template', course_code = "CISS", course_num = "240"))