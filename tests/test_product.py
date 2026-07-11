import pytest
import random
from datetime import datetime
from calendar import monthrange
from faker import Faker

from config.settings import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from pages.login_page import LoginPage
from pages.product_page import ProductPage

fake = Faker("pt_BR")

PRODUCT_TYPES = ["EXTINGUISHER", "SERVICE", "CONSUMABLE", "ACCESSORY", "HOSE", "DETECTOR", "SPRINKLER", "CENTRAL",
                 "LIGHTING", "DOOR", "HYDRANT"]


def test_create_product_success(page):  # Removido o 'async'
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    page.goto(f"{BASE_URL}/login")
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    page.goto(f"{BASE_URL}/produtos")

    random_product_type = random.choice(PRODUCT_TYPES)
    product_name = f"Produto {fake.word().capitalize()} {random.randint(100, 999)}"
    lot = f"LOT-{random.randint(1000, 9999)}"
    price = f"{random.uniform(10.0, 500.0):.2f}"

    today = datetime.now()
    _, last_day_of_month = monthrange(today.year, today.month)
    random_validity_day = random.randint(today.day, last_day_of_month)

    product_page.create_product(
        name=product_name,
        product_type=random_product_type,
        validity_day=random_validity_day,
        lot=lot,
        price=price,
    )

    toast = page.get_by_role("alert")
    toast.wait_for(state="visible")

    assert toast.is_visible()
    assert "sucesso" in toast.text_content().lower() or "cadastrado" in toast.text_content().lower()