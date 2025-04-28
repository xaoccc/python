import time
from playwright.sync_api import sync_playwright

post_text = ["post_text1", "post_text2", "post_text3"]
def my_bot(post):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.threads.com/", wait_until="load")
        page.locator("text=Allow all cookies").click()
        page.locator("text=Log in").click()
        page.locator("text=Continue with instagram").click()
        page.fill('input[placeholder="Username, phone or email"]', "USERNAME")
        page.fill('input[placeholder="Password"]', "PASSWORD")

        page.locator('div[role="button"]').nth(1).click()
        page.locator('div[aria-label="Empty text field. Type to compose a new post."]').click()
        page.locator('div[aria-placeholder="What\'s new?"]').fill(post)

        post_button = page.get_by_role("button", name="Post")
        post_button.click(force=True)
        browser.close()

for i in range(3):
    my_bot(post_text[i])
    if i != 2:
        print("Sleeping for 1 hour...")
        time.sleep(3600)