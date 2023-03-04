class LandingPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_field = "input[name='username']"
        self.start_button = "button[name='login']"

    def enter_name(self, name):
        self.driver.find_element_by_css_selector(self.username_field).send_keys(name)

    def click_start_button(self):
        self.driver.find_element_by_css_selector(self.start_button).click()

    def login(self, name):
        self.enter_name(name)
        self.click_start_button()
