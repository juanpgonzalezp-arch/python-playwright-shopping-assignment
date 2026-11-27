# Open the application and enter the supplied demo username and password.
# Click Login and verify that the Products page appears.
# Print PASS only after your verification succeeds.
# Save 02_products_page.png, keep the browser visible for 10 seconds, then close it.
# Expected result The user reaches the Products page and your check passes.
# Small hint Choose something visible after login that was missing before login. Use it as evidence.
# Optional challenge Try locked_out_user with the same password and verify the locked-account warning.

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username", exact=True).fill("standard_user")
    page.get_by_placeholder("Password", exact=True).fill("secret_sauce")
    page.get_by_role("button", name="Login", exact=True).click()

    product_page = page.locator('[data-test="title"]')
    expect(product_page).to_have_text("Products")
    print("Browser page:", product_page.inner_text())
    print("PASS: the product page appears after login")
    page.screenshot(path="02_products_page.png")
    page.wait_for_timeout(10_000) #keep the page visible for 10 seconds.
    browser.close()

