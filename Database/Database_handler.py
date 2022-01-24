from sqlalchemy_utils import database_exists, create_database
from datetime import datetime

from mysite import db, app, database_config
from mysite.Database.Bug_Report import Bug_Report
from mysite.utils.error_logger import log_error
from mysite.utils.security_utils import hashfun, randstring

from mysite.Database.Announcements import Announcements
from mysite.Database.Users import Users
from mysite.Database.Registration import Registrations
from mysite.Database.Join_team_Request import Join_team_Request
from mysite.Database.Bug_Report import Bug_Report


# USER_LENGTH = app.config['USER_LENGTH']
# EMAIL_LENGTH = app.config['EMAIL_LENGTH']
# HASHEDPASSWORD_LENGTH = app.config['HASHED_PASSWORD_LENGTH']
# SALT_LENGTH = app.config['SALT_LENGTH']
# RANDOM_LENGTH = app.config['RANDOM_LENGTH']

# TABLE_ARGS = { 'extend_existing': True,
#                'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8',
#                'mysql_collate': 'utf8_general_ci' }



class Database_handler():
    """
    Interface with connecting with the mysql server for the site. All interactions 
    with the database should be handled through method calls and Extensions on the 
    SQLAlchemy model objects. 
    """
    def __init__(self) -> None:
        """
        Initializes database\n
        If the database does not exist, it will be geneated for you\n
        It will generate/update all table models that are not implemented
        at start
        """

        self.db = db

        if not database_exists(database_config.SQLALCHEMY_DATABASE_URI):

            try:
                create_database(database_config.SQLALCHEMY_DATABASE_URI)
            except Exception as error:
                log_error(error)

        self.db.create_all()


    ###########################################################################
    # Bug Report Methods
    ###########################################################################
    def add_bug_report(self, message : str) -> int:
        try:
            new_bug_report = Bug_Report(
                create_time = datetime.now(),
                message=message
            )
            self.db.session.add(
                new_bug_report
            )
            self.db.session.commit()
            print(new_bug_report.as_dict())

            return new_bug_report.as_dict()['id']

        except Exception as error:
            log_error(error)
            return -1

    def delete_bug_report(self, id : int) -> bool:
        try:
            Bug_Report.query.filter_by(id = str(id)).delete()
            self.db.session.commit()
            return True

        except Exception as error:
            log_error(error)
            return False

    def get_all_bug_reports(self) -> list:
        try:
            join_requests = self.db.session.query(
                Bug_Report
            )

            return sorted([x.as_dict() for x in join_requests], key=lambda d: (d['create_time'] is not None, d['create_time']))


        except Exception as error:
            log_error(error)
            return []

    def get_most_recent_bug_report(self) -> dict:
        try:
            bug_report = self.db.session.query(
                Bug_Report
            )

            return bug_report.as_dict()


        except Exception as error:
            log_error(error)
            return []
            
    ###########################################################################
    # Join Team Requests Methods
    ###########################################################################
    def add_join_team_request(self, given_name : str, family_name : str, email : str) -> bool:
        try:
            self.db.session.add(
                Join_team_Request(
                    given_name = given_name,
                    family_name = family_name,
                    email = email,
                    create_time = datetime.now()
                )
            )

            self.db.session.commit()
            return True

        except Exception as error:
            log_error(error)
            return False

    def delete_join_team_request(self, id : int) -> bool:
        try:
            Join_team_Request.query.filter_by(id = str(id)).delete()
            self.db.session.commit()
            return True

        except Exception as error:
            log_error(error)
            return False

    def get_all_join_team_requests(self) -> list:
        try:
            join_requests = self.db.session.query(
                Join_team_Request
            )

            return sorted([x.as_dict() for x in join_requests], key=lambda d: (d['create_time'] is not None, d['create_time']))


        except Exception as error:
            log_error(error)
            return []

    ###########################################################################
    # Registration Methods
    ###########################################################################


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

    def is_registration(self, email : str) -> bool:
        try:
            print(email)
            registration = Registrations.query.filter_by(email = email).first()
            print(registration)
            
            if registration is None: return False
            else: return True

        except Exception as error:
            log_error(error)
            return None

    def get_registrations(self, username : str, code : str) -> dict:
        try:

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

        except Exception as error:
            log_error(error)
            return {}

    def get_registration_by_email(self, email : str) -> dict:
        try:
            registration = self.db.session.query(
                Registrations.id,
                Registrations.given_name,
                Registrations.family_name,
                Registrations.email,
                Registrations.username,
                Registrations.hashedpassword,
                Registrations.salt,
                Registrations.expiration
            ).filter_by(email = email)
            return [x._asdict() for x in registration][0]

        except Exception as error:
            log_error(error)
            return ""



    ###########################################################################
    # Announcement Methods
    ###########################################################################

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

    def delete_Announcement_list(self, announcement_list : list) -> bool:
        try:
            for id in announcement_list:
                Announcements.query.filter_by(id = id).delete()

            self.db.session.commit()
            return True
        except Exception as error:
            log_error(error)
            return False

    def get_all_Announcements(self) -> list:
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



    ###########################################################################
    # Users Methods
    ###########################################################################


    def add_User(self, given_name : str, family_name: str, email:str, username : str,  hashed_password : str, salt : str) -> bool:
        try:
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

        except Exception as error:
            log_error(error)
            return False

    def delete_User(self, id : int) -> bool:
        try:
            Users.query.filter_by(id=id).delete()
            self.db.session.commit()
            return True

        except Exception as error:
            log_error(error)
            return False
    
    def set_User_admin(self, id : int, value : bool) -> bool:
        try:
            self.db.session.query(Users).filter_by(
                id = id
            ).update(
                {"admin" : value}
            )

            self.db.session.commit()

            return False

        except Exception as error:
            log_error(error)
            return True

    def is_User(self, username : str, password: str) -> bool:
        try:
            user = Users.query.filter_by(username=username).first()
            
            if user is None: return False
            else: user = user.as_dict()

            return hashfun(password, user['salt']) == user['hashedpassword']

        except Exception as error:
            log_error(error)
            return None

    def get_User_by_Username(self, username : str) -> dict:
        try:
            user = Users.query.filter_by(username = username).first()
            
            if user is None: return False
            user = user.as_dict()

            user.pop('salt')
            user.pop('hashedpassword')

            return user
        except Exception as error:
            log_error(error)
            return {}

    def get_User_by_ID(self, id : int) -> dict:
        try:
            user = Users.query.filter_by(id=id).first()
            
            if user is None: return False
            user = user.as_dict()

            user.pop('salt')
            user.pop('hashedpassword')

            return user
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
                Users.admin
            )

            return sorted([x._asdict() for x in users], key=lambda d: (d['family_name'] is not None, d['family_name']))

        except Exception as error:
            log_error(error)
            return []

    def get_all_admins(self) -> list:
        try:
            users = self.db.session.query(
                Users.id,
                Users.given_name,
                Users.family_name,
                Users.email,
                Users.username,
                Users.admin
            ).filter_by(admin = True)
            return sorted([x._asdict() for x in users], key=lambda d: (d['family_name'] is not None, d['family_name']))

        except Exception as error:
            log_error(error)
            return []

