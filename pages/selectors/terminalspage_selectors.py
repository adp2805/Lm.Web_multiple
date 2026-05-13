from selenium.webdriver.common.by import By


SEARCHBYID = (By.CSS_SELECTOR,'input#rbTerminalsSearchCriteria[value="2"]')
TERMINALID = (By.CSS_SELECTOR, '#searchById>input+input')
SEARCHTBUTTON = (By.CSS_SELECTOR,'input#btSearch[type="button"]')
SELECT_TERMINAL = (By.XPATH,'//td[@class="terminal_number clickable_cell"]')
MODIFY_BUTTON = (By.XPATH,'//div[@class="content technicians"]//a')
SELECT_GROUP = (By.XPATH,'//option[contains(text(),"Lm.")]')
ALLOW_GROUP = (By.CSS_SELECTOR,'a#btnAlocateGroup')
SAVE_TERMINAL = (By.XPATH,'//input[@type="submit"]')
SAVE_ERR = (By.CSS_SELECTOR,'div.validation-summary-errors')

