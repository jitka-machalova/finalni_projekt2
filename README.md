# finalni_projekt2
# Odevzdání úkolu č. 2

test.calculator.py
from playwright.sync_api import sync_playwright


def test_calculator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Přejděte na stránku kalkulačky
        page.goto("https://calculator-online.net/cs/")

        # Příklad: testování sčítání 1 + 5
        page.click("SELECTOR_FOR_NUMBER_1")
        page.click("SELECTOR_FOR_PLUS")
        page.click("SELECTOR_FOR_NUMBER_5")
        page.click("SELECTOR_FOR_RESULT")

        # Ověření výsledku
        result = page.text_content("SELECTOR_FOR_RESULT_DISPLAY")
        assert result == "6", f'Expected 6 but got {result}'

        browser.close()


if __name__ == "__main__":
    test_calculator()

# finalni_projekt2
# Odevzdání úkolu č. 2

test.calculator2.py
from playwright.sync_api import sync_playwright


def test_calculator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Přejděte na stránku kalkulačky
        page.goto("https://calculator-online.net/cs/")

        # Příklad: testování odčítání 5 - 1
        page.click("SELECTOR_FOR_NUMBER_5")
        page.click("SELECTOR_FOR_MINUS")
        page.click("SELECTOR_FOR_NUMBER_1")
        page.click("SELECTOR_FOR_RESULT")

        # Ověření výsledku
        result = page.text_content("SELECTOR_FOR_RESULT_DISPLAY")
        assert result == "4", f'Expected 4 but got {result}'

        browser.close()


if __name__ == "__main__":
    test_calculator()

# finalni_projekt2
# Odevzdání úkolu č. 2

test.calculator3.py
from playwright.sync_api import sync_playwright


def test_calculator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Přejděte na stránku kalkulačky
        page.goto("https://calculator-online.net/cs/")

        # Příklad: testování dělení 6/2
        page.click("SELECTOR_FOR_NUMBER_6")
        page.click("SELECTOR_FOR_DIVIDED")
        page.click("SELECTOR_FOR_NUMBER_2")
        page.click("SELECTOR_FOR_RESULT")

        # Ověření výsledku
        result = page.text_content("SELECTOR_FOR_RESULT_DISPLAY")
        assert result == "3", f'Expected 3 but got {result}'

        browser.close()


if __name__ == "__main__":
    test_calculator()


# finalni_projekt2
# Odevzdání úkolu č. 2

test.calculator4.py
from playwright.sync_api import sync_playwright


def test_calculator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Přejděte na stránku kalkulačky
        page.goto("https://calculator-online.net/cs/")

        # Příklad: testování násobení 6 x 2
        page.click("SELECTOR_FOR_NUMBER_6")
        page.click("SELECTOR_FOR_MULTIPLICATION")
        page.click("SELECTOR_FOR_NUMBER_2")
        page.click("SELECTOR_FOR_RESULT")

        # Ověření výsledku
        result = page.text_content("SELECTOR_FOR_RESULT_DISPLAY")
        assert result == "12", f'Expected 12 but got {result}'

        browser.close()


if __name__ == "__main__":
    test_calculator()

# finalni_projekt2
# Odevzdání úkolu č. 2

test.calculator5.py
from playwright.sync_api import sync_playwright


def test_calculator():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Přejděte na stránku kalkulačky
        page.goto("https://calculator-online.net/cs/")

        # Příklad: testování výpočtů 256 ÷ 25 x 60
        page.click("SELECTOR_FOR_NUMBER_256")
        page.click("SELECTOR_FOR_DIVIDED")
        page.click("SELECTOR_FOR_NUMBER_25")
        page.click("SELECTOR_FOR_MULTIPLICATION")
        page.click("SELECTOR_FOR_NUMBER_60")
        page.click("SELECTOR_FOR_RESULT")

        # Ověření výsledku
        result = page.text_content("SELECTOR_FOR_RESULT_DISPLAY")
        assert result == "214.40", f'Expected 214.40 but got {result}'

        browser.close()


if __name__ == "__main__":
    test_calculator()

