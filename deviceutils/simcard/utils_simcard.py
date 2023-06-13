import copy
import random

from deviceutils import SIMCard, SIMCardIMEI
from deviceutils.location import AVAILABLE_COUNTRIES
from deviceutils.simcard.utils_luhn import luhn_calculate
from deviceutils.simcard.db_simcard import DB_SIMCARDS


def generate_imei(imei: SIMCardIMEI, tac: str, serial: str) -> str:
    if tac == "":
        tac = imei.t_a_c
    while len(tac) < 8:
        tac += str(random.randint(0, 9))
    while len(serial) < 6:
        serial += str(random.randint(0, 9))
    imei_int = int(tac + serial)
    imei.imei = tac + serial + str(luhn_calculate(imei_int))
    return imei.imei


def get_carrier_name(sim: SIMCard, heuristic: bool) -> str:
    if heuristic:
        return sim.carrier.split(" ")[0]
    return sim.carrier


def get_hni(sim: SIMCard) -> str:
    if sim.m_n_c.isdigit() and sim.m_c_c.isdigit():
        hni = sim.m_c_c + sim.m_n_c
        if len(hni) < 5:
            return "000000"
        return hni
    return "000000"


def randomize_simcard(sim: SIMCard, country_iso: str):
    if country_iso not in AVAILABLE_COUNTRIES:
        country_iso = random.choice(AVAILABLE_COUNTRIES)
    rand_sim: SIMCard = random.choice(DB_SIMCARDS[country_iso])
    sim.m_n_c = rand_sim.m_n_c
    sim.m_c_c = rand_sim.m_c_c
    sim.country_i_s_o = rand_sim.country_i_s_o
    sim.country_code = rand_sim.country_code


def get_random_simcard(country_iso: str) -> SIMCard:
    if country_iso not in AVAILABLE_COUNTRIES:
        country_iso = random.choice(AVAILABLE_COUNTRIES)
    rand_sim: SIMCard = random.choice(DB_SIMCARDS[country_iso])
    sim = copy.deepcopy(rand_sim)
    sim.imei = SIMCardIMEI()
    generate_imei(sim.imei, "", "")
    return sim
