class GamePage:
    def __init__(self, driver):
        self.driver = driver
        self.title_btn = "input[name='username']"
        self.name_label = "button[name='login']"

        self.get_cookie_btn = "input[name='username']"
        self.sell_cookie_btn = "button[name='login']"
        self.buy_factory_btn = "input[name='username']"

        self.cookies_label = "button[name='login']"
        self.factory_label = "input[name='username']"
        self.factory_label = "button[name='login']"

    def enter_name(self, name):
        self.driver.find_element_by_css_selector(self.username_field).send_keys(name)

    def click_start_button(self):
        self.driver.find_element_by_css_selector(self.start_button).click()

    def login(self, name):
        self.enter_name(name)
        self.click_start_button()
