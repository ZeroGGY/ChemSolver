"""
Solution chemistry calculations.
"""

from typing import Tuple, List

def calculate_molarity(moles: float, volume_liters: float) -> Tuple[float, List[str]]:
    molarity = moles / volume_liters
    steps = [
        rf"\text{{Formula: }} M = \frac{{n}}{{V \text{{ (L)}}}}",
        rf"\text{{Substitute values: }} M = \frac{{{moles}}}{{{volume_liters}}}",
        rf"M = {molarity:.4f} \text{{ M (mol/L)}}"
    ]
    return molarity, steps

def calculate_moles_for_solution(molarity: float, volume_liters: float) -> Tuple[float, List[str]]:
    moles = molarity * volume_liters
    steps = [
        rf"\text{{Formula: }} n = M \times V \text{{ (L)}}",
        rf"\text{{Substitute values: }} n = {molarity} \times {volume_liters}",
        rf"n = {moles:.4f} \text{{ moles}}"
    ]
    return moles, steps

def calculate_mass_percent(solute_mass: float, solution_mass: float) -> Tuple[float, List[str]]:
    percent = (solute_mass / solution_mass) * 100
    steps = [
        rf"\text{{Formula: }} \% (w/w) = \left( \frac{{\text{{Mass of Solute}}}}{{\text{{Mass of Solution}}}} \right) \times 100",
        rf"\text{{Substitute values: }} \% (w/w) = \left( \frac{{{solute_mass}}}{{{solution_mass}}} \right) \times 100",
        rf"\% (w/w) = {percent:.2f}\%"
    ]
    return percent, steps

def calculate_volume_percent(solute_vol: float, solution_vol: float) -> Tuple[float, List[str]]:
    percent = (solute_vol / solution_vol) * 100
    steps = [
        rf"\text{{Formula: }} \% (v/v) = \left( \frac{{\text{{Volume of Solute}}}}{{\text{{Volume of Solution}}}} \right) \times 100",
        rf"\text{{Substitute values: }} \% (v/v) = \left( \frac{{{solute_vol}}}{{{solution_vol}}} \right) \times 100",
        rf"\% (v/v) = {percent:.2f}\%"
    ]
    return percent, steps