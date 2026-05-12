from browser import Browser
from pages.selectors.homepage_selectors import SUCCURSALES


class Home_page(Browser):
    def verify_login_successful(self):
        expected_url = "https://localhost/LM/"
        actual_url = self.driverObject.get_current_url()
        assert actual_url == expected_url, f"{expected_url} is different from {actual_url}"

    # def click_succursale_button(self):
    #     self.driverObject.find_element(*SUCCURSALES).click()
