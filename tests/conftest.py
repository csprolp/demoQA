import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def config_browser():
    browser.config.base_url = "https://demoqa.com"
    browser.config.window_width = 1200
    browser.config.window_height = 900
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = "eager"
    browser.config.driver_options = driver_options

    yield
    browser.quit()
