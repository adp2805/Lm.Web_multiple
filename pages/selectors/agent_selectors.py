from selenium.webdriver.common.by import By
SEARCHBYID = (By.CSS_SELECTOR,'input#rbAgentsSearchCriteria[value="2"]')
INSERT_AGENT_ID = (By.CSS_SELECTOR,'input#tbAgentId')
SEARCH_BUTTON = (By.CSS_SELECTOR,'#btSearch')
SELECT_AGENT = (By.XPATH,'//td[@class="first_name clickable_cell"]')
MODIFY_AGENT = (By.XPATH,'//div[@class="content_section section_buttons"]//a[1]')