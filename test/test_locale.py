import unittest

from deviceutils.locale import locale_from_string


class TestLocale(unittest.TestCase):
    def test_parse(self):
        locale = locale_from_string("en_US")
        print(locale.to_dict())
        locale = locale_from_string("en-US")
        print(locale.to_dict())
