from mysite import app
from mysite.Database.Database_handler import Database_handler
from mysite.config.config_all import *

from flask import redirect, render_template, session, url_for
from mysite.utils.security_utils import is_admin

@app.route(ROUTES['document'].link)
def documentation() -> None:
    """
    Page for displaying site documentation, as provided by doxygen https://www.doxygen.nl/index.html
    """

    if not is_admin(): return redirect(url_for('home'))


    return render_template('documentation.html',
                            menu_data = MENU_LINKS,
                            site_data = SITE_DATA)
