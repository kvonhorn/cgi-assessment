from ._twitter import TwitterPage
from .login_error import LoginErrorPage
#from .feed_page import FeedPage


class LoginResultPage(TwitterPage):
    def __init__(self):
        self.login_error_page = None
        #self.feed_page = None   # TODO: Implement this once I test a happy path

    def set_login_error_page(self, login_error_page):
        self.login_error_page = login_error_page

    def get_login_error_page(self):
        return self.login_error_page

    def login_successful(self):
        return not isinstance(self.login_error_page, LoginErrorPage)
