from flask.templating import render_template
from mysite import *

# from app.Menu_data import Menu_data

def load_data():
    import json
    with open('mysite/static/site-data.json') as site_data:
        return json.load(site_data)


@app.route("/")
def index():
    # data = Menu_data.Menu_data()

    menu_data = load_data()

    return render_template('home.html', menu_data = menu_data)

@app.route("/site-documentation")
def documentation() -> None:
    menu_data = load_data()

    return render_template('documentation.html', menu_data = menu_data)
