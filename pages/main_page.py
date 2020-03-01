from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from pages.search_results_page import SearchResultsPage


class MainPage(object):

    search_input_field_id = "ss"
    check_in_and_out_calendars_class = "xp__dates-inner"
    check_in_or_check_out_date_generic_xpath = '//td[@data-date="{0}"]'
    next_calendar_arrow_xpath = '//div[@data-bui-ref="calendar-next"]'
    search_button_xpath = '//button[@data-sb-id="main"]'

    def __init__(self, driver):
        self.driver = driver
        self.search_input_field_element = self.driver.find_element_by_id(self.search_input_field_id)
        self.check_in_and_out_calendars_element = self.driver.find_element_by_class_name(
            self.check_in_and_out_calendars_class)

    def click_on_search_input_field(self):
        try:
            self.search_input_field_element.click()
        except NoSuchElementException:
            print("Could not find element with the locator provided.")
        except ElementNotVisibleException:
            print("Element with the locator provided is not visible.")
        except ElementClickInterceptedException:
            print("Element with locator provided could not be clicked.")

    def type_location_in_search_input_field(self, location):
        try:
            self.search_input_field_element.send_keys(location)
        except NoSuchElementException:
            print("Could not find element with the locator provided.")
        except ElementNotVisibleException:
            print("Element with the locator provided is not visible.")

    def click_on_check_in_calendar(self):
        try:
            self.check_in_and_out_calendars_element.click()
        except NoSuchElementException:
            print("Could not find element with the locator provided.")
        except ElementNotVisibleException:
            print("Element with the locator provided is not visible.")
        except ElementClickInterceptedException:
            print("Element with locator provided could not be clicked.")

    def select_check_in_date(self, date):
        try:
            date_test = []
            while not date_test:
                date_test = self.driver.find_elements_by_xpath(
                    self.check_in_or_check_out_date_generic_xpath.format(date))
                if date_test:
                    check_in_date_element = self.driver.find_element_by_xpath(
                        self.check_in_or_check_out_date_generic_xpath.format(date))
                    check_in_date_element.click()
                else:
                    next_calendar_arrow_element = self.driver.find_element_by_xpath(self.next_calendar_arrow_xpath)
                    next_calendar_arrow_element.click()
        except NoSuchElementException:
            print("Could not find element with the locator provided.")
        except ElementNotVisibleException:
            print("Element with the locator provided is not visible.")
        except ElementClickInterceptedException:
            print("Element with locator provided could not be clicked.")

    def select_check_out_date(self, date):
        try:
            date_test = []
            while not date_test:
                date_test = self.driver.find_elements_by_xpath(
                    self.check_in_or_check_out_date_generic_xpath.format(date))
                if date_test:
                    check_out_date_element = self.driver.find_element_by_xpath(
                        self.check_in_or_check_out_date_generic_xpath.format(date))
                    check_out_date_element.click()
                else:
                    next_calendar_arrow_element = self.driver.find_element_by_xpath(self.next_calendar_arrow_xpath)
                    next_calendar_arrow_element.click()
        except NoSuchElementException:
            print("Could not find element with the locator provided.")
        except ElementNotVisibleException:
            print("Element with the locator provided is not visible.")
        except ElementClickInterceptedException:
            print("Element with locator provided could not be clicked.")

    def click_on_search_button(self):
        try:
            search_button_element = self.driver.find_element_by_xpath(self.search_button_xpath)
            search_button_element.click()
            return SearchResultsPage(self.driver)
        except NoSuchElementException:
            print("Could not find element with the locator provided.")
        except ElementNotVisibleException:
            print("Element with the locator provided is not visible.")
        except ElementClickInterceptedException:
            print("Element with locator provided could not be clicked.")

