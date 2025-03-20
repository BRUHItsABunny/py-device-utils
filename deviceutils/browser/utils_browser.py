import random

from deviceutils import Browser
from deviceutils.browser.db_browsers import AVAILABLE_BROWSERS, DB_BROWSERS
from typing import Dict, List, Union, Optional
import aiohttp

def get_random_browser(brand: str = "") -> Browser:
    if brand not in AVAILABLE_BROWSERS:
        brand = random.choice(AVAILABLE_BROWSERS)
    browsers = DB_BROWSERS[brand]
    return browsers[random.choice(list(browsers.keys()))]


def get_browser_headers(browser: Browser, product_override: str = "", platform: str = "", is_mobile: bool = False) -> dict:
    if platform == "":
        platform = "\"Windows\""

    ua_product_start = browser.user_agent.index("(")
    ua_product_end = browser.user_agent.index(")")
    ua_start = browser.user_agent[0:ua_product_start+1]
    ua_end = browser.user_agent[ua_product_end:]

    if product_override == "":
        product_override = browser.user_agent[ua_product_start+1:ua_product_end]

    result = {
        "User-Agent": ua_start + product_override + ua_end
    }

    if browser.brand_header != "":
        result["sec-ch-ua"] = browser.brand_header
        result["sec-ch-ua-platform"] = platform
        result["sec-ch-ua-mobile"] = "?0"
        if is_mobile:
            result["sec-ch-ua-mobile"] = "?1"
    return result


def set_sec_fetch_headers(
        headers: Dict[str, Union[str, List[str]]],
        site: Optional[str] = None,
        mode: Optional[str] = None,
        dest: Optional[str] = None,
) -> Dict[str, Union[str, List[str]]]:
    if site is None:
        site = 'same-origin'
    if mode is None:
        mode = 'cors'
    if dest is None:
        dest = 'empty'

    headers['sec-fetch-site'] = site
    headers['sec-fetch-mode'] = mode
    headers['sec-fetch-dest'] = dest
    return headers


brand_permutations: List[List[int]] = [
    [0, 1, 2],
    [0, 2, 1],
    [1, 0, 2],
    [1, 2, 0],
    [2, 0, 1],
    [2, 1, 0],
]

greasy_chars: List[str] = [' ', '(', ':', '-', '.', '/', ')', ';', '=', '?', '_']
greasy_chars_legacy: List[str] = [' ', ' ', ';']
greased_versions: List[str] = ['8', '99', '24']


def generate_brand_header(brand: str, major_version: int, use_legacy: bool = False) -> str:
    result: List[Optional[str]] = [None] * 3
    order = brand_permutations[major_version % len(brand_permutations)]

    if not use_legacy:
        grease = (
            f'"Not{greasy_chars[major_version % len(greasy_chars)]}A'
            f'{greasy_chars[(major_version + 1) % len(greasy_chars)]}Brand";v="{greased_versions[major_version % len(greased_versions)]}"'
        )
    else:
        grease = (
            f'"{greasy_chars_legacy[order[0]]}Not{greasy_chars_legacy[order[1]]}A'
            f'{greasy_chars_legacy[order[2]]}Brand";v="{greased_versions[1]}"'
        )

    if len(brand) > 0:
        result = [None] * 3
        result[order[0]] = grease
        result[order[1]] = f'"Chromium";v="{major_version}"'
        result[order[2]] = f'"{brand}";v="{major_version}"'
    else:
        result = [None] * 2
        result[major_version % 2] = grease
        result[(major_version + 1) % 2] = f'"Chromium";v="{major_version}"'

    return ', '.join(filter(None, result))


PlatformWindows = 'win'
PlatformWindows64 = 'win64'
PlatformIOS = 'ios'
PlatformAndroid = 'android'
PlatformMac = 'mac'
PlatformMacARM64 = 'mac_arm64'
PlatformLinux = 'linux'

ChannelExtended = 'extended'
ChannelStable = 'stable'
ChannelBeta = 'beta'
ChannelDev = 'dev'
ChannelCanary = 'canary'


class ChromiumVersion:
    def __init__(self, name: str, version: str) -> None:
        self.name = name
        self.version = version

    def get_major_version(self) -> int:
        parts = self.version.split('.')
        try:
            return int(parts[0])
        except (ValueError, IndexError):
            return 0

    def get_ua_version(self) -> str:
        major_str = self.version.split('.')[0]
        return f"{major_str}.0.0.0"


async def get_latest_chromium(
        index: int,
        platform: str = PlatformWindows,
        channel_id: str = ChannelStable
) -> ChromiumVersion:
    req_url = f"https://versionhistory.googleapis.com/v1/chrome/platforms/{platform}/channels/{channel_id}/versions"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(req_url) as response:
                response.raise_for_status()
                resp_parsed = await response.json()
                versions = resp_parsed.get("versions", [])
                versions_length = len(versions)

                if versions_length == 0:
                    raise Exception("No versions found in the response.")

                if index < 0:
                    unsigned_index = -index
                    version_index = (versions_length - (unsigned_index % versions_length)) % versions_length
                else:
                    version_index = index % versions_length

                version_data = versions[version_index]
                return ChromiumVersion(version_data["name"], version_data["version"])
    except Exception as error:
        raise Exception(f"Failed to get Chromium version: {error}") from error
