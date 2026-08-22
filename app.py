"""
ChemSolver 9-10: Streamlit Web Application Entry Point.
"""

import streamlit as st

from engine.mole_calc import (
    calculate_moles_from_mass, calculate_mass_from_moles,
    calculate_particles, calculate_moles_from_particles
)
from engine.solution_calc import (
    calculate_molarity, calculate_moles_for_solution,
    calculate_mass_percent, calculate_volume_percent
)
from engine.gas_laws import boyles_law, charles_law, ideal_gas_law
from engine.ph_calc import (
    calculate_ph_from_h, calculate_poh_from_oh, calculate_h_from_ph
)
from engine.equilibrium_calc import calculate_kc

from utils.validators import (
    validate_positive, validate_non_negative,
    validate_temperature_kelvin, validate_ph_range
)

st.set_page_config(page_title="ChemSolver 9-10", page_icon="🧪", layout="wide")

st.title("🧪 ChemSolver 9-10")
st.caption("Step-by-Step Chemistry Numerical Solver for Class 9th & Matric (10th) Students")

st.sidebar.title("📌 Navigation")
module = st.sidebar.radio(
    "Select a Chemistry Module:",
    ["Mole Concept", "Solutions & Molarity", "Gas Laws", "pH & Acids/Bases", "Chemical Equilibrium"]
)

def render_solution(given_data: dict, formula: str, steps: list, final_result: str):
    st.markdown("### 📊 Solution Breakdown")
    col1, col2 = st.columns([1, 1])
    with col1:
        st.subheader("1. Given Data")
        for key, val in given_data.items():
            st.write(f"• **{key}:** `{val}`")
        st.subheader("2. Formula Used")
        st.latex(formula)

    with col2:
        st.subheader("3. Step-by-Step Working")
        for step in steps:
            st.latex(step)
            
    st.success(f"### 🎉 Final Answer: {final_result}")

if module == "Mole Concept":
    st.header("⚖️ Mole Concept Calculations")
    calc_type = st.selectbox("Choose Calculation Type:", ["Mass to Moles", "Moles to Mass", "Moles to Particles (Avogadro's Number)", "Particles to Moles"])

    if calc_type == "Mass to Moles":
        mass = st.number_input("Mass of Substance (g):", min_value=0.0, value=18.0, step=0.1)
        molar_mass = st.number_input("Molar Mass (g/mol):", min_value=0.1, value=18.015, step=0.1)
        if st.button("Solve"):
            err = validate_positive(mass, "Mass") or validate_positive(molar_mass, "Molar Mass")
            if err: st.error(err)
            else:
                moles, steps = calculate_moles_from_mass(mass, molar_mass)
                render_solution({"Mass (m)": f"{mass} g", "Molar Mass (M)": f"{molar_mass} g/mol"}, r"n = \frac{m}{M}", steps, f"{moles:.4f} moles")

    elif calc_type == "Moles to Mass":
        moles = st.number_input("Number of Moles (n):", min_value=0.0, value=1.0, step=0.1)
        molar_mass = st.number_input("Molar Mass (g/mol):", min_value=0.1, value=44.01, step=0.1)
        if st.button("Solve"):
            err = validate_positive(moles, "Moles") or validate_positive(molar_mass, "Molar Mass")
            if err: st.error(err)
            else:
                mass, steps = calculate_mass_from_moles(moles, molar_mass)
                render_solution({"Moles (n)": f"{moles} mol", "Molar Mass (M)": f"{molar_mass} g/mol"}, r"m = n \times M", steps, f"{mass:.4f} g")

    elif calc_type == "Moles to Particles (Avogadro's Number)":
        moles = st.number_input("Number of Moles (n):", min_value=0.0, value=2.0, step=0.1)
        if st.button("Solve"):
            err = validate_positive(moles, "Moles")
            if err: st.error(err)
            else:
                particles, steps = calculate_particles(moles)
                render_solution({"Moles (n)": f"{moles} mol", "Avogadro's Constant (Na)": "6.022 × 10²³"}, r"N = n \times N_A", steps, f"{particles:.4e} particles")

    elif calc_type == "Particles to Moles":
        particles = st.number_input("Total Particle Count (N):", min_value=0.0, value=1.204e24, format="%.3e")
        if st.button("Solve"):
            err = validate_positive(particles, "Particle count")
            if err: st.error(err)
            else:
                moles, steps = calculate_moles_from_particles(particles)
                render_solution({"Particles (N)": f"{particles:.4e}", "Avogadro's Constant (Na)": "6.022 × 10²³"}, r"n = \frac{N}{N_A}", steps, f"{moles:.4f} moles")

