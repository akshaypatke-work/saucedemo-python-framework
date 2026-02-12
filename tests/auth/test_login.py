import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_successful_login(login_page):
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in login_page.page.url


@pytest.mark.regression
def test_locked_user_login(login_page):
    login_page.login("locked_out_user", "secret_sauce")
    assert "Epic sadface" in login_page.get_error_message()


@pytest.mark.regression
def test_invalid_login(login_page):
    login_page.login("invalid_user", "wrong_password")
    assert "Epic sadface" in login_page.get_error_message()
