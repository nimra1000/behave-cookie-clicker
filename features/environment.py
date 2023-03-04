from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def before_scenario(context, _):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())
    context.driver.get("https://seun-akinbode-2022-09-29.cookieclickertechtest.airelogic.com/")


def after_scenario(context, _):
    context.driver.quit()