from playwright.sync_api import sync_playwright

def test_calculator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Přejděte na stránku kalkulačky
        page.goto("https://calculator-online.net/cs/")

        # Čekání na načtení tlačítka cookies a kliknutí na přijetí
        page.wait_for_selector('#accept-choices')  # Selektor pro tlačítko cookies
        page.click('#accept-choices')  # Kliknutí na tlačítko cookies

        # Příklad: testování matematických funkcí 256 ÷ 25 x 60
        page.click('span.bg-white:has-text("2")')  # Selektor pro číslo 2
        page.click('span.bg-white:has-text("5")')  # Selektor pro číslo 5
        page.click('span.bg-white:has-text("6")')  # Selektor pro číslo 6
        page.click('span.grey_color:has-text("÷")')  # Selektor pro ÷
        page.click('span.bg-white:has-text("2")')  # Selektor pro číslo 2
        page.click('span.bg-white:has-text("5")')  # Selektor pro číslo 5
        page.click('span.grey_color:has-text("×")')  # Selektor pro x
        page.click('span.bg-white:has-text("6")')  # Selektor pro číslo 6
        page.click('span.bg-white:has-text("0")')  # Selektor pro číslo 0
        page.click('span.blue_btn:has-text("=")')  # Selektor pro =

        result = page.text_content('#showOutput').replace('\xa0', '').strip()  # Nahrazení nezlomitelné mezery a odstranění bílých znaků
        assert result == "614.4", f'Expected 614.4 but got {result}'

        browser.close()

if __name__ == "__main__":
    test_calculator()
