from pages.inventory_page import InventoryPage
from config.test_config import USERS


def login(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", USERS["standard"]["username"])
    page.fill("#password", USERS["standard"]["password"])
    page.click("#login-button")


def test_product_details_navigation(page):
    login(page)

    inventory = InventoryPage(page)

    # Capture first product info
    name_before = inventory.get_first_product_name()
    price_before = inventory.get_first_product_price()

    # Click first product
    inventory.click_first_product()

    # Validate details page info matches
    name_after = page.locator(".inventory_details_name").inner_text()
    price_after = float(
        page.locator(".inventory_details_price").inner_text().replace("$", "")
    )

    assert name_before == name_after
    assert price_before == price_after
