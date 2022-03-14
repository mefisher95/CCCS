from sqlalchemy import ForeignKey
from mysite import db

class Software(db.Model):
    """
    MySql table for Courses that are accesses by authorized students
    and managed through manage_site
    """

    __tablename__ = 'Software'
    id = db.Column(db.Integer, primary_key = True)
    software_name = db.Column(db.String(256), nullable = False)
    link = db.Column(db.Text, nullable=False)

    def as_dict(self) -> dict:
        """
        generates a dicitionary for a record by assigning the key:values based on the 
        table column names and corresponding records
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}