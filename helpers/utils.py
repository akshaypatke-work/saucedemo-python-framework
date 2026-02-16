import random
import string


def is_url_contains(page, text: str) -> bool:
    """
    Check if given text exists in current page URL.
    """
    return text in page.url


def wait_for_element(page, locator: str, timeout: int = 5000):
    """
    Wait for element to be visible.
    """
    page.wait_for_selector(locator, timeout=timeout)


def generate_random_string(length: int = 6) -> str:
    """
    Generate random string for dynamic test data.
    """
    return ''.join(random.choices(string.ascii_letters, k=length))
