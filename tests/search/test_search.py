import pytest
from selenium import webdriver
from resources.urls import Urls
from pages.main_page import MainPage


class TestSearch:

    stars = {
        "three": True,
        "four": False,
        "five": True,
        "no": False
    }

    @pytest.fixture(scope="class")
    def open_main_page(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(Urls.MAIN_PAGE)
        return MainPage(driver)

    def test_search_with_spa_and_wellness_centre_filter(self, open_main_page):
        main_page = open_main_page
        main_page.click_on_search_input_field()
        main_page.type_location_in_search_input_field("Limerick")
        main_page.click_on_check_in_calendar()
        main_page.select_check_in_date("2020-07-10")
        main_page.select_check_out_date("2020-07-15")
        search_results_page = main_page.click_on_search_button()
        search_results_page.click_on_star_rating_checkbox(self.stars)
        search_results_page.click_on_show_all_thirteen_link()
        search_results_page.click_on_spa_and_wellness_centre(True)
