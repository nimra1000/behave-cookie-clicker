import time
from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class GamePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    
    def set_cookie_quantity(self, desired_quantity):
        element = self.driver.find_element(By.ID, "cookies")
        current_quantity = int(element.text)

        if current_quantity != desired_quantity:
            difference = current_quantity - desired_quantity
            if difference < 0:
                for i in range(abs(difference)):
                    self.click_button("click")
            elif difference > 0:
                self.type("cookies-to-sell", difference)
                self.click_button("sell-cookies!")

    def check_quantity(self, expected_quantity, locator):
        element = self.driver.find_element(By.ID, locator)
        current_quantity = int(element.text)
        assert current_quantity == expected_quantity, f"quantity received '{current_quantity}' does not match expected quantity of '{expected_quantity}' "
       