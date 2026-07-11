from config.settings import (
    BASE_URL,
    TEST_EMAIL,
    TEST_PASSWORD
)

from pages.login_page import LoginPage


def test_login_success(page):

    login_page = LoginPage(page)

    page.goto(
        f"{BASE_URL}/login"
    )

    login_page.login(
        TEST_EMAIL,
        TEST_PASSWORD
    )

    assert "/dashboard" in page.url