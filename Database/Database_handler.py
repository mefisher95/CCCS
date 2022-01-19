from mysite import db, app, config
from sqlalchemy_utils import database_exists, create_database

from mysite.utils.error_logger import log_error

from mysite.Database.Menu_data import Menu_data
from mysite.Database.Site_data import Site_data


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

        if not database_exists(config.SQLALCHEMY_DATABASE_URI):

            try:
                create_database(config.SQLALCHEMY_DATABASE_URI)
            except Exception as error:
                log_error(error)

            self.db.create_all()
            self.set_menu_data("/", "Home")
            self.set_menu_data("/", "About")
            self.set_menu_data("/site-documentation", "Documentation")

            self.set_site_data("CCCS - Development", "/images/logos/CCCS.png", "/images/logos/favicon.ico")


    ##### Menu data ##########
    def get_menu_data(self) -> list[dict]:
        try:
            menu_data = self.db.session.query(Menu_data.link, Menu_data.name)
            return [dict(obj) for obj in menu_data]

        except Exception as error:
            log_error(error)
            return [{}]

    def set_menu_data(self, link : str, name : str) -> bool:
        try:
            self.db.session.add(Menu_data(
                link = link, 
                name = name
            ))

            self.db.session.commit()
            return True

        except Exception as error:
            log_error(error)
            return False
        
    
    ##### Site Data ##########
    def get_site_data(self) -> dict:
        try:
            site_data  = self.db.session.query(Site_data.site_title, Site_data.site_logo, Site_data.fav_icon)
            return [dict(obj) for obj in site_data][0]

        except Exception as error:
            log_error(error)
            return {}

    def set_site_data(self, site_title : str, site_logo : str, fav_icon : str) -> bool:
        try:
            self.db.session.add(Site_data(
                site_title = site_title,
                site_logo = site_logo,
                fav_icon = fav_icon
            ))

            self.db.session.commit()
            return True

        except Exception as error:
            log_error(error)
            return False

            
            