elif module == "Solutions & Molarity":
    st.header("🧪 Solutions & Concentration")
    calc_type = st.selectbox("Choose Calculation Type:", ["Molarity (M = n / V)", "Required Moles from Molarity", "Percentage Concentration (% w/w)", "Percentage Concentration (% v/v)"])

    if calc_type == "Molarity (M = n / V)":
        moles = st.number_input("Moles of Solute (n):", min_value=0.0, value=0.5, step=0.1)
        vol_l = st.number_input("Volume of Solution (Liters):", min_value=0.0, value=1.0, step=0.1)
        if st.button("Solve"):
            err = validate_positive(moles, "Moles") or validate_positive(vol_l, "Volume")
            if err: st.error(err)
            else:
                molarity, steps = calculate_molarity(moles, vol_l)
                render_solution({"Moles (n)": f"{moles} mol", "Volume (V)": f"{vol_l} L"}, r"M = \frac{n}{V}", steps, f"{molarity:.4f} M")

    elif calc_type == "Required Moles from Molarity":
        molarity = st.number_input("Target Molarity (M):", min_value=0.0, value=2.0, step=0.1)
        vol_l = st.number_input("Volume of Solution (Liters):", min_value=0.0, value=2.5, step=0.1)
        if st.button("Solve"):
            err = validate_positive(molarity, "Molarity") or validate_positive(vol_l, "Volume")
            if err: st.error(err)
            else:
                moles, steps = calculate_moles_for_solution(molarity, vol_l)
                render_solution({"Molarity (M)": f"{molarity} M", "Volume (V)": f"{vol_l} L"}, r"n = M \times V", steps, f"{moles:.4f} moles")

    elif calc_type == "Percentage Concentration (% w/w)":
        solute_g = st.number_input("Solute Mass (g):", min_value=0.0, value=10.0, step=1.0)
        solution_g = st.number_input("Total Solution Mass (g):", min_value=0.0, value=100.0, step=1.0)
        if st.button("Solve"):
            err = validate_positive(solute_g, "Solute Mass") or validate_positive(solution_g, "Solution Mass")
            if err: st.error(err)
            elif solute_g > solution_g: st.error("Solute mass cannot exceed total solution mass.")
            else:
                pct, steps = calculate_mass_percent(solute_g, solution_g)
                render_solution({"Solute Mass": f"{solute_g} g", "Solution Mass": f"{solution_g} g"}, r"\% (w/w) = \left(\frac{\text{Mass of Solute}}{\text{Mass of Solution}}\right) \times 100", steps, f"{pct:.2f}%")

    elif calc_type == "Percentage Concentration (% v/v)":
        solute_ml = st.number_input("Solute Volume (mL):", min_value=0.0, value=50.0, step=1.0)
        solution_ml = st.number_input("Total Solution Volume (mL):", min_value=0.0, value=250.0, step=1.0)
        if st.button("Solve"):
            err = validate_positive(solute_ml, "Solute Volume") or validate_positive(solution_ml, "Solution Volume")
            if err: st.error(err)
            elif solute_ml > solution_ml: st.error("Solute volume cannot exceed total solution volume.")
            else:
                pct, steps = calculate_volume_percent(solute_ml, solution_ml)
                render_solution({"Solute Volume": f"{solute_ml} mL", "Solution Volume": f"{solution_ml} mL"}, r"\% (v/v) = \left(\frac{\text{Volume of Solute}}{\text{Volume of Solution}}\right) \times 100", steps, f"{pct:.2f}%")

