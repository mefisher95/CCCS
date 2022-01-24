from flask import url_for, render_template
from mysite import *

from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *
from mysite.pages.site_info import *



# from mysite.pages import site_documenation
# from mysite import


@app.route(ROUTES['home'].link)
def home():
    """
    central page for the site. default route in 
    """

    announcement_list = database_conn.get_all_Announcements()
    print(database_conn.get_all_Users())


    return render_template('home.html', 
                            menu_data = MENU_LINKS,
                            site_data = SITE_DATA,
                            all_announcements = announcement_list)