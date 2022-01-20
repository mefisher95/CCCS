AUTHORS = ['Michael Fisher']

ROUTES = {
        "home" : { "link" : "/", "name": "Home"},
        "about" : { "link" : "/", "name" : "About"},
        "document" : { "link" : "/site-documentation", "name" : "Documentation"}
    }

MENU_LINKS = [
    ROUTES['home'],
    ROUTES['about'],
    ROUTES['document']
]

SITE_TITLE = "CCCS - Development"
SITE_LOGO = "/images/logos/CCCS.png"
SITE_FAVICON = "/images/logos/favicon.ico"

def get_authors() -> list: return AUTHORS
def get_routes() -> dict : return ROUTES
def get_menu_links() -> list: return MENU_LINKS

def get_site_data() -> dict : 
    return { 
        'site_title' : SITE_TITLE,
        'site_logo' : SITE_LOGO,
        'fav_icon' : SITE_FAVICON
        }


