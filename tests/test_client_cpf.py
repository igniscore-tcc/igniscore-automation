from faker import Faker

from config.settings import (
    BASE_URL,
    TEST_EMAIL,
    TEST_PASSWORD,
)

from pages.login_page import LoginPage
from pages.client_page import ClientPage

fake = Faker("pt_BR")


def test_create_cnpj_client_success(page):
    login_page = LoginPage(page)
    client_page = ClientPage(page)

    page.goto(f"{BASE_URL}/login")

    login_page.login(
        TEST_EMAIL,
        TEST_PASSWORD,
    )

    page.goto(f"{BASE_URL}/clientes")

    company_name = fake.company()
    cnpj = fake.cnpj()
    email = fake.company_email()
    phone = fake.cellphone_number()

    client_page.create_cnpj(
        name=company_name,
        cnpj=cnpj,
        ie="123456789",
        uf="SP",
        email=email,
        phone=phone,
        obs="Cliente PJ criado automaticamente pelo Playwright",
    )

    page.get_by_text(company_name).wait_for()

    assert page.get_by_text(company_name).is_visible()