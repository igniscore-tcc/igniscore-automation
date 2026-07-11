import random
import re
from datetime import datetime
from calendar import monthrange
from faker import Faker

from config.settings import BASE_URL, TEST_EMAIL, TEST_PASSWORD
from pages.login_page import LoginPage
from pages.product_page import ProductPage

fake = Faker("pt_BR")

PRODUCT_TYPES = ["EXTINGUISHER", "SERVICE", "CONSUMABLE", "ACCESSORY", "HOSE", "DETECTOR", "SPRINKLER", "CENTRAL",
                 "LIGHTING", "DOOR", "HYDRANT"]

def test_create_product_success(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    page.goto(f"{BASE_URL}/login")
    login_page.login(TEST_EMAIL, TEST_PASSWORD)

    page.goto(f"{BASE_URL}/produtos")

    pagination_text = page.locator("footer").get_by_text(re.compile(r"\d+-\d+ de \d+")).text_content()
    total_antes = int(pagination_text.split(" de ")[1].strip())

    random_product_type = random.choice(PRODUCT_TYPES)
    product_name = f"Produto {fake.word().capitalize()} {random.randint(100, 999)}"
    lot = f"LOT-{random.randint(1000, 9999)}"
    price = f"{random.uniform(10.0, 500.0):.2f}"

    today = datetime.now()
    _, last_day_of_month = monthrange(today.year, today.month)

    if today.day == last_day_of_month:
        random_validity_day = today.day
    else:
        random_validity_day = random.randint(today.day + 1, last_day_of_month)

    product_page.create_product(
        name=product_name,
        product_type=random_product_type,
        validity_day=random_validity_day,
        lot=lot,
        price=price,
    )

    page.wait_for_timeout(1000)

    pagination_text_depois = page.locator("footer").get_by_text(re.compile(r"\d+-\d+ de \d+")).text_content()
    total_depois = int(pagination_text_depois.split(" de ")[1].strip())

    assert total_depois == total_antes + 1