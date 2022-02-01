from sqlalchemy import ForeignKey
from mysite import db, app

class Courses(db.Model):
    """
    MySql table for Courses that are accesses by authorized students
    and managed through manage_site
    """

    __tablename__ = 'Courses'
    id = db.Column(db.Integer, primary_key = True)
    department_id = db.Column(db.Integer, ForeignKey('Department.id'), nullable=False)
    # professor_id = db.Column(db.Integer, ForeignKey('Professor.id'), nullable=False)
    course_num = db.Column(db.Integer, nullable=False)
    course_name = db.Column(db.String(128), nullable=False)
    credit_hour = db.Column(db.Integer, nullable=False)
    link = db.Column(db.Text, nullable=True)

    def as_dict(self) -> dict:
        """
        generates a dicitionary for a record by assigning the key:values based on the 
        table column names and corresponding records
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}