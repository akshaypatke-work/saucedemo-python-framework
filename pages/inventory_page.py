from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_icon = ".shopping_cart_link"
        self.inventory_items = ".inventory_item"
        self.sort_dropdown = ".product_sort_container"
        self.item_names = ".inventory_item_name"
        self.item_prices = ".inventory_item_price"

    def get_title(self):
        return self.page.text_content(".title")

    def add_first_item_to_cart(self):
        self.page.click("button.btn_inventory")

    def go_to_cart(self):
        self.page.click(self.cart_icon)

    def get_cart_badge_count(self):
        return self.page.text_content(".shopping_cart_badge")

    def sort_by(self, value):
        self.page.select_option(self.sort_dropdown, value)

    def get_all_item_names(self):
        elements = self.page.query_selector_all(self.item_names)
        return [e.inner_text() for e in elements]

    def get_all_item_prices(self):
        elements = self.page.query_selector_all(self.item_prices)
        return [float(e.inner_text().replace("$", "")) for e in elements]

    def click_first_product(self):
        self.page.click(self.item_names)

    def get_first_product_name(self):
        return self.page.locator(self.item_names).first.inner_text()

    def get_first_product_price(self):
        return float(
            self.page.locator(self.item_prices).first.inner_text().replace("$", "")
        )
