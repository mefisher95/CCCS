from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# from mysite.config import config_all, flask_config, database_config

from mysite.config import *

app = Flask(__name__)


app.config.from_object(config.__name__)



app.secret_key = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

from mysite import Database
database_conn = Database.Database_handler()

# login_manager.init_app(app)

### import last
# from mysite.pages import index
from mysite import pages, config

