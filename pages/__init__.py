from mysite.pages import *

from mysite.pages import index, site_info
from mysite.pages.user_management import register, login, logout
from mysite.pages.admin import manage_site_data, manage_student_resources
from mysite.pages.main_pages import new_student_info, home
from mysite.pages.dev_pages import join_team, report_bug

from mysite.pages.courses import view_notes, view_assignment, view_quizzes, view_projects

from mysite.pages.student_resources import student_resources, view_tutorial

from mysite.pages.page_not_found import course_not_found

from mysite.pages.courses import course_template
from mysite.pages import test_bed