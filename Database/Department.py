from sqlalchemy import ForeignKey
from mysite import db, app

class Department(db.Model):
    """
    MySql table for Courses that are accesses by authorized students
    and managed through manage_site
    """

    __tablename__ = 'Department'
    id = db.Column(db.Integer, primary_key = True)
    code = db.Column(db.String(4), nullable=False, unique=True)
    name = db.Column(db.String(128), nullable=False, unique=True)

    def as_dict(self) -> dict:
        """
        generates a dicitionary for a record by assigning the key:values based on the 
        table column names and corresponding records
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}