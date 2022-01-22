from flask import redirect, request, url_for, render_template
from mysite import *

from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *
from mysite.pages.site_info import *
from mysite.utils.security_utils import *
from mysite.utils.SMTP_Email_access import send_email



# from mysite.pages import site_documenation
# from mysite import

def render_email(fname, lname, username, code):
    url = generate_register_url(username, code)
    return render_template('DNR.html', fname=fname, lname=lname, url=url)

def generate_register_url(user, code):
     url = str(url_for('finish_registration', _external=True)) + '?'
     user = "user=" + user
     code = "code=" + code
     return url + user + '&' + code


@app.route(ROUTES['register'].link, methods=['GET', 'POST'])
def registration():
    if request.method == "POST":
        given_name = request.form['given_name']
        family_name = request.form['family_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        code = randstring()

        database_conn.add_registration(
            given_name=given_name,
            family_name=family_name,
            email=email,
            username=username,
            password=password,
            code=code
        )

        send_email(email, 'Confirm-Registration', render_email(given_name, family_name, username, code))
        


    return render_template('registration.html', 
                            menu_data = MENU_LINKS,
                            site_data = SITE_DATA)

@app.route(ROUTES['finalize_register'].link, methods=['GET', 'POST'])
def finish_registration():
    if len(request.args) == 0:
        pass

    info = request.args
    username = info.get('user')
    code = info.get('code')
    print('info',info)
    print(username, code)
    registration = database_conn.get_registrations(username, code)
    print('tracking........')
    print(registration)
    print(registration['expiration'])

    if registration is not None:
        if datetime.datetime.now() <  registration['expiration']:
            print('in the loop')
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
        return "error"

