from ._twitter import TwitterPage


class LoginErrorPage(TwitterPage):
    path_expected = "/login/error"

    def __init__(self, driver):
        super().__init__(driver)
