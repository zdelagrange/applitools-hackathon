import os
import unittest
from test_case import BaseTestCase

from applitools.selenium import Eyes, Target
from page_objects.main import MainPage


class TestLoginPageUIElements(BaseTestCase):
    def setUp(self):
        self.eyes = Eyes()
        self.eyes.api_key = os.environ.get("APPLITOOLS_API_KEY")
        super().setUp()
        self.eyes.open(
            self.driver,
            "Hackathon",
            self._testMethodName,
            {"width": self.BROWSER_WIDTH, "height": self.BROWSER_HEIGHT},
        )

    def tearDown(self):
        self.eyes.close()
        super().tearDown()

    def test_login_page_ui_elements(self):
        success, elements_not_found, elements_not_visible = self.login_page.Validate()
        self.eyes.check(
            self._testMethodName + " validate login page elements", Target.window()
        )
        self.assertTrue(
            success,
            f"elements not found: {elements_not_found}\nelements not "
            f"visible: {elements_not_visible}",
        )

    def test_data_driven_a(self):
        """Test to ensure error is visible when you do not enter a username or password"""
        self.eyes.check(
            self._testMethodName + " before clicking login", Target.window()
        )
        self.login_page.login("", "")

        element = self.login_page.get_element_log_in_error()
        self.eyes.check(self._testMethodName + " after clicking login", Target.window())
        self.assertTrue(element, "The error does not exist on the page")
        self.assertTrue(element.is_displayed, "The error is not visible on the page")

    def test_data_driven_b(self):
        self.eyes.check(
            self._testMethodName + " before clicking login", Target.window()
        )
        self.login_page.login("username", "")

        element = self.login_page.get_element_log_in_error()
        self.eyes.check(self._testMethodName + " after clicking login", Target.window())
        self.assertTrue(element, "The error does not exist on the page")
        self.assertTrue(element.is_displayed, "The error is not visible on the page")

    def test_data_driver_c(self):
        self.eyes.check(
            self._testMethodName + " before clicking login", Target.window()
        )
        self.login_page.login("", "password")
        element = self.login_page.get_element_log_in_error()
        self.eyes.check(self._testMethodName + " after clicking login", Target.window())
        self.assertTrue(element, "The error does not exist on the page")
        self.assertTrue(element.is_displayed, "The error does not exist on the page")

    def test_data_driven_d(self):
        self.eyes.check(
            self._testMethodName + " before clicking login", Target.window()
        )
        self.login_page.login("username", "password")
        main_page = MainPage(self.login_page.driver)
        self.eyes.check(self._testMethodName + " after clicking login", Target.window())
        success, elements_not_found, elements_not_visible = main_page.Validate()
        self.assertTrue(
            success,
            f"elements not found: {elements_not_found}\nelements not "
            f"visible: {elements_not_visible}",
        )

    def test_table_sort(self):
        self.login_page.login("username", "password")
        main_page = MainPage(self.login_page.driver)
        amounts_before_sort = main_page.get_amounts_float()
        data_before_sort = main_page.get_row_data()
        # let's test to make sure it isn't already sorted!
        self.assertNotEqual(amounts_before_sort, sorted(amounts_before_sort))
        self.eyes.check(self._testMethodName + " before sort", Target.window())

        main_page.get_element_amount_header().click()
        amounts_after_sort = main_page.get_amounts_float()
        data_after_sort = main_page.get_row_data()
        self.eyes.check(self._testMethodName + " after sort", Target.window())

        self.assertNotEqual(amounts_before_sort, amounts_after_sort)
        self.assertEqual(amounts_after_sort, sorted(amounts_after_sort))
        [self.assertTrue(row in data_after_sort) for row in data_before_sort]

    def test_canvas_chart(self):
        self.login_page.login("username", "password")
        main_page = MainPage(self.login_page.driver)
        main_page.get_element_compare_expenses().click()
        self.eyes.check(
            self._testMethodName + " before adding next year ", Target.window()
        )
        main_page.get_element_show_data_for_next_year().click()
        self.eyes.check(
            self._testMethodName + " after adding next year ", Target.window()
        )

    def test_dynamic_content(self):
        self.driver.get(self.URL + "?showAd=true")
        self.login_page.login("username", "password")
        main_page = MainPage(self.driver)
        self.eyes.check(self._testMethodName, Target.window())
        self.assertTrue(main_page.get_element_flash_sale().is_displayed())
        self.assertTrue(main_page.get_element_flash_sale_2().is_displayed())


if __name__ == "__main__":
    unittest.main()
