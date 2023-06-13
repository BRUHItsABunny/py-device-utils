import unittest

from deviceutils import AndroidDeviceVersion
from deviceutils.android_device.utils_android_version import version_from_version_string, version_to_version_string, version_to_sdk_string, version_from_sdk_string


class TestAndroidDeviceVersion(unittest.TestCase):
    def test_parse(self):
        print(AndroidDeviceVersion._member_map_)
        print(AndroidDeviceVersion._value2member_map_)
        version = version_from_version_string("10.0")
        print(version)
        print(version_to_version_string(version))
        print(version_to_sdk_string(version))
        print(version_to_version_string(version_from_sdk_string("30")))
