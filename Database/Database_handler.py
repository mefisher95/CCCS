
from sqlalchemy_utils import database_exists, create_database
from datetime import datetime
from operator import itemgetter

from mysite import db, app, database_config
from mysite.utils.error_logger import log_error

from mysite.Database.Announcement import Announcement


USER_LENGTH = app.config['USER_LENGTH']
EMAIL_LENGTH = app.config['EMAIL_LENGTH']
HASHEDPASSWORD_LENGTH = app.config['HASHED_PASSWORD_LENGTH']
SALT_LENGTH = app.config['SALT_LENGTH']
RANDOM_LENGTH = app.config['RANDOM_LENGTH']

TABLE_ARGS = { 'extend_existing': True,
               'mysql_engine': 'InnoDB', 'mysql_charset': 'utf8',
               'mysql_collate': 'utf8_general_ci' }



class Database_handler():
    def __init__(self) -> None:

        self.db = db

        if not database_exists(database_config.SQLALCHEMY_DATABASE_URI):

            try:
                create_database(database_config.SQLALCHEMY_DATABASE_URI)
            except Exception as error:
                log_error(error)

        self.db.create_all()

    def set_Announcement(self, message : str, event_time : datetime = None) -> bool:
        try:
            if event_time is "" : event_time = None
            self.db.session.add(Announcement(
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
                Announcement.event_time, 
                Announcement.create_time,
                Announcement.id,
                Announcement.message
            )

            return sorted([x._asdict() for x in announcements], key=lambda d: (d['event_time'] is not None, d['event_time']))

        except Exception as error:
            log_error(error)
            return []

    def delete_Announcement_list(self, announcement_list : list) -> bool:
        try:
            for id in announcement_list:
                print('deleteing', id)
                Announcement.query.filter_by(id = id).delete()

            self.db.session.commit()
            return True
        except Exception as error:
            log_error(error)
            return False
