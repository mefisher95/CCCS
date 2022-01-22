from flask import redirect, request, url_for, render_template, session
from mysite import *


from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *
from mysite.pages.site_info import *
from mysite.utils.security_utils import *
from mysite.utils.SMTP_Email_access import send_email

@app.route(ROUTES['login'].link, methods=['GET', 'POST'])
def login():
    if request.method == "POST":

        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            if database_conn.is_User(username, password):
                user = database_conn.get_User_by_Username(username)
                session['username'] = user['username']
                session['given_name'] = user['given_name']
                session['admin'] = user['admin']

                return redirect(url_for('home'))

    return render_template('login.html', 
                            menu_data = MENU_LINKS,
                            site_data = SITE_DATA)

