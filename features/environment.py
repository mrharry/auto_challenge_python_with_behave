from selenium import webdriver
from features.pages.login_page import LoginPage
from features.pages.overview_page import OverviewPage
from features.pages.base_page import BasePage


def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.implicitly_wait(30)
    context.browser.set_page_load_timeout(30)
    context.browser.maximize_window()

    context.login_page = LoginPage(context.browser)
    context.overview_page = OverviewPage(context.browser)
    context.base_page = BasePage(context.browser)


def after_all(context):
    context.browser.close()