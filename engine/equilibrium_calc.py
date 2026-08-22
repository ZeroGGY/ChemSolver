"""
Chemical equilibrium (Kc) calculations.
"""

from typing import Tuple, List

def calculate_kc(
    a_conc: float, b_conc: float, c_conc: float, d_conc: float,
    a_coeff: int, b_coeff: int, c_coeff: int, d_coeff: int
) -> Tuple[float, List[str]]:
    numerator = (c_conc ** c_coeff) * (d_conc ** d_coeff)
    denominator = (a_conc ** a_coeff) * (b_conc ** b_coeff)
    kc = numerator / denominator

    steps = [
        rf"\text{{General Reaction: }} {a_coeff}\text{{A}} + {b_coeff}\text{{B}} \rightleftharpoons {c_coeff}\text{{C}} + {d_coeff}\text{{D}}",
        rf"\text{{Kc Expression: }} K_c = \frac{{[\text{{C}}]^{{{c_coeff}}} [\text{{D}}]^{{{d_coeff}}}}}{{[\text{{A}}]^{{{a_coeff}}} [\text{{B}}]^{{{b_coeff}}}}}",
        rf"\text{{Substitute concentrations: }} K_c = \frac{{({c_conc})^{{{c_coeff}}} \times ({d_conc})^{{{d_coeff}}}}}{{({a_conc})^{{{a_coeff}}} \times ({b_conc})^{{{b_coeff}}}}}",
        rf"K_c = {kc:.4e}"
    ]
    return kc, steps