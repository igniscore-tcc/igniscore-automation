from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.email_input = page.get_by_role("textbox", name="Email")

        self.password_input = page.get_by_role("textbox", name="Senha")

        self.login_button = page.get_by_role("button", name="Entrar")

    def login(self, email, password):
        self.email_input.fill(email)

        self.password_input.fill(password)

        self.login_button.click()

        self.page.wait_for_url("**/dashboard")