from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_login


app = Flask(__name__)
from mysite import views
from mysite import config





# import config
# from config import *



app.config.from_object(config.__name__)



app.secret_key = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