elif module == "Gas Laws":
    st.header("🎈 Gas Laws Solver")
    law_choice = st.selectbox("Select Gas Law:", ["Boyle's Law (P1V1 = P2V2)", "Charles's Law (V1/T1 = V2/T2)", "Ideal Gas Law (PV = nRT)"])

    if law_choice == "Boyle's Law (P1V1 = P2V2)":
        target = st.selectbox("Target Variable to Solve For:", ["P2", "V2", "P1", "V1"])
        col1, col2 = st.columns(2)
        with col1:
            p1 = None if target == "P1" else st.number_input("Initial Pressure P1 (atm):", value=1.0, step=0.1)
            v1 = None if target == "V1" else st.number_input("Initial Volume V1 (L):", value=2.0, step=0.1)
        with col2:
            p2 = None if target == "P2" else st.number_input("Final Pressure P2 (atm):", value=2.0, step=0.1)
            v2 = None if target == "V2" else st.number_input("Final Volume V2 (L):", value=1.0, step=0.1)
        if st.button("Solve"):
            result, var_name, steps = boyles_law(p1, v1, p2, v2)
            given = {k: f"{v}" for k, v in {"P1": p1, "V1": v1, "P2": p2, "V2": v2}.items() if v is not None}
            render_solution(given, r"P_1 V_1 = P_2 V_2", steps, f"{var_name} = {result:.4f}")

    elif law_choice == "Charles's Law (V1/T1 = V2/T2)":
        target = st.selectbox("Target Variable to Solve For:", ["V2", "T2", "V1", "T1"])
        col1, col2 = st.columns(2)
        with col1:
            v1 = None if target == "V1" else st.number_input("Initial Volume V1 (L):", value=2.0, step=0.1)
            t1_c = None if target == "T1" else st.number_input("Initial Temp T1 (°C):", value=25.0, step=1.0)
        with col2:
            v2 = None if target == "V2" else st.number_input("Final Volume V2 (L):", value=4.0, step=0.1)
            t2_c = None if target == "T2" else st.number_input("Final Temp T2 (°C):", value=50.0, step=1.0)
        if st.button("Solve"):
            err = validate_temperature_kelvin(t1_c) if t1_c is not None else None
            if not err and t2_c is not None: err = validate_temperature_kelvin(t2_c)
            if err: st.error(err)
            else:
                result, var_name, steps = charles_law(v1, t1_c, v2, t2_c)
                given = {k: f"{v}" for k, v in {"V1": v1, "T1 (°C)": t1_c, "V2": v2, "T2 (°C)": t2_c}.items() if v is not None}
                render_solution(given, r"\frac{V_1}{T_1} = \frac{V_2}{T_2}", steps, f"{var_name} = {result:.4f}")

    elif law_choice == "Ideal Gas Law (PV = nRT)":
        target = st.selectbox("Target Variable to Solve For:", ["P", "V", "n", "T"])
        col1, col2 = st.columns(2)
        with col1:
            p = None if target == "P" else st.number_input("Pressure P (atm):", value=1.0, step=0.1)
            v = None if target == "V" else st.number_input("Volume V (L):", value=22.4, step=0.1)
        with col2:
            n = None if target == "n" else st.number_input("Moles n (mol):", value=1.0, step=0.1)
            t_c = None if target == "T" else st.number_input("Temperature T (°C):", value=0.0, step=1.0)
        if st.button("Solve"):
            err = validate_temperature_kelvin(t_c) if t_c is not None else None
            if err: st.error(err)
            else:
                result, var_name, steps = ideal_gas_law(p, v, n, t_c)
                given = {k: f"{v}" for k, v in {"P": p, "V": v, "n": n, "T (°C)": t_c}.items() if v is not None}
                render_solution(given, r"PV = nRT", steps, f"{var_name} = {result:.4f}")

