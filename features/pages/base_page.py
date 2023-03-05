import time
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def type(self, locator, value):
        if locator == 'name':
            input_field = self.driver.find_element(By.XPATH, "//input['{}']".format(locator))
        else:    
            input_field = self.driver.find_element(By.ID, "{}".format(locator))

        input_field.clear()
        input_field.send_keys(value)

    def click_button(self, locator):
        if locator == 'Start!':
            button = self.driver.find_element(By.XPATH,("//button[contains(text(), '{}')]").format(locator))
        else:    
            button = self.driver.find_element(By.ID, "{}".format(locator))

        button.click()
        time.sleep(1)

    def confirm_redirection(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"URL received '{current_url}' does not match expected URL of '{expected_url}' "

    def confirm_button_exists(self, locator):
        if locator == 'Start!':
            button = self.driver.find_element(By.XPATH,("//button[contains(text(), '{}')]").format(locator)) #####
        else:    
            button = self.driver.find_element(By.ID, "{}".format(locator))        
        
        assert button.is_displayed(), f"Cannot find button '{locator}' on the page"

    def confirm_input_fields_exists(self, locator):
        if locator == 'name':
            input_field = self.driver.find_element(By.XPATH, "//input['{}']".format(locator))
        else:    
            input_field = self.driver.find_element(By.ID, "{}".format(locator))

        assert input_field.is_displayed(), f"Cannot find input field '{locator}' on the page"
