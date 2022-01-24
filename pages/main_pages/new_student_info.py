import os
from flask import render_template
from mysite import *

from mysite.config import *
from mysite.pages.site_info import *


@app.route(ROUTES['new_student_info'].link)
def new_student_info():
    
    pics = [x for x in os.listdir('mysite/static/images/PiCS_gallery/')]

    return render_template('new_student_info.html',
                            menu_data = MENU_LINKS,
                            site_data = SITE_DATA,
                            pictures_urls = pics)