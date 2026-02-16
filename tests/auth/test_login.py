import pytest
from helpers.test_data import (
    STANDARD_USER,
    LOCKED_USER,
    INVALID_USER,
    VALID_PASSWORD,
    INVALID_PASSWORD,
)
from helpers.utils import is_url_contains


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login(login_page):
    login_page.login(STANDARD_USER, VALID_PASSWORD)
    assert is_url_contains(login_page.page, "inventory")


@pytest.mark.regression
def test_locked_user_login(login_page):
    login_page.login(LOCKED_USER, VALID_PASSWORD)
    assert "Epic sadface" in login_page.get_error_message()


@pytest.mark.regression
def test_invalid_login(login_page):
    login_page.login(INVALID_USER, INVALID_PASSWORD)
    assert "Epic sadface" in login_page.get_error_message()
