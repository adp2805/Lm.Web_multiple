from selenium.webdriver.common.by import By

USERNAME = (By.CSS_SELECTOR,'#UserName')
PASSWORD = (By.ID, "Password")
LOGIN_BUTTON = (By.XPATH, '//input[@type= "submit"]')
WRONG_PASSWORD_MSG = (By.CSS_SELECTOR,"div.validation-summary-errors>ul>li")


