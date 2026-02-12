import pytest
from pages.login_page import LoginPage

BASE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="function")
def login_page(page):
    """
    Returns LoginPage object (not raw page)
    """
    login = LoginPage(page)
    login.go_to(BASE_URL)
    return login


@pytest.fixture(scope="function")
def authenticated_page(page):
    """
    Returns page after successful login
    """
    login = LoginPage(page)
    login.go_to(BASE_URL)
    login.login("standard_user", "secret_sauce")
    return page