elif module == "pH & Acids/Bases":
    st.header("🧫 pH and pOH Calculations")
    calc_type = st.selectbox("Choose Calculation Type:", ["pH and pOH from [H+]", "pH and pOH from [OH-]", "[H+] Concentration from pH"])

    if calc_type == "pH and pOH from [H+]":
        h_conc = st.number_input("[H+] Concentration (M):", value=1.0e-7, format="%.4e")
        if st.button("Solve"):
            err = validate_positive(h_conc, "[H+] Concentration")
            if err: st.error(err)
            else:
                ph, poh, steps = calculate_ph_from_h(h_conc)
                render_solution({"[H+] Concentration": f"{h_conc:.4e} M"}, r"\text{pH} = -\log_{10}[\text{H}^+]", steps, f"pH = {ph:.2f}, pOH = {poh:.2f}")

    elif calc_type == "pH and pOH from [OH-]":
        oh_conc = st.number_input("[OH-] Concentration (M):", value=1.0e-3, format="%.4e")
        if st.button("Solve"):
            err = validate_positive(oh_conc, "[OH-] Concentration")
            if err: st.error(err)
            else:
                ph, poh, steps = calculate_poh_from_oh(oh_conc)
                render_solution({"[OH-] Concentration": f"{oh_conc:.4e} M"}, r"\text{pOH} = -\log_{10}[\text{OH}^-]", steps, f"pH = {ph:.2f}, pOH = {poh:.2f}")

    elif calc_type == "[H+] Concentration from pH":
        ph = st.number_input("pH Value:", min_value=0.0, max_value=14.0, value=7.0, step=0.1)
        if st.button("Solve"):
            err = validate_ph_range(ph)
            if err: st.error(err)
            else:
                h_conc, steps = calculate_h_from_ph(ph)
                render_solution({"pH": f"{ph}"}, r"[\text{H}^+] = 10^{-\text{pH}}", steps, f"[H+] = {h_conc:.4e} M")

elif module == "Chemical Equilibrium":
    st.header("⚖️ Chemical Equilibrium Constant (Kc)")
    st.markdown("For reaction: **aA + bB ⇌ cC + dD**")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Reactants")
        a_coeff = st.number_input("Coefficient 'a':", min_value=1, value=1, step=1)
        a_conc = st.number_input("[A] Concentration (M):", min_value=0.001, value=0.5, step=0.1)
        b_coeff = st.number_input("Coefficient 'b':", min_value=1, value=1, step=1)
        b_conc = st.number_input("[B] Concentration (M):", min_value=0.001, value=0.5, step=0.1)
    with col2:
        st.subheader("Products")
        c_coeff = st.number_input("Coefficient 'c':", min_value=1, value=1, step=1)
        c_conc = st.number_input("[C] Concentration (M):", min_value=0.001, value=1.0, step=0.1)
        d_coeff = st.number_input("Coefficient 'd':", min_value=1, value=1, step=1)
        d_conc = st.number_input("[D] Concentration (M):", min_value=0.001, value=1.0, step=0.1)

    if st.button("Solve"):
        err = validate_positive(a_conc, "[A]") or validate_positive(b_conc, "[B]") or validate_positive(c_conc, "[C]") or validate_positive(d_conc, "[D]")
        if err: st.error(err)
        else:
            kc, steps = calculate_kc(a_conc, b_conc, c_conc, d_conc, a_coeff, b_coeff, c_coeff, d_coeff)
            render_solution(
                {"Reactant [A]": f"{a_conc} M (coeff {a_coeff})", "Reactant [B]": f"{b_conc} M (coeff {b_coeff})", "Product [C]": f"{c_conc} M (coeff {c_coeff})", "Product [D]": f"{d_conc} M (coeff {d_coeff})"},
                r"K_c = \frac{[\text{C}]^c [\text{D}]^d}{[\text{A}]^a [\text{B}]^b}",
                steps,
                f"Kc = {kc:.4e}"
            )