import pytest


@pytest.mark.regression
def test_sort_name_a_to_z(authenticated_page):
    authenticated_page.select_option(".product_sort_container", "az")
    assert True


@pytest.mark.regression
def test_sort_name_z_to_a(authenticated_page):
    authenticated_page.select_option(".product_sort_container", "za")
    assert True


@pytest.mark.regression
def test_sort_price_low_to_high(authenticated_page):
    authenticated_page.select_option(".product_sort_container", "lohi")
    assert True


@pytest.mark.regression
def test_sort_price_high_to_low(authenticated_page):
    authenticated_page.select_option(".product_sort_container", "hilo")
    assert True
