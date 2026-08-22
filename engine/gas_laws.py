"""
Gas Law calculations.
"""

from typing import Tuple, List

R_GAS_CONSTANT: float = 0.0821

def boyles_law(p1: float = None, v1: float = None, p2: float = None, v2: float = None) -> Tuple[float, str, List[str]]:
    steps = [rf"\text{{Formula: }} P_1 V_1 = P_2 V_2"]
    
    if p2 is None:
        p2 = (p1 * v1) / v2
        steps.append(rf"P_2 = \frac{{P_1 V_1}}{{V_2}} = \frac{{{p1} \times {v1}}}{{{v2}}}")
        steps.append(rf"P_2 = {p2:.4f} \text{{ atm}}")
        return p2, "P2", steps
    elif v2 is None:
        v2 = (p1 * v1) / p2
        steps.append(rf"V_2 = \frac{{P_1 V_1}}{{P_2}} = \frac{{{p1} \times {v1}}}{{{p2}}}")
        steps.append(rf"V_2 = {v2:.4f} \text{{ L}}")
        return v2, "V2", steps
    elif p1 is None:
        p1 = (p2 * v2) / v1
        steps.append(rf"P_1 = \frac{{P_2 V_2}}{{V_1}} = \frac{{{p2} \times {v2}}}{{{v1}}}")
        steps.append(rf"P_1 = {p1:.4f} \text{{ atm}}")
        return p1, "P1", steps
    else:
        v1 = (p2 * v2) / p1
        steps.append(rf"V_1 = \frac{{P_2 V_2}}{{P_1}} = \frac{{{p2} \times {v2}}}{{{p1}}}")
        steps.append(rf"V_1 = {v1:.4f} \text{{ L}}")
        return v1, "V1", steps

def charles_law(v1: float = None, t1_c: float = None, v2: float = None, t2_c: float = None) -> Tuple[float, str, List[str]]:
    steps = []
    t1_k = t1_c + 273.15 if t1_c is not None else None
    t2_k = t2_c + 273.15 if t2_c is not None else None
    
    if t1_k:
        steps.append(rf"T_1 = {t1_c}^\circ\text{{C}} + 273.15 = {t1_k:.2f} \text{{ K}}")
    if t2_k:
        steps.append(rf"T_2 = {t2_c}^\circ\text{{C}} + 273.15 = {t2_k:.2f} \text{{ K}}")
        
    steps.append(rf"\text{{Formula: }} \frac{{V_1}}{{T_1}} = \frac{{V_2}}{{T_2}}")

    if v2 is None:
        v2 = (v1 * t2_k) / t1_k
        steps.append(rf"V_2 = \frac{{V_1 T_2}}{{T_1}} = \frac{{{v1} \times {t2_k:.2f}}}{{{t1_k:.2f}}}")
        steps.append(rf"V_2 = {v2:.4f} \text{{ L}}")
        return v2, "V2", steps
    elif t2_c is None:
        t2_k_calc = (v2 * t1_k) / v1
        t2_c_calc = t2_k_calc - 273.15
        steps.append(rf"T_2 \text{{ (K)}} = \frac{{V_2 T_1}}{{V_1}} = \frac{{{v2} \times {t1_k:.2f}}}{{{v1}}} = {t2_k_calc:.2f} \text{{ K}}")
        steps.append(rf"T_2 \text{{ (^\circ C)}} = {t2_k_calc:.2f} - 273.15 = {t2_c_calc:.2f}^\circ\text{{C}}")
        return t2_c_calc, "T2", steps
    elif v1 is None:
        v1 = (v2 * t1_k) / t2_k
        steps.append(rf"V_1 = \frac{{V_2 T_1}}{{T_2}} = \frac{{{v2} \times {t1_k:.2f}}}{{{t2_k:.2f}}}")
        steps.append(rf"V_1 = {v1:.4f} \text{{ L}}")
        return v1, "V1", steps
    else:
        t1_k_calc = (v1 * t2_k) / v2
        t1_c_calc = t1_k_calc - 273.15
        steps.append(rf"T_1 \text{{ (K)}} = \frac{{V_1 T_2}}{{V_2}} = \frac{{{v1} \times {t2_k:.2f}}}{{{v2}}} = {t1_k_calc:.2f} \text{{ K}}")
        steps.append(rf"T_1 \text{{ (^\circ C)}} = {t1_k_calc:.2f} - 273.15 = {t1_c_calc:.2f}^\circ\text{{C}}")
        return t1_c_calc, "T1", steps

def ideal_gas_law(p: float = None, v: float = None, n: float = None, t_c: float = None) -> Tuple[float, str, List[str]]:
    steps = [rf"\text{{Ideal Gas Constant }} R = {R_GAS_CONSTANT} \text{{ L}}\cdot\text{{atm/(mol}}\cdot\text{{K)}}"]
    
    t_k = t_c + 273.15 if t_c is not None else None
    if t_k:
        steps.append(rf"T = {t_c}^\circ\text{{C}} + 273.15 = {t_k:.2f} \text{{ K}}")
        
    steps.append(rf"\text{{Formula: }} PV = nRT")

    if p is None:
        p = (n * R_GAS_CONSTANT * t_k) / v
        steps.append(rf"P = \frac{{nRT}}{{V}} = \frac{{{n} \times {R_GAS_CONSTANT} \times {t_k:.2f}}}{{{v}}}")
        steps.append(rf"P = {p:.4f} \text{{ atm}}")
        return p, "P", steps
    elif v is None:
        v = (n * R_GAS_CONSTANT * t_k) / p
        steps.append(rf"V = \frac{{nRT}}{{P}} = \frac{{{n} \times {R_GAS_CONSTANT} \times {t_k:.2f}}}{{{p}}}")
        steps.append(rf"V = {v:.4f} \text{{ L}}")
        return v, "V", steps
    elif n is None:
        n = (p * v) / (R_GAS_CONSTANT * t_k)
        steps.append(rf"n = \frac{{PV}}{{RT}} = \frac{{{p} \times {v}}}{{{R_GAS_CONSTANT} \times {t_k:.2f}}}")
        steps.append(rf"n = {n:.4f} \text{{ moles}}")
        return n, "n", steps
    else:
        t_k_calc = (p * v) / (n * R_GAS_CONSTANT)
        t_c_calc = t_k_calc - 273.15
        steps.append(rf"T \text{{ (K)}} = \frac{{PV}}{{nR}} = \frac{{{p} \times {v}}}{{{n} \times {R_GAS_CONSTANT}}} = {t_k_calc:.2f} \text{{ K}}")
        steps.append(rf"T \text{{ (^\circ C)}} = {t_k_calc:.2f} - 273.15 = {t_c_calc:.2f}^\circ\text{{C}}")
        return t_c_calc, "T", steps