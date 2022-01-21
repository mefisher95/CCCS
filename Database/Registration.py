from mysite import db, app

TABLE_ARGS = { 'extend_existing': True,
               'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8',
               'mysql_collate': 'utf8_general_ci' }


class Registrations(db.Model):
    __tablename__ = 'Registrations'
    __tableargs__ = TABLE_ARGS

    id = db.Column(db.Integer, primary_key=True)
    given_name = db.Column(db.String(app.config['USER_LENGTH']), nullable=False)
    family_name = db.Column(db.String(app.config['USER_LENGTH']), nullable=False)
    email = db.Column(db.String(app.config['EMAIL_LENGTH']), unique=True, nullable=False)
    username = db.Column(db.String(app.config['USER_LENGTH']), unique=True, nullable=False)
    hashedpassword = db.Column(db.String(app.config['HASHED_PASSWORD_LENGTH']), nullable=False)
    salt = db.Column(db.String(app.config['SALT_LENGTH']), nullable=False)
    code = db.Column(db.String(app.config['RANDOM_LENGTH']), nullable=False)
    expiration = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Registration %s %s %s %s %s %s %s %s %s>' % \
            (self.id, self.given_name, self.family_name, self.username, self.email, self.hashedpassword,
             self.salt, self.code, self.expiration)
