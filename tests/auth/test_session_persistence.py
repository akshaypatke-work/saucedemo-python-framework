import pytest
from helpers.test_data import BASE_URL
from helpers.utils import is_url_contains


@pytest.mark.regression
def test_session_persistence_after_refresh(authenticated_page):
    page = authenticated_page
    page.reload()
    assert is_url_contains(page, "inventory")


@pytest.mark.regression
def test_session_persistence_direct_url(authenticated_page):
    page = authenticated_page
    page.goto(f"{BASE_URL}/inventory.html")
    assert is_url_contains(page, "inventory")
