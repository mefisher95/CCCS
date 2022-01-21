import os
from flask import redirect, url_for, render_template
from mysite import *
import mysite

from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *
from mysite.pages.site_info import *


@app.route(ROUTES['new_student_info'].link)
def new_student_info():
    
    pics = [x for x in os.listdir('mysite/static/images/PiCS_gallery/')]
    # with open(url_for('static', 'images/PiCS_gallery'))

    return render_template('new_student_info.html',
                            menu_data = MENU_LINKS,
                            site_data = SITE_DATA,
                            pictures_urls = pics)