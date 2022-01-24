from flask import redirect, request, url_for, render_template
from mysite import *

from mysite.Database.Database_handler import Database_handler
from mysite.config import *
from mysite.pages.site_info import *
from mysite.utils.security_utils import *
from mysite.utils.SMTP_Email_access import send_email
from mysite.utils.email_util import *


@app.route(ROUTES['register'].link, methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        given_name = request.form['given_name']
        family_name = request.form['family_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        code = randstring()

        if database_conn.is_registration(email):
            redo_reg = database_conn.get_registration_by_email(email)
            database_conn.delete_registration(redo_reg['id'])

        database_conn.add_registration(
            given_name=given_name,
            family_name=family_name,
            email=email,
            username=username,
            password=password,
            code=code
        )

        send_email(email, 'Confirm-Registration', render_email(given_name, family_name, username, code))

        return render_template(
            'user_management_templates/complete_registration.html',
            menu_data = MENU_LINKS,
            site_data = SITE_DATA
        )
        


    return render_template('user_management_templates/registration.html', 
                            menu_data = MENU_LINKS,
                            site_data = SITE_DATA)

@app.route(ROUTES['finalize_register'].link, methods=['GET', 'POST'])
def finish_registration():
    if len(request.args) == 0:
        pass

    info = request.args
    username = info.get('user')
    code = info.get('code')

    registration = database_conn.get_registrations(username, code)

    if registration is not None:
        if datetime.datetime.now() <  registration['expiration']:

            database_conn.delete_registration(registration['id'])
            database_conn.add_User(
                username = registration['username'],
                email = registration['email'],
                family_name=registration['family_name'],
                given_name=registration['given_name'],
                hashed_password=registration['hashedpassword'],
                salt=registration['salt']
            )

            return redirect(url_for('home'))

@app.route(ROUTES['resend_registration'].link, methods=['GET', 'POST'])
def resend_registration():

    if request.method == 'POST':
        email = request.form['email']

        if database_conn.is_registration(email):
            reg = database_conn.get_registration_by_email(email)
            print(reg)
            database_conn.delete_registration(reg['id'])

            code = randstring()
            database_conn.add_registration(
                given_name=reg['given_name'],
                family_name=reg['family_name'],
                email = reg['email'],
                username=reg['username'],
                password=reg['hashedpassword'],
                code = code
            )
            
            send_email(
                email, 
                'Confirm-Registration', 
                render_email(
                    reg['given_name'], 
                    reg['family_name'], 
                    reg['username'], 
                    code = code
                    )
                )

        return render_template(
            'user_management_templates/complete_registration.html', 
            menu_data = MENU_LINKS,
            site_data = SITE_DATA
            )

    return render_template(
        'user_management_templates/resend_registration.html', 
        menu_data = MENU_LINKS,
        site_data = SITE_DATA
        )