import unittest

import deviceutils.android_device
from deviceutils.android_device import get_user_agent, get_fingerprint


class TestLocale(unittest.TestCase):
    def test_parse(self):
        device = deviceutils.android_device.get_random_device()
        print(device.to_json())
        print(get_user_agent(device))
        print(get_fingerprint(device))
