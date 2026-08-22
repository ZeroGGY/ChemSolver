"""
Mole concept calculations.
"""

from typing import Dict, Tuple, List

ATOMIC_MASSES: Dict[str, float] = {
    "H": 1.008, "He": 4.003, "Li": 6.941, "Be": 9.012, "B": 10.81,
    "C": 12.011, "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180,
    "Na": 22.990, "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974,
    "S": 32.06, "Cl": 35.45, "K": 39.098, "Ca": 40.078, "Fe": 55.845,
    "Cu": 63.546, "Zn": 65.38, "Ag": 107.87, "I": 126.90
}

AVOGADRO_NUMBER: float = 6.022e23

def calculate_moles_from_mass(mass_g: float, molar_mass: float) -> Tuple[float, List[str]]:
    moles = mass_g / molar_mass
    steps = [
        rf"\text{{Formula: }} n = \frac{{m}}{{M}}",
        rf"\text{{Substitute values: }} n = \frac{{{mass_g}}}{{{molar_mass}}}",
        rf"n = {moles:.4f} \text{{ moles}}"
    ]
    return moles, steps

def calculate_mass_from_moles(moles: float, molar_mass: float) -> Tuple[float, List[str]]:
    mass = moles * molar_mass
    steps = [
        rf"\text{{Formula: }} m = n \times M",
        rf"\text{{Substitute values: }} m = {moles} \times {molar_mass}",
        rf"m = {mass:.4f} \text{{ g}}"
    ]
    return mass, steps

def calculate_particles(moles: float) -> Tuple[float, List[str]]:
    particles = moles * AVOGADRO_NUMBER
    steps = [
        rf"\text{{Formula: }} N = n \times N_A",
        rf"\text{{Where }} N_A = 6.022 \times 10^{{23}} \text{{ particles/mol}}",
        rf"\text{{Substitute values: }} N = {moles} \times (6.022 \times 10^{{23}})",
        rf"N = {particles:.4e} \text{{ particles}}"
    ]
    return particles, steps

def calculate_moles_from_particles(particles: float) -> Tuple[float, List[str]]:
    moles = particles / AVOGADRO_NUMBER
    steps = [
        rf"\text{{Formula: }} n = \frac{{N}}{{N_A}}",
        rf"\text{{Substitute values: }} n = \frac{{{particles:.4e}}}{{6.022 \times 10^{{23}}}}",
        rf"n = {moles:.4f} \text{{ moles}}"
    ]
    return moles, steps