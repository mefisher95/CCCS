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

        database_conn.add_bug_report(bug_desc)

        # database_conn.add_join_team_request(
        #     given_name=given_name,
        #     family_name=family_name,
        #     email=email
        #     )

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
