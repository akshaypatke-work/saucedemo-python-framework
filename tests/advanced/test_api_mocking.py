import pytest


@pytest.mark.api
@pytest.mark.regression
def test_mock_inventory_empty(page, base_url):
    """
    Mock inventory page to simulate empty product list.
    Verify that no products are displayed.
    """

    # Intercept the inventory HTML request
    def handle_route(route):
        route.fulfill(
            status=200,
            content_type="text/html",
            body="""
            <html>
                <head><title>Inventory</title></head>
                <body>
                    <div class="inventory_list"></div>
                </body>
            </html>
            """
        )

    # Register route BEFORE navigation
    page.route("**/inventory.html", handle_route)

    # Go directly to inventory page
    page.goto(f"{base_url}/inventory.html")

    # Wait for load
    page.wait_for_load_state("load")

    # Verify no products rendered
    items = page.query_selector_all(".inventory_item")
    assert len(items) == 0, "Inventory should be empty when page is mocked"
