from faker import Faker
import re
from config.settings import (
    BASE_URL,
    TEST_EMAIL,
    TEST_PASSWORD,
)

from pages.login_page import LoginPage
from pages.client_page import ClientPage

fake = Faker("pt_BR")


def test_create_cpf_client_success(page):
    login_page = LoginPage(page)
    client_page = ClientPage(page)

    page.goto(f"{BASE_URL}/login")

    login_page.login(
        TEST_EMAIL,
        TEST_PASSWORD,
    )

    page.goto(f"{BASE_URL}/clientes")

    pagination_text = page.locator("footer").get_by_text(re.compile(r"\d+-\d+ de \d+")).text_content()

    total_antes = int(pagination_text.split(" de ")[1].strip())

    name = fake.name()
    cpf = fake.cpf()
    email = fake.email()
    phone = fake.cellphone_number()

    client_page.create_cpf(
        name=name,
        cpf=cpf,
        email=email,
        phone=phone,
        obs="Cliente PF criado automaticamente pelo Playwright",
    )

    page.wait_for_timeout(1000)

    pagination_text_depois = page.locator("footer").get_by_text(re.compile(r"\d+-\d+ de \d+")).text_content()
    total_depois = int(pagination_text_depois.split(" de ")[1].strip())

    assert total_depois == total_antes + 1