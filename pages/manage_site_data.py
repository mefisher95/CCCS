from flask import render_template, request
from mysite import app, database_conn
import datetime
# from mysite.config import *
from mysite.config.config_all import *

@app.route(ROUTES['manage_site_data'].link, methods = ['GET', 'POST'])
def manage_site_data() -> None:


    if request.method == "POST":
        event_date = request.form['event_date']
        event_message = request.form['event_message']
        
        delete_list = request.form.getlist('delete_list')
        print("delete_list", delete_list)
        print("event_date", type(event_date))
        print("event_message", event_message)

        if event_message is not "": database_conn.add_Announcement(event_message, event_date)
        if len(delete_list): database_conn.delete_Announcement_list(delete_list)

        print(request.form)
        # print('test', request.form(['announcement']))
        x = request.form.get('announcement_submit')
        print(x)


    all_announcements = database_conn.get_all_Announcements()


    return render_template('manage_site_data.html',
                            menu_data = MENU_LINKS,
                            site_data = SITE_DATA,
                            all_announcements = all_announcements)