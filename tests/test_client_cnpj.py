from faker import Faker

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

    page.get_by_text(name).wait_for()

    assert page.get_by_text(name).is_visible()