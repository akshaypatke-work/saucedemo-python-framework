import pytest
from helpers.test_data import FIRST_NAME, LAST_NAME, POSTAL_CODE
from helpers.utils import is_url_contains


@pytest.mark.smoke
@pytest.mark.regression
def test_inventory_and_cart_flow(authenticated_page):
    page = authenticated_page

    page.click(".inventory_item button")
    page.click(".shopping_cart_link")

    assert is_url_contains(page, "cart")


@pytest.mark.regression
def test_remove_item_from_cart(authenticated_page):
    page = authenticated_page

    page.click(".inventory_item button")
    page.click(".shopping_cart_link")
    page.click(".cart_button")

    assert is_url_contains(page, "cart")


@pytest.mark.regression
def test_complete_checkout_flow(authenticated_page):
    page = authenticated_page

    page.click(".inventory_item button")
    page.click(".shopping_cart_link")
    page.click("#checkout")

    page.fill("#first-name", FIRST_NAME)
    page.fill("#last-name", LAST_NAME)
    page.fill("#postal-code", POSTAL_CODE)

    page.click("#continue")
    page.click("#finish")

    assert is_url_contains(page, "complete")
