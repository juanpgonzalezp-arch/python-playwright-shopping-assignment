#Open Chromium with the browser visible and navigate to the application.
#Print the page title in the terminal.
#Save a screenshot as 01_login_page.png.
#Keep the browser visible for 10 seconds, then close it.
#Expected result The login page opens, the title appears in the terminal and the screenshot is saved.
#Small hint Follow the same order as a person opening a website: browser, tab, then address.

from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com/")
    print("Page title:", page.title())
    page.screenshot(path="01_login_page.png")
    page.wait_for_timeout(10_000) #keep the page visible for 5 seconds.
    browser.close()