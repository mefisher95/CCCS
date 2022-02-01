from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from mysite.config import *

# from mysite.config import config_all, flask_config, database_config


app = Flask(__name__)


app.config.from_object(config.__name__)



app.secret_key = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
db = SQLAlchemy(app)

from mysite import Database

database_conn = Database.Database_handler()

# login_manager.init_app(app)

### import last
# from mysite.pages import index
from mysite import config, pages
