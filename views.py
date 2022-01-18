from flask.templating import render_template
from mysite import *

# from app.Menu_data import Menu_data

def load_data():
    """
    Stand in helper function that loads data from the the knowledge base and pipe it to pages
    """
    import json
    with open('mysite/static/site-data.json') as site_data:
        return json.load(site_data)


@app.route("/")
def index():
    """
    central page for the site. default route in 
    """
    # data = Menu_data.Menu_data()

    menu_data = load_data()

    return render_template('home.html', menu_data = menu_data)

@app.route("/site-documentation")
def documentation() -> None:
    """
    Page for displaying site documentation, as provided by doxygen https://www.doxygen.nl/index.html
    """
    menu_data = load_data()

    return "/static/HTML/autodoc/index.html"
