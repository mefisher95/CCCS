from fileinput import filename
from flask import url_for
from datetime import datetime


def log_error(error : Exception, file : str = "error_log.txt") -> None:
    with open('mysite/static/logs/' + file , 'a') as exception_file:
        # print(url_for('static', filename = "logs/"+ file))
        exception_file.write('TIMESTAMP >>> ' + str(datetime.now()) + '\n' +  str(error) + '\n\n')