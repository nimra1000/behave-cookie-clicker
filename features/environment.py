import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from features.pages.base_page import BasePage
from features.pages.landing_page import LandingPage
from features.pages.game_page import GamePage


def before_all(context):
    context.base_url = "https://seun-akinbode-2022-09-29.cookieclickertechtest.airelogic.com/"


def before_scenario(context, _):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get(context.base_url)


    context.base = BasePage(context.driver)
    context.landing = LandingPage(context.driver)
    context.game = GamePage(context.driver)


def after_scenario(context, _):
    context.driver.quit()