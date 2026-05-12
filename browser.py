
from seleniumbase import Driver

class Browser:
    driverObject = Driver()

    def maximize_window(self):
        self.driverObject.maximize_window()


    def close_browser(self):
        self.driverObject.quit()








