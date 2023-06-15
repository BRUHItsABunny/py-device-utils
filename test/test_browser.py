import json
import unittest

from deviceutils.browser import get_random_browser, get_browser_headers


class TestLocale(unittest.TestCase):
    def test_parse(self):
        browser = get_random_browser()
        print(browser)
        print(json.dumps(get_browser_headers(browser)))
