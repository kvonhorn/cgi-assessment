from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from ._twitter import TwitterPage
from .login_error import LoginErrorPage
from .login_result import LoginResultPage


class HomePage(TwitterPage):
    path_expected = "/"

    uid_textbox_class_name = 'email-input'
    password_textbox_selector = 'input[name="session[password]"]'
    login_button_class_name = 'submit'

    def __init__(self, driver: webdriver):
        super().__init__(driver)

    @staticmethod
    def open(driver: webdriver):
        """
        Open the Twitter home page with the given webdriver and returns a HomePage object
        :param driver: A webdriver instance
        :return: A HomePage object
        """
        home_page = HomePage(driver)
        home_page.go(HomePage.path_expected)
        return home_page

    def set_uid(self, uid: str):
        uid_textbox = self.driver.find_element_by_class_name(HomePage.uid_textbox_class_name)
        uid_textbox.clear()
        uid_textbox.send_keys(uid)
        return self

    def set_password(self, password: str):
        password_textbox = self.driver.find_element_by_css_selector(HomePage.password_textbox_selector)
        password_textbox.clear()
        password_textbox.send_keys(password)
        return self

    def click_login(self):
        login_button = self.driver.find_element_by_class_name(HomePage.login_button_class_name)
        login_button.click()
        login_result_page = LoginResultPage()

        # Wait for next page to load
        WebDriverWait(self.driver, 15).until(
            lambda x: x.current_url.find(LoginErrorPage.path_expected) > -1 or x.find_element_by_id('global-new-tweet-button'),
            "Could not determine if login was successful or not"
        )

        # Determine if login was successful or not
        if self.driver.current_url.find(LoginErrorPage.path_expected) > -1:
            login_error_page = LoginErrorPage(self.driver)
            login_result_page.set_login_error_page(login_error_page)
            #login_result_page.login_error_page = login_error_page
        else:
            #print("Setting new FeedPage instance")
            # TODO: Pass in a new FeedPage instance
            pass

        return login_result_page

