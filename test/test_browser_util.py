import unittest

from deviceutils.browser import get_latest_chromium, generate_brand_header, random_browser_version_by_name


class MyTestCase(unittest.IsolatedAsyncioTestCase):
    async def test_get_latest_chromium(self):
        browser = random_browser_version_by_name("chrome")
        if browser is None:
            return

        latest_chrome = await get_latest_chromium(0)
        print("Latest Chromium:", latest_chrome.__dict__)

        browser.user_agent = (
            f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            f"AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/{latest_chrome.get_ua_version()} Safari/537.36"
        )

        # Build the brand header using the generated header function
        browser.brand_header = generate_brand_header("Google Chrome", latest_chrome.get_major_version())

        print("User Agent:", browser.user_agent)
        print("Brand Header:", browser.brand_header)
