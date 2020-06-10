from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.search_results_page import SearchResultsPage


class MainPage(BasePage):
    MAIN_PAGE_URL = "http://automationpractice.com/index.php"

    SEARCH_INPUT = (By.ID, "search_query_top")

    def load(self):
        self.browser.get(self.MAIN_PAGE_URL)

    def search_for_product(self, product):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(product + Keys.ENTER)
        return SearchResultsPage(self.browser)
