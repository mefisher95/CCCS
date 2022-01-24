from mysite import db

class Announcements(db.Model):
    """
    MySql table for Announcements that is displayed on the home page and is managed
    through manage_site_data
    """

    __tablename__ = 'Announcements'
    id = db.Column(db.Integer, primary_key = True) 
    message = db.Column(db.Text, nullable = False)
    event_time = db.Column(db.DateTime)
    create_time = db.Column(db.DateTime, nullable = False)

    def as_dict(self) -> dict:
        """
        generates a dicitionary for a record by assigning the key:values based on the 
        table column names and corresponding records
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}