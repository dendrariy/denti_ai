from selenium.webdriver.common.by import By

from src.constants import TESTDATA
from src.urls import FILE_UPLOAD_PAGE_URL

from .base_page import BasePage


class FileUploadPage(BasePage):
    def __init__(self, browser):
        self.browser = browser
        self.url = FILE_UPLOAD_PAGE_URL
        self.header = (By.XPATH, '//h3[.="File Uploader"]')
        self.header_file_uploaded = (By.XPATH, '//h3[.="File Uploaded!"]')
        self.button_file_upload = (By.CSS_SELECTOR, "#file-upload")
        self.button_file_submit = (By.CSS_SELECTOR, "#file-submit")
        self.uploaded_files = (By.CSS_SELECTOR, "#uploaded-files")

    def file_upload(self, filename: str):
        self.browser.find_element(*self.button_file_upload).send_keys(TESTDATA + filename)
        self.browser.find_element(*self.button_file_submit).click()

    def check_uploaded_file(self, filename: str):
        assert self.browser.find_element(*self.header_file_uploaded).is_displayed(), "Element is not visible"
        assert self.browser.find_element(*self.uploaded_files).text == filename, "Filename is not matched"
