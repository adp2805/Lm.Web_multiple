from browser import Browser
from pages.base_page import Base_page
from pages.home_page import Home_page
from pages.login_page import Login_page


# un marcator care defineste o metoda ce contine cod care trebuie sa il ruleze sistemul inainte de a rula primul test
from pages.succursales_page import Succursales_page


def before_all(context):
    #conext va fi o cutiuta care va stoca toate obiectele instantiate in scopul proiectului
    #context will be a box that will storrage all the .... objects in project purpose.
    context.browser = Browser()
    context.browser.maximize_window()
    context.login_page = Login_page()
    context.home_page = Home_page()
    context.succursales_page = Succursales_page()
    context.base_page = Base_page()


def after_all(context):
    context.browser.close_browser()