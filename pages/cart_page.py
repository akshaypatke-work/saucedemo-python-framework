from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = ".cart_item"
        self.remove_button = "button.btn_secondary"
        self.checkout_button = "#checkout"

    def get_cart_items_count(self):
        return len(self.page.query_selector_all(self.cart_items))

    def remove_item(self):
        self.page.click(self.remove_button)

    def proceed_to_checkout(self):
        self.page.click(self.checkout_button)
