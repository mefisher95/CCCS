from flask import redirect, request, url_for, render_template, session
from mysite import *


from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *
from mysite.pages.site_info import *
from mysite.utils.security_utils import *
from mysite.utils.SMTP_Email_access import send_email

@app.route(ROUTES['join_team'].link, methods=['GET', 'POST'])
def join_team():

    if request.method == 'POST':
        given_name = request.form['given_name']
        family_name = request.form['family_name']
        email = request.form['email']

        database_conn.add_join_team_request(
            given_name=given_name,
            family_name=family_name,
            email=email
            )

        return render_template(
            'dev_pages/successful_join_team.html',
            menu_data = MENU_LINKS,
            site_data = SITE_DATA
        )

    return render_template(
        'dev_pages/join_team.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA
    )

        # if database_conn.is_User(username, password):
        #     user = database_conn.get_User_by_Username(username)
        #     session['username'] = user['username']
        #     session['given_name'] = user['given_name']
        #     session['admin'] = user['admin']

        #     return redirect(url_for('home'))

    # return render_template('user_management_templates/login.html', 
    #                         menu_data = MENU_LINKS,
    #                         site_data = SITE_DATA)

