import datetime, string


#### SQLALCHEMY CONSTANTS ####
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="root",
    password="root",
    hostname="localhost", # OK
    databasename="cccs")
SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
SQLALCHEMY_POOL_RECYCLE = 280 # changed to 50? better than 299?
SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_TRACK_MODIFICATIONS = True


#### DB CONSTANTS ####
USER_LENGTH = 64
USER_MIN_LENGTH = 2
EMAIL_LENGTH = 128
PASSWORD_MIN_LENGTH = 8
PASSWORD_MAX_LENGTH = 64
HASHED_PASSWORD_LENGTH = 128
SESSION_KEY_LENGTH = 64
SALT_LENGTH = 50
RANDOM_LENGTH = 16
HASH_ROUNDS = 100
DTIME_FOR_REGISTRATION = datetime.timedelta(minutes=15)
USER_CHARS = "%s%s." % (string.ascii_letters, string.digits)
EMAIL_SUBSTRINGS=[]

SQLALCHEMY_POOL_RECYCLE = 280 # changed to 50? better than 299?
SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_TRACK_MODIFICATIONS = True
