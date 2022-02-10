from mysite.Database.Registration import Registrations


AUTHORS = ['Michael Fisher', 'Grant Clark']

class Route: 
    def __init__(self, link : str, name : str) -> None :
        self.link = link
        self.name = name

    def __str__(self) -> str:
        return "< Route- Name: {0}, Link: {1} >".format(self.name, self.link)     

    def __repr__(self) -> str:
        return "< Route {0} >".format(self.name)   

ROUTES = { 
        "index" : Route("/", "Index"),
        "home" : Route("/home", "Home"),
        "document" : Route("/site-documentation", "Documentation"),
        "manage_site_data" : Route("/manage_site", "Manage Site"),
        "new_student_info" : Route("/new_student_info", "New Student Information"),
        "register" : Route("/SellUsYourSoul", "Register"),
        "finalize_register" : Route("/SoulSold", "Finalize Registration"),
        "login" : Route("/login", "Login"), 
        "logout" : Route("/logout", "Logout"),
        "resend_registration" : Route('/resend_registration', "Resend Registration"),
        "join_team" : Route('/join_team', "Join the Team"),
        "report_bug" : Route('/report_bug', "Report Bug"),
        "student_resources" : Route('/student_resources', "Student Resources"),
        "course_not_found" : Route('/course_not_found', "Course Not Found")
    }

MENU_LINKS = [
    ROUTES['home'],
    ROUTES['new_student_info'],
    ROUTES['student_resources']
]

SITE_TITLE = "CCCS - Development"
SITE_LOGO = "/images/logos/CCCS.png"
SITE_FAVICON = "/images/logos/favicon.ico"

SITE_DATA = { 
    'site_title' : SITE_TITLE,
    'site_logo' : SITE_LOGO,
    'fav_icon' : SITE_FAVICON
    }

def get_authors() -> list: return AUTHORS
def get_routes() -> dict : return ROUTES
def get_menu_links() -> list: return MENU_LINKS

def get_site_data() -> dict : 
    return { 
        'site_title' : SITE_TITLE,
        'site_logo' : SITE_LOGO,
        'fav_icon' : SITE_FAVICON
        }


