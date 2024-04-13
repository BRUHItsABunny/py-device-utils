import unittest

from deviceutils.location import get_random_location


class TestLocale(unittest.TestCase):
    def test_parse(self):
        device = get_random_location('US')
        print(device.to_json())
