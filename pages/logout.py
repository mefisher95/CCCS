from flask import redirect, request, url_for, render_template, session
from mysite import *


from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *
from mysite.pages.site_info import *
from mysite.utils.security_utils import *
from mysite.utils.SMTP_Email_access import send_email

@app.route(ROUTES['logout'].link, methods=['GET', 'POST'])
def logout():

    print(session)

    session.clear()

    print(session)

    return redirect(url_for('home'))

    
