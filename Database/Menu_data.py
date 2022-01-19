<<<<<<< HEAD
from mysite import db

class Menu_data(db.Model):
    __tablename__ = 'Menu_data'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(128), nullable=False)
=======
from mysite import db



class Menu_data(db.Model):
    """
        SQLAlchemy class to support python datamodel conversion with sql table
    """
    __tablename__ = 'Menu_data'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(128), nullable=False)
>>>>>>> e2e6fc0c922c83f7983f8bf5efac2ba4dbd92102
    name = db.Column(db.String(128), nullable=False)