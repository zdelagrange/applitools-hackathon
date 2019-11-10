class MainPage(object):

    PATH = "/hackathonApp.html"

    LOCATORS = {
        "content": "div.content-w",
        "amount_header": "th#amount",
        "recent_transaction_rows": "table#transactionsTable>tbody tr",
        "compare_expenses": "a#showExpensesChart",
        "flash_sale": 'div#flashSale>img[src$=".gif"]',
        "flash_sale_2": 'div#flashSale2>img[src$=".gif"]',
    }

    VALIDATION_ELEMENTS = ["content"]

    def __init__(self, driver):
        self.driver = driver

    def get_element_compare_expenses(self):
        return self.driver.find_element_by_css_selector(
            self.LOCATORS["compare_expenses"]
        )

    def get_element_flash_sale(self):
        return self.driver.find_element_by_css_selector(self.LOCATORS["flash_sale"])

    def get_element_flash_sale_2(self):
        return self.driver.find_element_by_css_selector(self.LOCATORS["flash_sale_2"])

    def get_element_amount_header(self):
        return self.driver.find_element_by_css_selector(self.LOCATORS["amount_header"])

    def get_elements_table_rows(self):
        return self.driver.find_elements_by_css_selector(
            self.LOCATORS["recent_transaction_rows"]
        )

    def get_row_data(self):
        rows = []
        for row in self.get_elements_table_rows():
            data = {}
            data["status"] = row.find_element_by_css_selector(
                "td:nth-of-type(1)>span:nth-of-type(" "2)"
            ).text
            data["date"] = row.find_element_by_css_selector(
                "td:nth-of-type(2)>span:nth-of-type(" "1)"
            ).text
            data["description"] = row.find_element_by_css_selector(
                "td:nth-of-type(3)>span"
            ).text
            data["category"] = row.find_element_by_css_selector(
                "td:nth-of-type(4)>a"
            ).text
            data["amount"] = row.find_element_by_css_selector("td:nth-of-type(5)").text
            rows.append(data)
        return rows

    def get_elements_amounts(self):
        # table_rows = self.get_elements_table_rows()
        # elements = []
        # for row in table_rows:
        #     elements += row.find_element_by_css_selector('td:nth-of-type(5)>span')
        # return elements
        self.driver.save_screenshot("./ss.png")
        return self.driver.find_elements_by_css_selector("td:nth-of-type(5)>span")

    def get_amounts_float(self):
        return [
            self.get_number_from_amount_row(ele.text)
            for ele in self.get_elements_amounts()
        ]

    def get_number_from_amount_row(self, text):
        new_text = text[: text.find("U") - 1].replace(",", "").replace(" ", "")
        return float(new_text)

    def Validate(self):
        validation_locators = {}
        for element in self.VALIDATION_ELEMENTS:
            validation_locators[element] = self.LOCATORS[element]
        success = True
        elements_not_found = []
        elements_not_visible = []
        for key in validation_locators:
            try:
                element = self.driver.find_element_by_css_selector(self.LOCATORS[key])
                element.is_displayed()
            except NoSuchElementException:
                success = False
                elements_not_found += key
            except ElementNotVisibleException:
                elements_not_visible += key
        return success, elements_not_found, elements_not_visible
