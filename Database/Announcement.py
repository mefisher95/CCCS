from sqlalchemy import column
from mysite import db

class Announcement(db.Model):
    """
    creates announcements for display on the home page. 
    interface model for connecting to MySQL table 
    """

    __tablename__ = 'Announcement'
    id = db.Column(db.Integer, primary_key = True)
    message = db.Column(db.Text, nullable = False)
    event_time = db.Column(db.DateTime)
    create_time = db.Column(db.DateTime, nullable = False)