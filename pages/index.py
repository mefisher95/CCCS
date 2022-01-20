from flask import url_for, render_template
from mysite import *

from mysite.Database.Database_handler import Database_handler
# from mysite.config.site_info import *
from mysite.config import *

# from mysite.pages import site_documenation
# from mysite import



def load_page_data(): 
    import json

    with open('mysite/static/page-data.json') as page_data:
        return json.load(page_data)


@app.route("/")
def index():
    """
    central page for the site. default route in 
    """
    # data = Menu_data.Menu_data()

    db = Database_handler()

    menu_data = get_menu_links()
    site_data = get_site_data()
    page_data = load_page_data()

    print(menu_data)
    print(site_data)

    return render_template('home.html', 
                            menu_data = menu_data,
                            site_data = site_data,
                            page_data = page_data)