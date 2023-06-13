from deviceutils import AndroidDeviceVersion

def is_valid_version(version: AndroidDeviceVersion) -> bool:
    if version < 1 or version > 34:
        return False
    return True


def version_from_version_string(version: str) -> AndroidDeviceVersion:
    version_splits = version.split(".")
    if len(version_splits) == 1:
        version_splits.append("0")

    normalized_version = "V" + "_".join(version_splits).upper()
    if normalized_version in AndroidDeviceVersion._member_map_.keys():
        return AndroidDeviceVersion._member_map_[normalized_version]
    return AndroidDeviceVersion.AndroidVersion_NONE


def version_from_sdk_string(sdk_string: str) -> AndroidDeviceVersion:
    if not sdk_string.isdigit():
        return AndroidDeviceVersion.AndroidVersion_NONE
    sdk_int = int(sdk_string)
    if sdk_int < 1 or sdk_int > 34:
        return AndroidDeviceVersion.AndroidVersion_NONE
    return AndroidDeviceVersion._value2member_map_[sdk_int]


def version_to_version_string(version: AndroidDeviceVersion) -> str:
    return version.name[1:].replace("_", ".")


def version_to_sdk_string(version: AndroidDeviceVersion) -> str:
    return str(version)
