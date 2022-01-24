from flask import redirect, request, url_for, render_template, session
from mysite import *


from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *
from mysite.pages.site_info import *
from mysite.utils.security_utils import *
from mysite.utils.SMTP_Email_access import send_email

@app.route(ROUTES['report_bug'].link, methods=['GET', 'POST'])
def report_bug():

    if request.method == 'POST':
        bug_desc = request.form['bug_desc']

        report_id = database_conn.add_bug_report(bug_desc)

        for user in database_conn.get_all_admins():
            send_email(
                user['email'], 
                "Bug Report #{0}:".format(report_id), 
                "Bug Reoprt Generated:\n\n" + bug_desc)

        return render_template(
            'dev_pages/successful_report_bug.html',
            menu_data = MENU_LINKS,
            site_data = SITE_DATA
        )

    return render_template(
        'dev_pages/report_bug.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA
    )
