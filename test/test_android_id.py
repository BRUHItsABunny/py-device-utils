import unittest

from deviceutils.android_device import *


class TestAndroidDeviceId(unittest.TestCase):
    def test_randomize(self):
        device_id = new_device_id()
        print(device_id_to_hex(device_id))
        print(device_id_to_base64(device_id))
        print(device_id_to_decimal_string(device_id))
