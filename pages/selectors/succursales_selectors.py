from selenium.webdriver.common.by import By

TRDSUCCURSALE = (By.XPATH,"//tr[@data-id=2]")
MODIFYSUC = (By.XPATH,'//a[@href="/LM/Branches/Edit/2"]')
MODIFY_SUC_NAME = (By.CSS_SELECTOR,"input#Description")
SAVEBUTTON = (By.XPATH,'//input[@class="submit_positive"]')
DELETEINPUT = (By.CSS_SELECTOR,"input#Description")

