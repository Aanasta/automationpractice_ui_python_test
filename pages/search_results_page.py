from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    SEARCH_RESULTS_PAGE_URL = "http://automationpractice.com/index.php?controller=search&orderby=position&orderway" \
                              "=desc&search_query=Blouse&submit_search="

    PRODUCT_RESULTS_TILES = (By.XPATH, "//div[@class='product-container']")
    PRODUCT_RESULT_TITLE = (By.XPATH, "//div[@class='product-container']//h5/a")
    PRODUCT_RESULT_IMAGE = (By.XPATH, "//img[@alt='Blouse']")

    def get_search_results_count(self):
        return len(self.browser.find_elements(*self.PRODUCT_RESULTS_TILES))

    def get_search_result_title(self):
        return self.browser.find_element(*self.PRODUCT_RESULT_TITLE).text

    def is_search_result_image_displayed(self):
        return self.browser.find_element(*self.PRODUCT_RESULT_IMAGE).is_displayed()
