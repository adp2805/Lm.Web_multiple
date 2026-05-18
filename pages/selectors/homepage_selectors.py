from selenium.webdriver.common.by import By

LOGOUT_BUTTON = (By.CSS_SELECTOR,"a#logout_link")
SUCCURSALES = (By.CSS_SELECTOR,"li.branches>a")
HOMEBUTTON = (By.CSS_SELECTOR, "div.home")
TERMINALBUTTON = (By.XPATH,'//div[@class="rtc_manager"]//a[@href="/LM/Terminals"]')
REGIONAL_CENTER = (By.CSS_SELECTOR,"li.regional_centers>a")
RETAILER = (By.CSS_SELECTOR,'li.retailers>a')
AGENT_BUTTON = (By.CSS_SELECTOR,'li.agents>a')
