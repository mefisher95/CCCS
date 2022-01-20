from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
import flask_login


# from mysite.config import config_all, flask_config, database_config

from mysite.config import *

app = Flask(__name__)


app.config.from_object(config.__name__)



app.secret_key = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

login_manager = flask_login.LoginManager()
# login_manager.init_app(app)

### import last
# from mysite.pages import index
from mysite import pages, config, Database

