from selenium.webdriver.common.by import By

from browser import Browser
from pages.selectors.login_selectors import *


class Login_page(Browser):
    def go_to_login_page(self):
        self.driverObject.get("https://localhost/LM/Home/Login?ReturnUrl=%2fLM%2f")



    # def insert_username(self):
    #     self.driverObject.find_element(*USERNAME).send_keys("editec") # steluta de la username despacheteaza tuplul
    #
    # def insert_password(self):
    #     self.driverObject.find_element(*PASSWORD).send_keys("editec")

    # def inset_wrong_paswwrod(self):
    #     self.driverObject.find_element(*WRONG_PASSWORD_MSG).send_keys("wrong")

    # def click_login_button(self):
    #     self.driverObject.find_element(*LOGIN_BUTTON).click()

    # def click_logout_button(self):
    #     self.driverObject.find_element(*LOGOUT_BUTTON).click()
