from email.policy import default
from mysite import db, app

class Users(db.Model):
    """
    creates Users for display on the home page. 
    interface model for connecting to MySQL table 
    """
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    given_name = db.Column(db.String(app.config['USER_LENGTH']), nullable=False)
    family_name = db.Column(db.String(app.config['USER_LENGTH']), nullable=False)
    email = db.Column(db.String(app.config['EMAIL_LENGTH']), unique=True, nullable=False)
    username = db.Column(db.String(app.config['USER_LENGTH']), unique=True, nullable=False)
    hashedpassword = db.Column(db.String(app.config['HASHED_PASSWORD_LENGTH']), nullable=False)
    salt = db.Column(db.String(app.config['SALT_LENGTH']), nullable=False)
    admin = db.Column(db.Boolean, default=False)