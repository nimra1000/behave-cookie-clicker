from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class BasePage:
    def click(self, el):
        self.driver.find_element_by_css_selector(self.el).click()