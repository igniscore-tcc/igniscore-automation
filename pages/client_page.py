from playwright.sync_api import Page

class ClientPage:
    def __init__(self, page: Page):
        self.page = page

        self.add_button = page.get_by_test_id("buttonAdd")

        self.primary_type_button = page.get_by_test_id("buttonTypePerson").first
        self.secondary_type_button = page.get_by_test_id("buttonTypePerson").last

        self.name_input = page.get_by_test_id("inputName")
        self.cnpj_input = page.get_by_test_id("inputCNPJ")
        self.cpf_input = page.get_by_test_id("inputCPF")
        self.ie_input = page.get_by_test_id("inputIE")
        self.uf_select = page.get_by_test_id("selectUF")
        self.email_input = page.get_by_test_id("inputEmail")
        self.phone_input = page.get_by_test_id("inputTelefone")
        self.obs_input = page.get_by_test_id("inputObs")
        self.save_button = page.get_by_test_id("buttonSalvar")

    def create_cnpj(
            self,
            name: str,
            cnpj: str,
            ie: str,
            uf: str,
            email: str,
            phone: str,
            obs: str,
    ):
        self.add_button.click()
        self.name_input.wait_for(state="visible")
        self.primary_type_button.click()

        self.name_input.fill(name)
        self.cnpj_input.fill(cnpj)
        self.ie_input.fill(ie)
        self.uf_select.select_option(uf)
        self.email_input.fill(email)
        self.phone_input.fill(phone)
        self.obs_input.fill(obs)

        self.save_button.click()

    def create_cpf(
            self,
            name: str,
            cpf: str,
            email: str,
            phone: str,
            obs: str,
    ):
        self.add_button.click()
        self.name_input.wait_for(state="visible")
        self.secondary_type_button.click()

        self.name_input.fill(name)
        self.cpf_input.fill(cpf)
        self.email_input.fill(email)
        self.phone_input.fill(phone)
        self.obs_input.fill(obs)

        self.save_button.click()