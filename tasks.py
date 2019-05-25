from selenium import webdriver
from pageobjects.twitter import home
import unittest
import requests


class Task1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.home_page = home.HomePage.open(self.driver)

    def tearDown(self) -> None:
        self.home_page = None
        self.driver.close()
        self.driver.quit()

    '''
    Task1
    Create automated test to validate Twitter login. The test script should:

    Visit twitter.com
    Click "login" button
    Fill out username / password
    Assert login failed
    
    Note: The assignment notes in item 2 that I should click "login" button, and in item 3 "Fill out username/password."
        I've reversed the order of these two items
    '''
    def test_task_1_cannot_log_into_twitter(self) -> None:
        uid = 'UserId'
        password = 'hunter2'
        self.home_page.set_uid(uid)
        self.home_page.set_password(password)
        login_result_page = self.home_page.click_login()

        login_successful = login_result_page.login_successful()
        self.assertFalse(login_successful, "Login as %s/%s was unexpectedly successful" % (uid, password))

        #login_error_page = login_result_page.get_login_error_page()    # An example of how to use LoginResultPage


class Task2(unittest.TestCase):
    def setUp(self) -> None:
        self.url_task2 = "https://data.ca.gov/api/action/datastore/search.json?resource_id=104076d0-4bbd-4d53-a6df-0f5cb8b0030c&limit=10&offset=0"
        self.result = requests.get(self.url_task2)

    '''
    Task 2
    Create automated test to validate API data:

    Visit https://data.ca.gov/api/action/datastore/search.json?resource_id=104076d0-4bbd-4d53-a6df-0f5cb8b0030c&limit=10&offset=0
    Assert result set size is exactly 10
    Assert the first county in the result set is "ALAMEDA"
    '''
    def test_task_2_validate_api_data(self) -> None:
        result_set = self.result.json()['result']['records']
        self.assertEqual(10, len(result_set))
        self.assertEqual("ALAMEDA", result_set[0]['county'])
