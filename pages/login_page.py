class LoginPage:

    def __init__(self, page):
        self.page = page
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def go_to(self, base_url):
        self.page.goto(base_url)

    def login(self, username, password):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.inner_text(self.error_message)

    def is_inventory_page_loaded(self):
        return self.page.locator(".inventory_list").is_visible()
