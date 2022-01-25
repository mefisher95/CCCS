from mysite import db
from mysite.utils.SMTP_Email_access import send_email

class Bug_Report(db.Model):
    """
    MySql table for Bug Reports that are submitted by users and managed on
    the site management page
    """

    __tablename__ = 'Bug_Report'
    id = db.Column(db.Integer, primary_key = True)
    
    create_time = db.Column(db.DateTime, nullable = False)
    message = db.Column(db.Text, nullable = False)

    

    def as_dict(self) -> dict:
        """
        generates a dicitionary for a record by assigning the key:values based on the 
        table column names and corresponding records
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    x = 1