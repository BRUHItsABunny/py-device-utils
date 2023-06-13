import copy
import random

from deviceutils import GPSLocation, GPSLocationLocationProvider
from deviceutils.location.db_countries import *
from deviceutils.location.db_cities import *
from deviceutils.location.db_locations import *


def get_location_accuracy(location: GPSLocation) -> int:
    if location.provider.value == 0:
        return random.randint(1, 3)
    return location.provider.value


def get_location_provider_string(location: GPSLocation) -> str:
    provider_value = get_location_accuracy(location)
    return GPSLocationLocationProvider._value2member_map_[provider_value].name.lower()


def get_random_location(country_iso: str) -> GPSLocation:
    if country_iso not in AVAILABLE_COUNTRIES:
        country_iso = random.choice(AVAILABLE_COUNTRIES)
    city = random.choice(AVAILABLE_CITIES[country_iso])
    location = LOCATION_DB[country_iso][city]
    return copy.deepcopy(location)
