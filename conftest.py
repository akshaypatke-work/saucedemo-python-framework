import os
import pytest

from config.env_config import BASE_URL
from pages.login_page import LoginPage


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page", None)

        if page:
            screenshots_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_path = os.path.join(
                screenshots_dir,
                f"{item.name}.png"
            )

            page.screenshot(path=screenshot_path)


# --- RESTORE TEST FIXTURES ---
@pytest.fixture(scope="function")
def login_page(page):
    """
    Returns LoginPage object (NOT raw Playwright page)
    """
    login = LoginPage(page)
    login.go_to(BASE_URL)
    return login


@pytest.fixture(scope="function")
def authenticated_page(page):
    """
    Returns logged-in Playwright page
    """
    page.goto(BASE_URL)
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")
    return page
