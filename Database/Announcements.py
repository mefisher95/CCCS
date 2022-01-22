from mysite import db

class Announcements(db.Model):
    """
    creates announcements for display on the home page. 
    interface model for connecting to MySQL table 
    """

    __tablename__ = 'Announcements'
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.Text, nullable = False)
    event_time = db.Column(db.DateTime)
    create_time = db.Column(db.DateTime, nullable = False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}