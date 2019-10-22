from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class BasePage(object):

    def __init__(self, browser, base_url='https://login.sandbox.freeagent.com/'):
        self.base_url = base_url
        self.browser = browser
        self.timeout = 30

    def navigate(self, url):
        url = self.base_url + url
        return self.browser.get(url)

    def find_element(self, *locator):
        return self.browser.find_element(*locator)

    def text_of(self, *locator):
        return self.find_element(*locator).text

    def get_page_title(self):
        return self.browser.title

    def fill_in(self, input_text, *locator):
        self.find_element(*locator).clear()
        return self.find_element(*locator).send_keys(input_text)

    def submit(self, *locator):
        return self.find_element(*locator).click()

