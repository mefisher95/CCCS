from mysite import db

class Site_data(db.Model):
    __tablename__ = 'Site_data'
    id = db.Column(db.Integer, primary_key=True)
    site_title = db.Column(db.String(64))
    site_logo = db.Column(db.String(128))
    fav_icon = db.Column(db.String(128))
    # menu_links = db.Column(db.Integer, db.ForeignKey('menu_links.id'))