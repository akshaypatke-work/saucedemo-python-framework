import pytest
from playwright.sync_api import Page


BASE_URL = "https://www.saucedemo.com"


@pytest.fixture(scope="session")
def storage_state(browser):
    context = browser.new_context()
    page = context.new_page()

    # Perform login once
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")

    # Save storage state
    storage = context.storage_state()
    context.close()
    return storage


@pytest.fixture
def authenticated_page(browser, storage_state):
    context = browser.new_context(storage_state=storage_state)
    page = context.new_page()
    page.goto(f"{BASE_URL}/inventory.html")

    yield page
    context.close()
