from flask import redirect, render_template, request, url_for
from mysite import app, database_conn
import datetime
# from mysite.config import *
from mysite.config.config_all import *
from mysite.utils.security_utils import is_admin

@app.route(ROUTES['manage_site_data'].link, methods = ['GET', 'POST'])
def manage_site_data() -> None:

    if not is_admin(): return redirect(url_for('home'))


    if request.method == "POST":
        if 'toggle_admin_submit' in request.form:
            modify_admin_data = eval(request.form['toggle_admin_submit'])

            database_conn.set_User_admin(modify_admin_data['id'], not modify_admin_data['admin'])

        if 'delete_user_submit' in request.form:
            user_id = request.form['delete_user_submit']
            database_conn.delete_User(user_id)

        if 'delete_join_team_submit' in request.form:
            request_id = request.form['delete_join_team_submit']
            print(request_id)
            database_conn.delete_join_team_request(request_id)

        if 'delete_bug_report_submit' in request.form:
            bug_id = request.form['delete_bug_report_submit']
            database_conn.delete_bug_report(bug_id)
        
        if 'announcement_submit' in request.form:

            event_date = request.form['event_date']
            event_message = request.form['event_message']
            
            delete_list = request.form.getlist('delete_list')

            if event_message != "": database_conn.add_Announcement(event_message, event_date)
            if len(delete_list): database_conn.delete_Announcement_list(delete_list)


    all_announcements = database_conn.get_all_Announcements()
    all_users = database_conn.get_all_Users()
    all_join_requests = database_conn.get_all_join_team_requests()
    all_bug_reports = database_conn.get_all_bug_reports()



    return render_template(
        'site_management_templates/manage_site_data.html',
        menu_data = MENU_LINKS,
        site_data = SITE_DATA,
        all_announcements = all_announcements,
        all_users = all_users,
        all_join_requests = all_join_requests,
        all_bug_reports = all_bug_reports 
        )