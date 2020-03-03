import pytest
from selenium import webdriver
from resources.urls import Urls
from pages.main_page import MainPage
from resources.test_data import TestData


class TestSearch:

    @pytest.fixture(params=TestData.test_data.values(), ids=list(TestData.test_data.keys()))
    def get_test_data(self, request):
        return request.param

    @pytest.fixture()
    def get_driver(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(0.2)
        driver.maximize_window()
        yield driver
        driver.close()

    @pytest.fixture()
    def open_main_page(self, get_driver):
        get_driver.get(Urls.MAIN_PAGE)
        return MainPage(get_driver)

    def test_search_with_spa_and_wellness_centre_filters(self, get_test_data, open_main_page):
        main_page = open_main_page
        main_page.click_on_search_input_field()
        main_page.type_location_in_search_input_field(get_test_data["location"])
        main_page.click_on_check_in_calendar()
        main_page.select_check_in_date(get_test_data["dates"]["check_in_date"])
        main_page.select_check_out_date(get_test_data["dates"]["check_out_date"])
        search_results_page = main_page.click_on_search_button()
        search_results_page.click_hotels_checkbox()
        search_results_page.click_on_star_rating_checkbox(get_test_data["stars"])
        search_results_page.click_on_show_all_facilities_link()
        search_results_page.click_on_spa_and_wellness_centre(get_test_data["spa_and_wellness"])
        assert search_results_page.check_top_results(get_test_data["result"])
