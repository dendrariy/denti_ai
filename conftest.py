import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--headless", action="store", default="True", help="headless mode")


@pytest.fixture(scope="function")
def browser(request):
    headless = request.config.getoption("headless")
    browser = None
    if headless == "True":
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        print("\nstart chrome browser for test in headless mode..")
        browser = webdriver.Chrome(options=options)
    elif headless == "False":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    else:
        raise pytest.UsageError("--headless should be True or False")
    yield browser
    print("\nquit browser..")
    browser.quit()
