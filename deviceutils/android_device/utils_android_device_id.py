import base64
import random

from deviceutils import AndroidDeviceID


def new_device_id() -> AndroidDeviceID:
    return random_device_id(AndroidDeviceID())


def random_device_id(device_id: AndroidDeviceID) -> AndroidDeviceID:
    return device_id_from_hex(device_id, random.randbytes(8).hex())


def device_id_from_hex(device_id: AndroidDeviceID, id_str: str) -> AndroidDeviceID:
    device_id.id = int(id_str, 16)
    return device_id


def device_id_to_hex(device_id: AndroidDeviceID) -> str:
    return hex(device_id.id)[2:]


def device_id_to_decimal_string(device_id: AndroidDeviceID) -> str:
    return str(device_id.id)


def device_id_to_base64(device_id: AndroidDeviceID) -> str:
    return str(base64.b64encode(bytes.fromhex(device_id_to_hex(device_id))), "utf-8")
