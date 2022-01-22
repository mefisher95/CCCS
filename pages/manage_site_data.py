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
            print(request.form['delete_user_submit'])
            user_id = request.form['delete_user_submit']
            database_conn.delete_User(user_id)

        if 'announcement_submit' in request.form:

            event_date = request.form['event_date']
            event_message = request.form['event_message']
            
            delete_list = request.form.getlist('delete_list')

            if event_message != "": database_conn.add_Announcement(event_message, event_date)
            if len(delete_list): database_conn.delete_Announcement_list(delete_list)

            # print('test', request.form(['announcement']))
            x = request.form.get('announcement_submit')

    all_announcements = database_conn.get_all_Announcements()
    all_users = database_conn.get_all_Users()


    return render_template('manage_site_data.html',
                            menu_data = MENU_LINKS,
                            site_data = SITE_DATA,
                            all_announcements = all_announcements,
                            all_users = all_users)