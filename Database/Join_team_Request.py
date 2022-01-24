from mysite import db, app

class Join_team_Request(db.Model):
    """
    creates announcements for display on the home page. 
    interface model for connecting to MySQL table 
    """

    __tablename__ = 'Join_team_Request'
    id = db.Column(db.Integer, primary_key = True)
    
    create_time = db.Column(db.DateTime, nullable = False)

    given_name = db.Column(db.String(app.config['USER_LENGTH']), nullable=False)
    family_name = db.Column(db.String(app.config['USER_LENGTH']), nullable=False)
    email = db.Column(db.String(app.config['EMAIL_LENGTH']), nullable=False)

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}