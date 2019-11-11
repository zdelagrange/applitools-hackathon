import os
from unittest import TestCase

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from page_objects.login import LoginPage


class BaseTestCase(TestCase):

    URL = os.environ.get("URL", "https://demo.applitools.com/hackathon.html")
    BROWSER_HEIGHT = 1080
    BROWSER_WIDTH = 1920

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        self.driver = Chrome(options=options)
        self.driver.set_window_size(self.BROWSER_WIDTH, self.BROWSER_HEIGHT)
        self.driver.get(self.URL)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()
