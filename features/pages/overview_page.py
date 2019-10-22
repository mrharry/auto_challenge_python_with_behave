from selenium.webdriver.common.by import By
from features.pages.base_page import BasePage


class OverviewPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)