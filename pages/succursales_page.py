from browser import Browser


class Succursales_page(Browser):
    def verify_succursales_page(self):
        actual_url = self.driverObject.get_current_url()
        expected_url = "https://localhost/LM/Branches"
        assert actual_url == expected_url, (f"{actual_url} difera fata de {expected_url}")
