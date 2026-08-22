import math

def calculate_ph_from_h(h_conc):
    if h_conc <= 0:
        raise ValueError("[H+] concentration must be greater than 0.")
    ph = -math.log10(h_conc)
    poh = 14.0 - ph
    oh_conc = 10 ** (-poh)
    return ph, poh, oh_conc

def calculate_poh_from_oh(oh_conc):
    if oh_conc <= 0:
        raise ValueError("[OH-] concentration must be greater than 0.")
    poh = -math.log10(oh_conc)
    ph = 14.0 - poh
    h_conc = 10 ** (-ph)
    return ph, poh, h_conc

def calculate_ph_from_oh(oh_conc):
    return calculate_poh_from_oh(oh_conc)

def calculate_h_from_ph(ph):
    if ph < 0 or ph > 14:
        raise ValueError("pH should typically be between 0 and 14.")
    h_conc = 10 ** (-ph)
    poh = 14.0 - ph
    oh_conc = 10 ** (-poh)
    return h_conc, poh, oh_conc

def calculate_oh_from_poh(poh):
    if poh < 0 or poh > 14:
        raise ValueError("pOH should typically be between 0 and 14.")
    oh_conc = 10 ** (-poh)
    ph = 14.0 - poh
    h_conc = 10 ** (-ph)
    return h_conc, ph, oh_conc