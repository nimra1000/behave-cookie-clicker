from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from features.pages.base_page import BasePage
from features.pages.landing_page import LandingPage
from features.pages.game_page import GamePage
import allure


def before_all(context):
    context.base_url = "https://seun-akinbode-2022-09-29.cookieclickertechtest.airelogic.com/"


def before_scenario(context, _):
    browser = context.config.userdata['browser']

    if browser == 'chrome':
         context.driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == 'firefox':
         context.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    else:
        raise Exception(f'Invalid browser "{browser}" specified in userdata')

    context.driver.get(context.base_url)

    context.base = BasePage(context.driver)
    context.landing = LandingPage(context.driver)
    context.game = GamePage(context.driver)


def after_step(context, step):
    if step.status == "failed":
        allure.attach(
            context.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG
        )


def after_scenario(context, _):
    context.driver.quit()