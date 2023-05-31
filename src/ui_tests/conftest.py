import pytest
from faker import Faker
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Firefox(executable_path="./chromedriver")
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def fake_data() -> Faker:
    return Faker("en_US")
