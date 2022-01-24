from mysite import db, app

class Users(db.Model):
    """
    MySql table for Usesrs that represents all user management on the site. 
    Can be managed through the site management page
    """
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key = True)
    given_name = db.Column(db.String(app.config['USER_LENGTH']), nullable=False)
    family_name = db.Column(db.String(app.config['USER_LENGTH']), nullable=False)
    email = db.Column(db.String(app.config['EMAIL_LENGTH']), unique=True, nullable=False)
    username = db.Column(db.String(app.config['USER_LENGTH']), unique=True, nullable=False)
    hashedpassword = db.Column(db.String(app.config['HASHED_PASSWORD_LENGTH']), nullable=False)
    salt = db.Column(db.String(app.config['SALT_LENGTH']), nullable=False)
    admin = db.Column(db.Boolean, default=False)

    def as_dict(self) -> dict:
        """
        generates a dicitionary for a record by assigning the key:values based on the 
        table column names and corresponding records
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}