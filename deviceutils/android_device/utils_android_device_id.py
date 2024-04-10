import base64
import random

from deviceutils import AndroidDeviceId


def new_device_id() -> AndroidDeviceId:
    return random_device_id(AndroidDeviceId())


def random_device_id(device_id: AndroidDeviceId) -> AndroidDeviceId:
    return device_id_from_hex(device_id, random.randbytes(8).hex())


def device_id_from_hex(device_id: AndroidDeviceId, id_str: str) -> AndroidDeviceId:
    device_id.id = int(id_str, 16)
    return device_id


def device_id_to_hex(device_id: AndroidDeviceId) -> str:
    return hex(device_id.id)[2:]


def device_id_to_decimal_string(device_id: AndroidDeviceId) -> str:
    return str(device_id.id)


def device_id_to_base64(device_id: AndroidDeviceId) -> str:
    return str(base64.b64encode(bytes.fromhex(device_id_to_hex(device_id))), "utf-8")
