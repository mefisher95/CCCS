import os
from flask import render_template
from mysite import *

from mysite.config import *
from mysite.pages.site_info import *


@app.route('/ciss240')
def ciss240():
    

    return render_template(
        'ciss240.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA
    )