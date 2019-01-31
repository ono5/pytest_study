from pytest import fixture

from selenium import webdriver


@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser

    # Teardown
    print("I am tearing down this browser")

