from playwright.sync_api import Page  # Mudou para sync_api

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        self.add_button = page.get_by_test_id("buttonAdd")
        self.name_input = page.get_by_test_id("inputName")
        self.type_select = page.get_by_test_id("selectType")
        self.validity_trigger = page.get_by_test_id("datePickerValidity")
        self.lot_input = page.get_by_test_id("inputLot")
        self.price_input = page.get_by_test_id("inputPrice")
        self.save_button = page.get_by_test_id("buttonSalvar")

    def select_validity_date(self, day: int | str):
        self.validity_trigger.click()
        # Removido os awaits internos
        self.page.get_by_role("button", name=str(day), exact=True).click()

    def create_product(self, name: str, product_type: str, validity_day: int | str, lot: str, price: str):
        self.add_button.click()
        self.name_input.fill(name)
        self.type_select.select_option(value=product_type)
        self.select_validity_date(validity_day)
        self.lot_input.fill(lot)
        self.price_input.fill(price)
        self.save_button.click()