from selenium.webdriver.common.by import By

from src.constants import LOGIN, PASSWORD
from src.pages.base_page import BasePage
from src.urls import BASIC_AUTH_PAGE_URL


class BasicAuthPage(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.url = f"http://{LOGIN}:{PASSWORD}@{BASIC_AUTH_PAGE_URL}"
        self.header = (By.XPATH, '//div[@class="example"]/h3')
        self.content = (By.XPATH, '//div[@class="example"]/p')

    def get_header_text(self) -> str:
        return self.browser.find_element(*self.header).text

    def get_content_text(self) -> str:
        return self.browser.find_element(*self.content).text
