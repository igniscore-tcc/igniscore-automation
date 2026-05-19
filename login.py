import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context()

    page = context.new_page()

    page.goto("https://front-end-tcc-lovat.vercel.app/login")

    page.get_by_role("textbox", name="Email").fill("")

    page.get_by_role("textbox", name="Senha").fill("")

    page.get_by_role("button", name="Entrar").click()

    expect(page).to_have_url(re.compile(r".*/dashboard"))

    page.wait_for_timeout(60000)

    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)