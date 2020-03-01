from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


class SearchResultsPage:
    three_stars_checkbox_xpath = '//a[@data-id="class-3"]'
    four_stars_checkbox_xpath = '//a[@data-id="class-4"]'
    five_stars_checkbox_xpath = '//a[@data-id="class-5"]'
    no_stars_checkbox_xpath = '//a[@data-id="class-0"]'
    search_message_xpath = '//div[@class="sr-usp-overlay sr-usp-overlay--wide"]'
    show_all_thirteen_link_xpath = '(//button[@class="collapsed_partly_link collapsed_partly_more"])[1]'
    spa_and_wellness_centre_xpath = '//a[@data-id="hotelfacility-54"]'

    def __init__(self, driver):
        self.driver = driver

    def click_on_star_rating_checkbox(self, stars):
        try:
            if stars["three"]:
                three_stars_checkbox_element = self.driver.find_element_by_xpath(self.three_stars_checkbox_xpath)
                three_stars_checkbox_element.click()
                search_message_element = WebDriverWait(self.driver, 10).until(
                    expected_conditions.presence_of_element_located((By.XPATH, self.search_message_xpath)))
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.staleness_of(search_message_element))
            if stars["four"]:
                four_stars_checkbox_element = self.driver.find_element_by_xpath(self.four_stars_checkbox_xpath)
                four_stars_checkbox_element.click()
                search_message_element = WebDriverWait(self.driver, 10).until(
                    expected_conditions.presence_of_element_located((By.XPATH, self.search_message_xpath)))
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.staleness_of(search_message_element))
            if stars["five"]:
                five_stars_checkbox_element = self.driver.find_element_by_xpath(self.five_stars_checkbox_xpath)
                five_stars_checkbox_element.click()
                search_message_element = WebDriverWait(self.driver, 10).until(
                    expected_conditions.presence_of_element_located((By.XPATH, self.search_message_xpath)))
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.staleness_of(search_message_element))
            if stars["no"]:
                no_stars_checkbox_element = self.driver.find_element_by_xpath(self.no_stars_checkbox_xpath)
                no_stars_checkbox_element.click()
                search_message_element = WebDriverWait(self.driver, 10).until(
                    expected_conditions.presence_of_element_located((By.XPATH, self.search_message_xpath)))
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.staleness_of(search_message_element))
        except NoSuchElementException:
            print("Could not find element with the locator provided.")
        except ElementNotVisibleException:
            print("Element with the locator provided is not visible.")
        except ElementClickInterceptedException:
            print("Element with locator provided could not be clicked.")

    def click_on_show_all_thirteen_link(self):
        try:
            show_all_thirteen_link_element = self.driver.find_element_by_xpath(self.show_all_thirteen_link_xpath)
            show_all_thirteen_link_element.click()
        except NoSuchElementException:
            print("Could not find element with the locator provided.")
        except ElementNotVisibleException:
            print("Element with the locator provided is not visible.")
        except ElementClickInterceptedException:
            print("Element with locator provided could not be clicked.")

    def click_on_spa_and_wellness_centre(self, test_data):
        try:
            if test_data:
                spa_and_wellness_centre_element = self.driver.find_element_by_xpath(self.spa_and_wellness_centre_xpath)
                spa_and_wellness_centre_element.click()
                search_message_element = WebDriverWait(self.driver, 10).until(
                    expected_conditions.presence_of_element_located((By.XPATH, self.search_message_xpath)))
                WebDriverWait(self.driver, 10).until(
                    expected_conditions.staleness_of(search_message_element))
        except NoSuchElementException:
            print("Could not find element with the locator provided.")
        except ElementNotVisibleException:
            print("Element with the locator provided is not visible.")
        except ElementClickInterceptedException:
            print("Element with locator provided could not be clicked.")
