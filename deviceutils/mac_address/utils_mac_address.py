import os

from deviceutils import Mac


def randomize_mac_address(mac: Mac, oui: str, multi_cast: bool, uua: bool):
    if oui == "":
        oui = mac.oui
    mac_bytes = bytearray(os.urandom(6))
    if multi_cast:
        mac_bytes[0] |= 0
    else:
        mac_bytes[0] ^= 1
    if uua:
        mac_bytes[0] ^= 1 << 1
    else:
        mac_bytes[0] |= 1 << 1
