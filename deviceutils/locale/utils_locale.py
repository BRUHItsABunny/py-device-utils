from deviceutils import Locale


def get_country_from_locale(locale: Locale, iso: bool = True) -> str:
    country = locale.country_iso
    if iso:
        return country.upper()
    return country.lower()


def locale_to_string(locale: Locale, separator: str, iso: bool = True) -> str:
    return locale.language.lower() + separator + get_country_from_locale(locale, iso)


def locale_from_string(locale_str: str) -> Locale:
    locale = Locale()

    parts = []
    if "-" in locale_str:
        parts = locale_str.split("-")
    elif "_" in locale_str:
        parts = locale_str.split("_")

    if len(parts) == 2:
        locale.language = parts[0].lower()
        locale.country_i_s_o = parts[1].upper()
    else:
        raise Exception("the supplied locale had an unsupported format")
    return locale
