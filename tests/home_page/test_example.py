import pytest
from playwright.sync_api import expect
from pages.home_page import HomePage


@pytest.mark.user_type("TestUser1")
def test_example(login, page):
    home_page = HomePage(page)
    expect(home_page.header_label).to_contain_text("Swag Labs")


def test_user_lands_on_product_page():
    pass


def test_list_of_products_visible():
    pass


def test_filter_sort_name_z_to_a():
    pass


def test_filter_sort_price_low_to_high():
    pass


def test_verify_adding_item_to_cart():
    pass


def test_verify_adding_items_to_cart():
    pass
