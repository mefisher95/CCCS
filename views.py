from flask import url_for, render_template
from mysite import *
import json

from mysite.Database.Database_handler import Database_handler
from mysite.config.site_info import *



def load_page_data(): 
    with open('mysite/static/page-data.json') as page_data:
        return json.load(page_data)

# def load_data():
#     """
#     Stand in helper function that loads data from the the knowledge base and pipe it to pages
#     """
#     import json
#     with open('mysite/static/site-data.json') as site_data:
#         return json.load(site_data)


# @app.route("/")
# def index():
#     """
#     central page for the site. default route in 
#     """
#     # data = Menu_data.Menu_data()

#     db = Database_handler()

#     menu_data = get_menu_links()
#     site_data = get_site_data()
#     page_data = load_page_data()

#     print(menu_data)
#     print(site_data)

#     return render_template('home.html', 
#                             menu_data = menu_data,
#                             site_data = site_data,
#                             page_data = page_data)

# @app.route("/site-documentation")
# def documentation() -> None:
#     """
#     Page for displaying site documentation, as provided by doxygen https://www.doxygen.nl/index.html
#     """

#     db = Database_handler()

#     menu_data = get_menu_links()
#     site_data = get_site_data()
#     page_data = load_page_data()

#     return render_template('documentation.html',
#                             menu_data = menu_data,
#                             site_data = site_data,
#                             page_data = page_data)
