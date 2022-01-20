from mysite import app
from mysite.Database.Database_handler import Database_handler
from mysite.config.config_all import *

from flask import render_template

def load_page_data(): 
    import json
    with open('mysite/static/page-data.json') as page_data:
        return json.load(page_data)


@app.route("/site-documentation")
def documentation() -> None:
    """
    Page for displaying site documentation, as provided by doxygen https://www.doxygen.nl/index.html
    """

    db = Database_handler()

    menu_data = get_menu_links()
    site_data = get_site_data()
    page_data = load_page_data()

    return render_template('documentation.html',
                            menu_data = menu_data,
                            site_data = site_data,
                            page_data = page_data)
