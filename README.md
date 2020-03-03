# README #

### What is this repository for? ###

* This repository is for a code challenge required for the QC Test Automation Engineer position recruitment process at Kneat.
* The challenge is to write a set of Selenium tests for the new 'Spa and wellness centre' and 'Star rating' filters options of Booking.com, including framework to support these tests.
* This is version 1.1.0.
* The test here was written in Python with Pytest and has 10 different sets of test data that cover many different scenarios using the mentioned features.
* The test data is in a dictionary format that can be later refactored to a JSON format.
* The test uses the Page Object Model design pattern for easy maintenance.
* The test framework developed uses Pytest fixtures to leverage the reuse of code. 
* Further improvements for future development include logging and negative tests.

### How do I get set up? ###

* You must have Python, Pytest and Selenium installed. 
* This test automation uses Chrome browser so you need to have the latest Selenium Chromedriver installed also.
* The test data (in ..resources\test_data.py) must be configured to use future check-in and check-out dates. Currently the tests will not pass if dates before the current date are used.
* To run the tests you can simply use your IDE runner or type pytest on the project root folder. 

### Who do I talk to? ###

* Marco Sanchotene