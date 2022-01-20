from flask import redirect, url_for, render_template
from mysite import *

from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *


@app.route("/")
def index():
    return redirect(url_for('home'))