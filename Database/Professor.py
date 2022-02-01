from email.policy import default
from mysite import db, app

class Professor(db.Model):
    """
    MySql table for Professors that are accesses by courses and info pages
    and managed through manage_site
    """

    __tablename__ = 'Professor'
    id = db.Column(db.Integer, primary_key = True)
    
    title = db.Column(db.String(8), default="Dr.")
    given_name = db.Column(db.String(app.config['USER_LENGTH']), nullable=False)
    family_name = db.Column(db.String(app.config['USER_LENGTH']), nullable=False)
    email = db.Column(db.String(app.config['EMAIL_LENGTH']), unique=True, nullable=False)

    def as_dict(self) -> dict:
        """
        generates a dicitionary for a record by assigning the key:values based on the 
        table column names and corresponding records
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}