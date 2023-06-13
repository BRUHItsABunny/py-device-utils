import random

from deviceutils import AndroidDevice, new_device_id, get_random_location, SIMCardIMEI, randomize_simcard, \
    generate_imei, MAC, AndroidDeviceBuildData, ScreenData, CPUDataArchitecture, CPUData, version_from_version_string, \
    locale_from_string, version_to_version_string, locale_to_string
from deviceutils.android_device.db_android_devices import DB_DEVICES, AVAILABLE_DEVICES


def get_device_from_db(device_key: str) -> AndroidDevice:
    device: AndroidDevice = DB_DEVICES[device_key]
    # randomize factors
    device.id = new_device_id()
    device.location = get_random_location(device.locale.country_i_s_o)
    for sim in device.sim_slots:
        randomize_simcard(sim, device.locale.country_i_s_o)
        if sim.imei is None:
            sim.imei = SIMCardIMEI()
        generate_imei(sim.imei, "", "")
    if device.mac_address is None:
        device.mac_address = MAC()
    return device


def get_random_device() -> AndroidDevice:
    device: AndroidDevice = DB_DEVICES[random.choice(AVAILABLE_DEVICES)]
    # randomize factors
    device.id = new_device_id()
    device.location = get_random_location(device.locale.country_i_s_o)
    for sim in device.sim_slots:
        randomize_simcard(sim, device.locale.country_i_s_o)
        if sim.imei is None:
            sim.imei = SIMCardIMEI()
        generate_imei(sim.imei, "", "")
    if device.mac_address is None:
        device.mac_address = MAC()
    return device


def device_from_fingerprint(fingerprint: str) -> AndroidDevice:
    device = AndroidDevice()
    device.build = AndroidDeviceBuildData()
    device.screen = ScreenData()
    device.cpu = CPUData(arch=CPUDataArchitecture.ARM64, abi_list=["arm64-v8a", "armeabi-v7a", "armeabi"])

    main_parts = fingerprint.split("/")
    device.build.manufacturer = main_parts[0]
    device.build.product = main_parts[1]
    sub_parts = main_parts[2].split(":")
    device.build.device = sub_parts[0]
    device.version = version_from_version_string(sub_parts[1])

    device.build.id = main_parts[3]
    sub_parts = main_parts[4].split(":")
    device.build.incremental_version = sub_parts[0]
    device.build.type = sub_parts[1]
    device.build.tags = main_parts[5]

    return device


def device_from_user_agent(user_agent: str) -> AndroidDevice:
    device = AndroidDevice()
    device.build = AndroidDeviceBuildData()
    device.screen = ScreenData()
    device.cpu = CPUData(arch=CPUDataArchitecture.ARM64, abi_list=["arm64-v8a", "armeabi-v7a", "armeabi"])

    index_start = user_agent.index("(")
    index_stop = user_agent.index(")")
    device_str = user_agent[index_start:index_stop]
    for element in device_str.split("; "):
        if "Android " in element:
            device.version = version_from_version_string(element.split(" ")[1])
        elif "-" in element:
            device.locale = locale_from_string(element)
        elif "Build/" in element:
            parts = element.split(" Build/")
            device.build.model = parts[0]
            device.build.id = parts[1]
    return device


def get_user_agent(device: AndroidDevice) -> str:
    return "(Linux; Android {}; {}; {} Build/{})".format(
        version_to_version_string(device.version),
        locale_to_string(device.locale, "-", True),
        device.build.model,
        device.build.id
    )


def get_fingerprint(device: AndroidDevice) -> str:
    return "{}/{}/{}:{}/{}/{}:{}/{}".format(
        device.build.manufacturer,
        device.build.product,
        device.build.device,
        version_to_version_string(device.version),
        device.build.id,
        device.build.incremental_version,
        device.build.type,
        device.build.tags
    )
