import copy
import random

from deviceutils import SimCard, SimCardImei
from deviceutils.location import AVAILABLE_COUNTRIES
from deviceutils.simcard.utils_luhn import luhn_calculate
from deviceutils.simcard.db_simcard import DB_SIMCARDS


def generate_imei(imei: SimCardImei, tac: str, serial: str) -> str:
    if tac == "":
        tac = imei.tac
    while len(tac) < 8:
        tac += str(random.randint(0, 9))
    while len(serial) < 6:
        serial += str(random.randint(0, 9))
    imei_int = int(tac + serial)
    imei.imei = tac + serial + str(luhn_calculate(imei_int))
    return imei.imei


def get_carrier_name(sim: SimCard, heuristic: bool) -> str:
    if heuristic:
        return sim.carrier.split(" ")[0]
    return sim.carrier


def get_hni(sim: SimCard) -> str:
    if sim.mnc.isdigit() and sim.mcc.isdigit():
        hni = sim.mcc + sim.mnc
        if len(hni) < 5:
            return "000000"
        return hni
    return "000000"


def randomize_simcard(sim: SimCard, country_iso: str):
    if country_iso not in AVAILABLE_COUNTRIES:
        country_iso = random.choice(AVAILABLE_COUNTRIES)
    rand_sim: SimCard = random.choice(DB_SIMCARDS[country_iso])
    sim.m_n_c = rand_sim.mnc
    sim.m_c_c = rand_sim.mcc
    sim.country_i_s_o = rand_sim.country_iso
    sim.country_code = rand_sim.country_code


def get_random_simcard(country_iso: str) -> SimCard:
    if country_iso not in AVAILABLE_COUNTRIES:
        country_iso = random.choice(AVAILABLE_COUNTRIES)
    rand_sim: SimCard = random.choice(DB_SIMCARDS[country_iso])
    sim = copy.deepcopy(rand_sim)
    sim.imei = SimCardImei()
    generate_imei(sim.imei, "", "")
    return sim
