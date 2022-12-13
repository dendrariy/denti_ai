from typing import List

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from src.pages.base_page import BasePage
from src.urls import HOVERS_PAGE_URL


class HoverPage(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.url = HOVERS_PAGE_URL
        self.hover = (By.CLASS_NAME, "figure")
        self.header = (By.XPATH, '//h3[.="Hovers"]')
        self.hover_name = (By.XPATH, '//div[@class="figcaption"]/h5')
        self.hover_link = (By.XPATH, '//div[@class="figcaption"]/a')

    def get_hovers(self) -> List[WebElement]:
        return self.browser.find_elements(*self.hover)

    def get_hovers_names(self) -> list:
        return self.browser.find_elements(*self.hover_name)

    def get_hovers_links(self) -> list:
        return self.browser.find_elements(*self.hover_link)

    def move_to_hover(self, hover: WebElement):
        action = ActionChains(self.browser)
        action.move_to_element(hover).perform()
