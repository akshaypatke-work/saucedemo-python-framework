import pytest


@pytest.mark.regression
def test_session_persistence_after_refresh(authenticated_page):
    page = authenticated_page
    page.reload()
    assert "inventory" in page.url


@pytest.mark.regression
def test_session_persistence_direct_url(authenticated_page):
    page = authenticated_page
    page.goto("/inventory.html")
    assert "inventory" in page.url
