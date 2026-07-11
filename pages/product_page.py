from playwright.sync_api import Page

class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        self.add_button = page.get_by_test_id("buttonAdd")
        self.name_input = page.get_by_test_id("inputName")
        self.type_select = page.get_by_test_id("selectType")
        self.lot_input = page.get_by_test_id("inputLot")
        self.price_input = page.get_by_test_id("inputPrice")
        self.save_button = page.get_by_test_id("buttonSalvar")

    def select_validity_date(self, day: int | str):
        datepicker_container = self.page.locator("div:has(label:text('Validade'))")
        datepicker_button = datepicker_container.locator("button[type='button']").first

        datepicker_button.wait_for(state="visible")
        datepicker_button.click()

        self.page.wait_for_timeout(400)

        import re
        day_pattern = re.compile(rf"(^|\s){day}(\s|$)")

        self.page.locator("[role='dialog'], [data-radix-popper-content-wrapper]").get_by_role(
            "button", name=day_pattern
        ).filter(
            has_not=self.page.locator("[disabled]")
        ).first.click()

    def create_product(self, name: str, product_type: str, validity_day: int | str, lot: str, price: str):
        self.add_button.wait_for(state="visible")
        self.add_button.click()

        self.name_input.wait_for(state="visible")

        self.name_input.fill(name)
        self.type_select.select_option(value=product_type)

        self.select_validity_date(validity_day)

        self.lot_input.fill(lot)
        self.price_input.fill(price)
        self.save_button.click()