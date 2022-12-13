from src.pages.page_upload_file import FileUploadPage


def test_file_upload(browser):
    filename = "test.txt"

    page = FileUploadPage(browser)
    page.open()
    page.file_upload(filename)
    page.check_uploaded_file(filename)
