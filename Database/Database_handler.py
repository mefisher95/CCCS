
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime

from mysite import db, app, database_config
from mysite.utils.error_logger import log_error
from mysite.utils.security_utils import hashfun, randstring

from mysite.Database.Announcements import Announcements
from mysite.Database.Users import Users
from mysite.Database.Registration import Registrations


# USER_LENGTH = app.config['USER_LENGTH']
# EMAIL_LENGTH = app.config['EMAIL_LENGTH']
# HASHEDPASSWORD_LENGTH = app.config['HASHED_PASSWORD_LENGTH']
# SALT_LENGTH = app.config['SALT_LENGTH']
# RANDOM_LENGTH = app.config['RANDOM_LENGTH']

# TABLE_ARGS = { 'extend_existing': True,
#                'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8',
#                'mysql_collate': 'utf8_general_ci' }



class Database_handler():
    def __init__(self) -> None:

        self.db = db

        if not database_exists(database_config.SQLALCHEMY_DATABASE_URI):

            try:
                create_database(database_config.SQLALCHEMY_DATABASE_URI)
            except Exception as error:
                log_error(error)

        self.db.create_all()

    def add_registration(self, given_name: str, family_name : str, email : str, 
                         username : str, password : str, code : str ) -> bool:
        try:
            salt = randstring()
            hashedpassword = hashfun(password, salt)
            dtime = app.config['DTIME_FOR_REGISTRATION']
            expiration = datetime.now() + dtime

            self.db.session.add(Registrations(
                given_name = given_name,
                family_name = family_name,
                email = email,
                username = username,
                code = code,
                hashedpassword = hashedpassword,
                salt = salt,
                expiration = expiration
            ))

            self.db.session.commit()

            return True

        except Exception as error:
            log_error(error)
            return False

    def get_registrations(self, username : str, code : str) -> dict:
        # try:
        print('username', username)
        print('code', code)
        # registration:flask_sqlalchemy.BaseQuery = Registrations.query.filter_by(username=username, code=code).first()
        print('in reg')
        registration = self.db.session.query(
            Registrations.id,
            Registrations.given_name,
            Registrations.family_name,
            Registrations.email,
            Registrations.username,
            Registrations.hashedpassword,
            Registrations.salt,
            Registrations.expiration
        ).filter_by(username=username, code=code)
        return [x._asdict() for x in registration][0]
        # except Exception as error:
        #     log_error(error)
        #     return {}

    def delete_registration(self, id : int) -> bool:
        try:
            print('id:', id, type(id))
            Registrations.query.filter_by(id = str(id)).delete()
            print('are we here')
            self.db.session.commit()
            return True

        except Exception as error:
            log_error(error)
            return False

    def add_Announcement(self, message : str, event_time : datetime = None) -> bool:
        try:
            if event_time is "" : event_time = None
            self.db.session.add(Announcements(
                message = message,
                event_time = event_time,
                create_time = datetime.now()
            ))

            self.db.session.commit()

            return True

        except Exception as error:
            log_error(error)
            return False

    def get_all_Announcement(self) -> list:
        try:
            announcements = self.db.session.query(
                Announcements.event_time, 
                Announcements.create_time,
                Announcements.id,
                Announcements.message
            )

            return sorted([x._asdict() for x in announcements], key=lambda d: (d['event_time'] is not None, d['event_time']))

        except Exception as error:
            log_error(error)
            return []

    def delete_Announcement_list(self, announcement_list : list) -> bool:
        try:
            for id in announcement_list:
                Announcements.query.filter_by(id = id).delete()

            self.db.session.commit()
            return True
        except Exception as error:
            log_error(error)
            return False


    def add_User(self, given_name : str, family_name: str, email:str, username : str,  hashed_password : str, salt : str) -> bool:
        # try:
        print(given_name)
        print(family_name)
        print(username)
        print(hashed_password),
        print(salt)
        self.db.session.add(Users(
            given_name = given_name,
            family_name = family_name,
            email = email,
            username = username,
            hashedpassword = hashed_password,
            salt = salt
        ))

        self.db.session.commit()

        return True

        # except Exception as error:
        #     log_error(error)
        #     return False

    def delete_User(self, id : int) -> bool:
        try:
            Users.query.filter_by(id=id).delete()
            self.db.session.commit()
            return True

        except Exception as error:
            log_error(error)
            return False

    def get_User(self, id : int) -> dict:
        try:
            user = self.db.session.query(
                Announcements.event_time, 
                Announcements.create_time,
                Announcements.id,
                Announcements.message
            )

            return [x._asdict() for x in user][0]

        except Exception as error:
            log_error(error)
            return {}

    def get_all_Users(self) -> list:
        try:
            users = self.db.session.query(
                Users.id,
                Users.given_name,
                Users.family_name,
                Users.email,
                Users.username,
            )

            return sorted([x._asdict() for x in users], key=lambda d: (d['family_name'] is not None, d['family_name']))

        except Exception as error:
            log_error(error)
            return []