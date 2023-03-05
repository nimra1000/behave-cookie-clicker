from selenium.webdriver.common.by import By

class LandingPage:
    def __init__(self, driver):
        self.driver = driver

    def confirm_label_text_visible(self, text):
        label = self.driver.find_element(By.XPATH,("//p[contains(text(), '{}')]").format(text))
        assert label.is_displayed(), f"Cannot find text '{text}' on the page"

    def confirm_key_value_pair_visible(self, text):
        label = self.driver.find_element(By.XPATH,("//p//b[contains(text(), '{}')]").format(text))
        value = self.driver.find_element(By.ID, "{}".format(text.lower()))
        assert label.is_displayed(), f"Cannot find text '{text}' on the page"
        assert value.is_displayed(), f"There is no quantity amount for '{text}' on the page"