import random

from deviceutils import Browser
from deviceutils.browser.db_browsers import AVAILABLE_BROWSERS, DB_BROWSERS


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
