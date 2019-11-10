import os
from unittest import TestCase

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

from page_objects.login import LoginPage
from page_objects.main import MainPage

class TestLoginPageUIElements(TestCase):
    password = 'ApplitoolsP4ssword'

    URL = os.environ.get('URL', 'https://demo.applitools.com/hackathon.html')

    def setUp(self):
        chrome_options = ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = Chrome(chrome_options=chrome_options)
        self.driver.get(self.URL)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_page_ui_elements(self):
        success, elements_not_found, elements_not_visible = self.login_page.Validate()
        self.assertTrue(success, f'elements not found: {elements_not_found}\nelements not '
        f'visible: {elements_not_visible}')

    def test_data_driven_a(self):
        """Test to ensure error is visible when you do not enter a username or password"""
        self.login_page.login('', '')
        element = self.login_page.get_element_log_in_error()
        self.assertTrue(element, 'The error does not exist on the page')
        self.assertTrue(element.is_displayed, 'The error is not visible on the page')

    def test_data_driven_b(self):
        self.login_page.login('username', '')
        element = self.login_page.get_element_log_in_error()
        self.assertTrue(element, 'The error does not exist on the page')
        self.assertTrue(element.is_displayed, 'The error is not visible on the page')

    def test_data_driver_c(self):
        self.login_page.login('', 'password')
        element = self.login_page.get_element_log_in_error()
        self.assertTrue(element.is_displayed, 'The error does not exist on the page')

    def test_data_driven_d(self):
        self.login_page.login('username', 'password')
        main_page = MainPage(self.login_page.driver)
        success, elements_not_found, elements_not_visible = main_page.Validate()
        self.assertTrue(success, f'elements not found: {elements_not_found}\nelements not '
        f'visible: {elements_not_visible}')

    def test_table_sort(self):
        self.login_page.login('username', 'password')
        main_page = MainPage(self.login_page.driver)
        amounts_before_sort = main_page.get_amounts_float()
        data_before_sort = main_page.get_row_data()
        # let's test to make sure it isn't already sorted!
        self.assertNotEqual(amounts_before_sort, sorted(amounts_before_sort))

        main_page.get_element_amount_header().click()
        amounts_after_sort = main_page.get_amounts_float()
        data_after_sort = main_page.get_row_data()

        self.assertNotEqual(amounts_before_sort, amounts_after_sort)
        self.assertEqual(amounts_after_sort, sorted(amounts_after_sort))
        [self.assertTrue(row in data_after_sort) for row in data_before_sort]

    # this test can't be automated using selenium/webdriver, since it renders and draws on a
    # canvas element, which doesn't manipulate the DOM, so there are no elements to find.
    # def test_canvas_chart(self):
    #     self.login_page.login('username', 'password')
    #     main_page = MainPage(self.login_page.driver)
    #     main_page.get_element_compare_expenses().click()

    def test_dynamic_content(self):
        self.driver.get(self.URL + '?showAd=true')
        self.login_page.login('username', 'password')
        main_page = MainPage(self.driver)
        self.assertTrue(main_page.get_element_flash_sale().is_displayed())
        self.assertTrue(main_page.get_element_flash_sale_2().is_displayed())


if __name__ == '__main__':
    import unittest
    unittest.main()
