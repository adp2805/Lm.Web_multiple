from selenium.webdriver.common.by import By
SELECT_CENTER = (By.XPATH,'//tr[@data-id="3"]//td[2]')
MODIFY_CENTER = (By.XPATH,'//div[@class="content_section section_buttons"]//a[1]')
PHONE_NUMBER = (By.CSS_SELECTOR,'#Address_Mobile')
SAVE_CENTER = (By.XPATH,'//input[@type="submit"]')
SUCCURSALE_DROPDOWN = (By.CSS_SELECTOR,"#ddlBranches")
SELECTED_SUCCURSALE = (By.XPATH,'//option[contains(text(),"automatizare")]')