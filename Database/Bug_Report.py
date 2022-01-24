from mysite import db, app

class Bug_Report(db.Model):
    """
    creates announcements for display on the home page. 
    interface model for connecting to MySQL table 
    """

    __tablename__ = 'Bug_Report'
    id = db.Column(db.Integer, primary_key = True)
    
    create_time = db.Column(db.DateTime, nullable = False)
    message = db.Column(db.Text, nullable = False)



    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}