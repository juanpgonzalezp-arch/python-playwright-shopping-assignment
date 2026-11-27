#Open the application and log in.
#Choose two different products and add both to the cart.
#Verify that the cart count is two.
#Remove one of those products and verify that the count changes to one.
#Open the cart. Verify that the correct product remains and the removed product is absent.
#Print PASS after all checks succeed. Save 03_cart_result.png, keep the browser visible for 10 seconds, then close it.
#Expected result Exactly one product remains in the cart, and it is the product you kept.
#Small hint Each product has its own button. Make sure your action applies to the product you selected.



from playwright.sync_api import expect, sync_playwright
with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username", exact=True).fill("standard_user")
    page.get_by_placeholder("Password", exact=True).fill("secret_sauce")
    page.get_by_role("button", name="Login", exact=True).click()

    # Add two products to the cart
    page.locator('[data-test="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    page.locator('[data-test="add-to-cart-sauce-labs-bike-light"]').click()

    # Verify cart count is 2
    #expect(page.locator('[data-test="shopping-cart-badge"]')).to_have_text("2")
    cart_count = page.locator('[data-test="shopping-cart-badge"]').inner_text()
    assert cart_count == "2"
    print("PASS: Two products added to the cart.")

    #Remove one product from the cart
    page.locator('[data-test="remove-sauce-labs-bolt-t-shirt"]').click()

    # Verify cart count is 1
    cart_count = page.locator('[data-test="shopping-cart-badge"]').inner_text()
    assert cart_count == "1"
    print("PASS: One product removed from the cart.")

    #verify that the correct product remains in the cart
    page.locator('[data-test="shopping-cart-link"]').click()
    product_name = page.locator('[data-test="inventory-item-name"]').inner_text()
    assert product_name == "Sauce Labs Bike Light"
    print("PASS: The correct product remains in the cart after removal. that is:", product_name )
    page.screenshot(path="03_cart_result.png")

    #Browser wait for 10 seconds before closing
    page.wait_for_timeout(10_000) #keep the page visible for 10 seconds.
    browser.close()