from sqlalchemy_utils import database_exists, create_database
from datetime import datetime

from mysite import db, app, database_config
from mysite.Database.Bug_Report import Bug_Report
from mysite.Database.Course_Homework import Course_Homework
from mysite.utils.error_logger import log_error
from mysite.utils.security_utils import hashfun, randstring

from mysite.Database.Announcements import Announcements
from mysite.Database.Users import Users
from mysite.Database.Registration import Registrations
from mysite.Database.Join_team_Request import Join_team_Request
from mysite.Database.Bug_Report import Bug_Report

from mysite.Database.Department import Department
from mysite.Database.Courses import Courses

from mysite.Database.Course_Assignments import Course_Assignments
from mysite.Database.Course_Notes import Course_Notes
from mysite.Database.Course_Homework import Course_Homework
from mysite.Database.Course_Quizzes import Course_Quizzes
from mysite.Database.Course_Projects import Course_Projects



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
    #   Course Project Methods
    ###########################################################################
    def add_Course_Project(self, course_id : int, project_name : str, pdf_link : str, due_date : datetime) -> int:
        try:
            new_homework = Course_Projects(
                Course_id = course_id,
                project_name = project_name,
                pdf_link = pdf_link,
                due_date = due_date
            )

            self.db.session.add(new_homework)
            self.db.session.commit()

            return new_homework.as_dict()['id']

        except Exception as error:
            log_error(error)
            return -1

    def get_all_Course_Projects(self):
        try:
            projects = self.db.session.query(
                Course_Projects
            )
            projects = sorted([x.as_dict() for x in projects], key=lambda d: (d['Course_id'] is not None, d['Course_id']))
            for i in projects:
                i['Course'] = self.get_Course_by_id(
                    i['Course_id']
                )

            return projects

        except Exception as error:
            log_error(error)
            return -1

    def get_all_Course_Projects_in_Course(self, course_id : int) -> list:
        try:
            projects = Course_Projects.query.filter_by(Course_id = course_id)
            projects = sorted([x.as_dict() for x in projects], key=lambda d: (d['Course_id'] is not None, d['Course_id']))
            for i in projects:
                i['Course'] = self.get_Course_by_id(
                    i['Course_id']
                )

            return projects

        except Exception as error:
            log_error(error)
            return []

    def get_Course_Project_by_ID(self, project_id : int) -> dict:
        try:
            project = Course_Projects.query.filter_by(
                id = project_id
            ).first()


            return project.as_dict()
        except Exception as error:
            log_error(error)
            return {}

    def remove_Course_Project_from_Course(self, project_id : int) -> bool:
        try:
            Course_Projects.query.filter_by(
                id = project_id
            ).delete()

            self.db.session.commit()

            return True
        except Exception as error:
            log_error(error)
            return False

    ###########################################################################
    #   Course Quiz Methods
    ###########################################################################
    def add_Course_Quiz(self, course_id : int, quiz_name : str, pdf_link : str, due_date : datetime) -> int:
        try:
            new_homework = Course_Quizzes(
                Course_id = course_id,
                quiz_name = quiz_name,
                pdf_link = pdf_link,
                due_date = due_date
            )

            self.db.session.add(new_homework)
            self.db.session.commit()

            return new_homework.as_dict()['id']

        except Exception as error:
            log_error(error)
            return -1

    def get_all_Course_Quizzes(self):
        try:
            quizzes = self.db.session.query(
                Course_Quizzes
            )
            quizzes = sorted([x.as_dict() for x in quizzes], key=lambda d: (d['Course_id'] is not None, d['Course_id']))
            for i in quizzes:
                i['Course'] = self.get_Course_by_id(
                    i['Course_id']
                )

            return quizzes

        except Exception as error:
            log_error(error)
            return -1

    def get_all_Course_Quizzes_in_Course(self, course_id : int) -> list:
        try:
            quizzes = Course_Quizzes.query.filter_by(Course_id = course_id)
            quizzes = sorted([x.as_dict() for x in quizzes], key=lambda d: (d['Course_id'] is not None, d['Course_id']))
            for i in quizzes:
                i['Course'] = self.get_Course_by_id(
                    i['Course_id']
                )

            return quizzes

        except Exception as error:
            log_error(error)
            return []

    def get_Course_Quiz_by_ID(self, quiz_id : int) -> dict:
        try:
            quiz = Course_Quizzes.query.filter_by(
                id = quiz_id
            ).first()


            return quiz.as_dict()
        except Exception as error:
            log_error(error)
            return {}

    def remove_Course_Quiz_from_Course(self, quiz_id : int) -> bool:
        try:
            Course_Quizzes.query.filter_by(
                id = quiz_id
            ).delete()

            self.db.session.commit()

            return True
        except Exception as error:
            log_error(error)
            return False

    ###########################################################################
    #   Course Homework Methods
    ###########################################################################
    def add_Course_Homework(self, course_id : int, homework_name : str, pdf_link : str, due_date : datetime) -> int:
        try:
            new_homework = Course_Homework(
                Course_id = course_id,
                homework_name = homework_name,
                pdf_link = pdf_link,
                due_date = due_date
            )

            self.db.session.add(new_homework)
            self.db.session.commit()

            return new_homework.as_dict()['id']

        except Exception as error:
            log_error(error)
            return -1

    def get_all_Course_Homework(self):
        try:
            homework_assignments = self.db.session.query(
                Course_Homework
            )
            homework_assignments = sorted([x.as_dict() for x in homework_assignments], key=lambda d: (d['Course_id'] is not None, d['Course_id']))
            for i in homework_assignments:
                i['Course'] = self.get_Course_by_id(
                    i['Course_id']
                )

            return homework_assignments

        except Exception as error:
            log_error(error)
            return -1

    def get_all_Course_Homework_in_Course(self, course_id : int) -> list:
        try:
            homework_assignments = Course_Homework.query.filter_by(Course_id = course_id)
            homework_assignments = sorted([x.as_dict() for x in homework_assignments], key=lambda d: (d['Course_id'] is not None, d['Course_id']))
            for i in homework_assignments:
                i['Course'] = self.get_Course_by_id(
                    i['Course_id']
                )

            return homework_assignments

        except Exception as error:
            log_error(error)
            return []

    def get_Course_Homework_by_ID(self, homework_id : int) -> dict:
        try:
            homework = Course_Homework.query.filter_by(
                id = homework_id
            ).first()


            return homework.as_dict()
        except Exception as error:
            log_error(error)
            return {}

    def remove_Course_Homework_from_Course(self, homework_id : int) -> bool:
        try:
            Course_Homework.query.filter_by(
                id = homework_id
            ).delete()

            self.db.session.commit()

            return True
        except Exception as error:
            log_error(error)
            return False
    ###########################################################################
    # Course Notes Methods
    ###########################################################################
    def add_Course_Notes(self, course_id : int, notes_name : str, pdf_link : str) -> int:
        try:
            new_course_note = Course_Notes(
                Course_id = course_id,
                notes_name = notes_name,
                pdf_link = pdf_link
            )

            self.db.session.add(new_course_note)
            self.db.session.commit()
            return new_course_note.as_dict()['id']

        except Exception as error:
            log_error(error)
            return -1

    def get_all_Course_Notes(self):
        try:
            courses = self.db.session.query(
                Course_Notes
            )
            courses = sorted([x.as_dict() for x in courses], key=lambda d: (d['Course_id'] is not None, d['Course_id']))
            for i in courses:
                i['Course'] = self.get_Course_by_id(
                    i['Course_id']
                )

            return courses

        except Exception as error:
            log_error(error)
            return -1

    def get_all_Course_Notes_in_Course(self, course_id : int) -> list:
        try:
            notes = Course_Notes.query.filter_by(Course_id = course_id)
            notes = sorted([x.as_dict() for x in notes], key=lambda d: (d['Course_id'] is not None, d['Course_id']))
            for i in notes:
                i['Course'] = self.get_Course_by_id(
                    i['Course_id']
                )

            return notes

        except Exception as error:
            log_error(error)
            return []

    def get_Course_Notes_by_ID(self, notes_id : int) -> dict:
        try:
            note = Course_Notes.query.filter_by(
                id = notes_id
            ).first()


            return note.as_dict()
        except Exception as error:
            log_error(error)
            return {}

    def remove_Course_Notes_from_Course(self, notes_id : int) -> bool:
        print('notes_id', notes_id)
        try:
            Course_Notes.query.filter_by(
                id = notes_id
            ).delete()

            self.db.session.commit()

            return True
        except Exception as error:
            log_error(error)
            return False
    ###########################################################################
    # Course Assignment Methods
    ###########################################################################
    def add_Course_Assignment(
        self,
        user_id : int,
        course_id : int
        ) -> int:

        try:
            new_course_assignment = Course_Assignments(
                User_id = user_id,
                Course_id = course_id
            )

            self.db.session.add(new_course_assignment)
            self.db.session.commit()

            return new_course_assignment.as_dict()['id']

        except Exception as error:
            log_error(error)
            return -1
    
    def get_all_Users_in_Course(
        self,
        course_id : int
        ) -> list:

        try:
            assignments = Course_Assignments.query.filter_by(Course_id = course_id)
            return [x.as_dict() for x in assignments]

        except Exception as error:
            log_error(error)
            return []


    def remove_User_from_Course_Assignment(
        self, 
        user_id : int,
        course_id : int
        ) -> bool:
        try:
            Course_Assignments.query.filter_by(
                User_id = user_id,
                Course_id = course_id
            ).delete()
            
            self.db.session.commit()
            return True

        except Exception as error:
            log_error(error)
            return False

    ###########################################################################
    # Courses Methods
    ###########################################################################
    def add_Course(
        self, 
        department_id : int,
        # professor_id : int,
        course_num : int, course_name : str,
        credit_hour : int, 
        course_link : str = None
        ) -> int:
        try:
            new_course = Courses(
                department_id = department_id,
                course_num = course_num,
                course_name = course_name,
                credit_hour = credit_hour,
                link = course_link
            )

            self.db.session.add(new_course)
            self.db.session.commit()
            return new_course.as_dict()['id']

        except Exception as error:
            log_error(error)
            return -1

    def get_Course_by_course_code(
        self,
        dept_id : int,
        course_num : int
        ) -> dict:

        try:
            course = Courses.query.filter_by(
                department_id = dept_id,
                course_num = course_num
                ).first()

            course = course.as_dict()

            course['department'] = self.get_Department_by_id(
                course['department_id']
            ) 
            return course

        except Exception as error:
            log_error(error)
            return {}

    def get_Course_by_id(self, id : int) -> dict:
        try:
            course = Courses.query.filter_by(id = id).first()
            
            if course is None: return False
            course = course.as_dict()

            course['department'] = self.get_Department_by_id(
                course['department_id']
            ) 
            return course

        except Exception as error:
            log_error(error)
            return {}

    def get_all_Courses(self) -> list:
        try:
            courses = self.db.session.query(
                Courses
            )
            courses = sorted([x.as_dict() for x in courses], key=lambda d: (d['course_num'] is not None, d['course_num']))
            for i in courses:
                i['department'] = self.get_Department_by_id(
                    i['department_id']
                )

            return courses


        except Exception as error:
            log_error(error)
            return []

    def delete_Course(self, id : int) -> bool:
        try:
            users = self.get_all_Users_in_Course(id)
            notes = self.get_all_Course_Notes_in_Course(id)
            homework = self.get_all_Course_Homework_in_Course(id)
            quizzes = self.get_all_Course_Quizzes_in_Course(id)
            project = self.get_all_Course_Projects_in_Course(id)

            for user in users: self.remove_User_from_Course_Assignment(user['id'], id)
            for note in notes: self.remove_Course_Notes_from_Course(note['id'])
            for work in homework: self.remove_Course_Homework_from_Course(work['id'])
            for quiz in quizzes: self.remove_Course_Quiz_from_Course(quiz['id'])
            for proj in project: self.remove_Course_Project_from_Course(proj['id'])

            Courses.query.filter_by(id = id).delete()
            self.db.session.commit()
            return True

        except Exception as error:
            log_error(error)
            return False

    ###########################################################################
    # Department Methods
    ###########################################################################
    def add_Department(self, name : str, code : str) -> int:
        try:
            new_department = Department(
                name = name,
                code = code
            )
            self.db.session.add(new_department)
            self.db.session.commit()
            return new_department.as_dict()['id']
        except Exception as error:
            log_error(error)
            return -1

    def get_Department_by_code(self, code : str) -> dict:
        try:
            return Department.query.filter_by(code = code).first().as_dict()

        except Exception as error:
            log_error(error)
            return {}

    def get_Department_by_id(self, id : int) -> dict:
        try:
            department = Department.query.filter_by(id = id).first()
            
            if department is None: return False
            return department.as_dict()

        except Exception as error:
            log_error(error)
            return {}

    def get_all_Departments(self) -> list:
        try:
            departments = self.db.session.query(
                Department
            )
            print(departments)

            return sorted([x.as_dict() for x in departments], key=lambda d: (d['code'] is not None, d['code']))


        except Exception as error:
            log_error(error)
            return []

    def delete_Department(self, id : int) -> bool:
        try:
            Department.query.filter_by(id = id).delete()
            self.db.session.commit()
            return True
        except Exception as error:
            log_error(error)
            return False


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
