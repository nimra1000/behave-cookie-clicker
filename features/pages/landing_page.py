from selenium.webdriver.common.by import By

class LandingPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = "//input['name']"
        self.start_button = "//button[contains(text(), 'Start!')]"
        self.greeting_label = "//p[contains(text(), 'Hello')]"

    def login(self, name):
        self.enter_name(name)
        self.click_start_button()
