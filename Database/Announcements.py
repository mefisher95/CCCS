from mysite import db

class Announcements(db.Model):
    """
    MySql table for Announcements that is displayed on the home page and is managed
    through manage_site_data
    """

    __tablename__ = 'Announcements'
    """index id for record in table"""
    id = db.Column(db.Integer, primary_key = True) 

    message = db.Column(db.Text, nullable = False) #announcement message to be displayed 
    event_time = db.Column(db.DateTime) # the date of the event that the announcement takes place
    create_time = db.Column(db.DateTime, nullable = False) # timestamp for the creation of the announcement 

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}