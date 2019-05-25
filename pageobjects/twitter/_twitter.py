from urllib.parse import urljoin
from selenium import webdriver


class TwitterPage:
    base_url = "https://www.twitter.com/"

    def __init__(self, driver: webdriver):
        self.driver = driver

    def go(self, path: str):
        url_to_load = urljoin(TwitterPage.base_url, path)
        self.driver.get(url_to_load)
