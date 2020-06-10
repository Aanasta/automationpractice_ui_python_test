import pytest
from selenium import webdriver

from pages.main_page import MainPage


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_search_result_is_displayed(browser):
    product_to_search = "Blouse"

    main_page = MainPage(browser)
    main_page.load()
    search_results_page = main_page.search_for_product(product_to_search)

    assert browser.current_url == search_results_page.SEARCH_RESULTS_PAGE_URL
    assert search_results_page.get_search_results_count() > 0
    assert search_results_page.get_search_result_title() == product_to_search
    assert search_results_page.is_search_result_image_displayed()
