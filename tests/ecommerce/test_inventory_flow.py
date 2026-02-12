import pytest


@pytest.mark.smoke
@pytest.mark.regression
def test_inventory_and_cart_flow(authenticated_page):
    authenticated_page.click(".inventory_item button")
    authenticated_page.click(".shopping_cart_link")
    assert "cart" in authenticated_page.url


@pytest.mark.regression
def test_remove_item_from_cart(authenticated_page):
    authenticated_page.click(".inventory_item button")
    authenticated_page.click(".shopping_cart_link")
    authenticated_page.click(".cart_button")
    assert "cart" in authenticated_page.url


@pytest.mark.regression
def test_complete_checkout_flow(authenticated_page):
    authenticated_page.click(".inventory_item button")
    authenticated_page.click(".shopping_cart_link")
    authenticated_page.click("#checkout")
    authenticated_page.fill("#first-name", "Akshay")
    authenticated_page.fill("#last-name", "Patke")
    authenticated_page.fill("#postal-code", "411001")
    authenticated_page.click("#continue")
    authenticated_page.click("#finish")
    assert "complete" in authenticated_page.url
