from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def type(self, locator, value):
        input_box = self.driver.find_element(By.XPATH, "//input['{}']".format(locator))
        input_box.send_keys(value)

    def click_button(self, locator):
        button = self.driver.find_element(By.XPATH,("//button[contains(text(), '{}')]").format(locator))
        button.click()

    def confirm_redirection(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"URL received '{current_url}' does not match expected URL of '{expected_url}' "

    def confirm_label_text_visible(self, text):
        label = self.driver.find_element(By.XPATH,("//p[contains(text(), '{}')]").format(text))
        assert label.is_displayed(), f"Cannot find text '{text}' on the page"

    def confirm_key_value_pair_visible(self, text):
        label = self.driver.find_element(By.XPATH,("//p//b[contains(text(), '{}')]").format(text))
        value = self.driver.find_element(By.ID, "{}".format(text.lower()))
        assert label.is_displayed(), f"Cannot find text '{text}' on the page"
        assert value.is_displayed(), f"There is no quantity amount for '{text}' on the page"

    def confirm_button_exists(self, locator):
        button = self.driver.find_element(By.XPATH,("//button[contains(text(), '{}')]").format(locator))
        assert button.is_displayed(), f"Cannot find button '{locator}' on the page"

    def confirm_input_fields_exists(self, locator):
        button = self.driver.find_element(By.XPATH, "//input['{}']".format(locator))
        assert button.is_displayed(), f"Cannot find input field '{locator}' on the page"
