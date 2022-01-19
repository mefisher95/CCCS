from mysite import db

class Menu_data(db.Model):
    __tablename__ = 'Menu_data'
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)