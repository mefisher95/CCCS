from flask import render_template, url_for

def render_email(fname, lname, username, code):
    url = generate_register_url(username, code)
    return render_template('DNR.html', fname=fname, lname=lname, url=url)

def generate_register_url(user, code):
     url = str(url_for('finish_registration', _external=True)) + '?'
     user = "user=" + user
     code = "code=" + code
     return url + user + '&' + code
