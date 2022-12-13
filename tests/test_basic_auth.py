from src.pages.page_basic_auth import BasicAuthPage


def test_basic_auth(browser):
    expected_header = "Basic Auth"
    expected_content = "Congratulations! You must have the proper credentials."

    page = BasicAuthPage(browser)
    page.open()
    header_text = page.get_header_text()
    content_text = page.get_content_text()

    assert header_text == expected_header, f'Header text "{header_text}" is not equal "{expected_header}"'
    assert content_text == expected_content, f'Content text "{content_text}" is not equal "{expected_content}"'
