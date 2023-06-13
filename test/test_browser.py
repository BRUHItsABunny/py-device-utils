import json
import unittest

import deviceutils
from deviceutils import get_browser_headers


class TestLocale(unittest.TestCase):
    def test_parse(self):
        browser = deviceutils.get_random_browser()
        print(browser)
        print(json.dumps(get_browser_headers(browser)))
